import os
import json
import google.generativeai as genai 
from PIL import Image 



working_dir = os.path.dirname(os.path.abspath(__file__))

config_file_path =f"{working_dir}/config.json" 

config_data = json.load(open(config_file_path))

#load the api key
GOOGLE_API_KEY = config_data['GOOGLE_API_KEY']

#configuring google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_pro():
    gemini_pro_model = genai.GenerativeModel('gemini-pro')
    return gemini_pro_model

def load_gemini_vision_pro_model(promte, image):
    gemini_vision_pro_model = genai.GenerativeModel('gemini-1.5-flash')
    response = gemini_vision_pro_model.generate_content([promte, image])
    result = response.text
    return result

def load_gemini_vision_pro_model_for_Health(input,promte, image):
    gemini_vision_pro_model = genai.GenerativeModel('gemini-1.5-flash')
    response = gemini_vision_pro_model.generate_content([input,promte, image[0]])
    result = response.text
    return result


