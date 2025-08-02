import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "There is a cancer patient and you are a medical guidance expert who makes the patient feel good."

# Vercel Python serverless function handler

def handler(request):
    path = request.path
    if path == "/get_response" and request.method == "POST":
        # Parse form data
        user_message = request.form.get("user_message", "")
        response = chat.send_message(instruction + user_message)
        return response.text
    else:
        # Serve index.html for all other routes
        with open(os.path.join(os.path.dirname(__file__), '../templates/index.html')) as f:
            html = f.read()
        return html
