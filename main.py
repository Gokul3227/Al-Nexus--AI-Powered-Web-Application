import os
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import load_gemini_pro, load_gemini_vision_pro_model, load_gemini_vision_pro_model_for_Health
from PIL import Image
from youtube_transcript_api import YouTubeTranscriptApi


working_dir = os.path.dirname(os.path.abspath(__file__))

#page configuration how page and icon or logo should be present
st.set_page_config(
    page_title="AI Agent",
    page_icon="paste an emoji here",
    layout="centered"
)

with st.sidebar:

    selected = option_menu( menu_title="Features",
                           options= ['ChatAssitant',
                                     "Image Captioning",
                                     "Youtube_Transcript",
                                     "Gemini Health App",
                                     "Embed text",
                                     "ASK me anything"],
                                     menu_icon = 'robot', icons=['chat-dots-fill', "img",
                                                                 'textarea', 'patch-question-fill'],
                                                                default_index=0 )
#function to translate the role btw user and model
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return "user_role"

if selected == 'ChatAssitant':

    model = load_gemini_pro()

    #init chat session in streamlit 
    if 'chat_session' not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
        #streamlit title for chatbot
    st.title("ChatBot")

        #to display the chat history 
    for message in st.session_state.chat_session.history:
         with st.chat_message(translate_role_for_streamlit(message.role)):
              st.markdown(message.parts[0].text)

    #input_field for users message
    user_promt = st.chat_input("Ask Gemini AI>>>>")
    if user_promt:
        st.chat_message('user').markdown(user_promt)

        gemini_response = st.session_state.chat_session.send_message(user_promt)

        #gemini pro response 
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

if selected == 'Image Captioning':

    st.title("Image Captioning-->")
    upload_image = st.file_uploader("Upload An Image here....", type=["jpg","png","jpng"] )
    user_promt = st.text_input("Enter the promt here...!")
    if upload_image is not None and st.button("genrate caption"):
        image = Image.open(upload_image)
        col1, col2 = st.columns(2)
        with col1:
            resized_image = image.resize((800,500))
            st.image(resized_image)   
        respone = load_gemini_vision_pro_model(user_promt, image)

        with col2:
            st.info(respone)

if selected == 'Youtube_Transcript':
    model = load_gemini_pro()
    st.title("Youtube Transcript To Detailed Notes Converter")
    link = st.text_input("Please enter the Yutube link here..")
    
    promte = st.text_area("Enter the Promte here....")
    if link and promte:
        def youtube_transcript(link):
            try:
                video_id = link.split('=')[1]
                print(video_id)
                st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
                youtube_transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

                transcripted_text=''
                for i in youtube_transcript_text:
                    transcripted_text = " " + i['text']

                return transcripted_text
            
            except Exception as e:
                raise e
            
        transcript = youtube_transcript(link)

    def generate_content_by_gemini(promte,transcript):
            response_for_transcript = model.generate_content(promte+transcript)
            result = response_for_transcript

            return result.text
        
    if st.button("Get Trascript"):
            resp = generate_content_by_gemini(promte,transcript)
            st.markdown("## Detailed Summary")
            st.write(resp)
        

def input_image_setup(uploaded_file):
    #check the file uploaded or not 
    if uploaded_file is not None:
        #Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, #Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    
if selected == "Gemini Health App":
    st.title("AI Health ApP")
    def input_image_setup(uploaded_file):
    #check the file uploaded or not 
        if uploaded_file is not None:
            #Read the file into bytes
            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type, #Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file Uploaded")
    upload_image = st.file_uploader("Upload Image here...>", type=['jpg','png','jpng'])
    input = st.text_input("Enter the Query to ask...>")
    image=''
    promte = """You are an expert in nutritionist where you need to see the food items from the image 
                and calculate the total calories, also provide the details of every food items with calories intake in below formate
                
                1.Item 1- no of calaries
                2.Item 2- no of calories
                ---
                ---
                ------"""
    if upload_image is not None :
        image_byte_file = input_image_setup(upload_image)
        if st.button("Get the Calories "):
            
            img = Image.open(upload_image)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img.resize((800,500)))
                get_response_from_Ai = load_gemini_vision_pro_model_for_Health(input,promte,image_byte_file)
            with col2:
                st.info(get_response_from_Ai)
    
    


    



