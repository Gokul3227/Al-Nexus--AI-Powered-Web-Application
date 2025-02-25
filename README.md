
# 🧠 AI-Powered Multi-Feature Application

A brief description of what this project does and who it's for, This project is a Streamlit-based web application that integrates various AI-powered features using the Gemini AI models. It provides users with a range of tools, from chatting with an AI assistant to generating image captions and calculating calorie counts from food images.




## 🚀 Features

1. Chat Assistant

    Real-time conversational AI powered by Gemini Pro.

    Maintains chat history within the session.

2. Image Captioning

    Upload an image and get an AI-generated caption based on the provided prompt.

3. Gemini Health App (Calorie Estimator)

    Upload a food image and get calorie estimates for each item.

    AI returns a detailed calorie breakdown.
## 🛠️Setup and Installation

Clone the repository:

git clone https://github.com/yourusername/ai-multi-feature-app.git
cd ai-multi-feature-app

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

📂 Project Structure

.
├── app.py                      # Main application file
├── gemini_utility.py           # Utility functions for Gemini models
├── requirements.txt           # List of required Python packages
└── README.md                  # Project documentation

📄 Configuration

Store your API keys securely in a .json file:

config.json:

{
  "GEMINI_API_KEY": "your_api_key_here"
}

Make sure to load this file securely in your app and avoid committing it to version control. Add config.json to your .gitignore file to prevent accidental exposure.

🚩 How to Use

-Run the app and choose a feature from the sidebar.

-Interact with the AI: Chat or upload images.

-Get results: View AI-generated responses, image captions, or calorie counts.

🧑‍💻 Tech Stack

1.Python

2.Streamlit

3.PIL (Pillow)

4.Gemini AI models