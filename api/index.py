import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "There is a cancer patient and you are a medical guidance expert who makes the patient feel good."

def handler(request):
    if request.method == "POST" and request.path == "/get_response":
        try:
            data = request.json()
            user_message = data.get("user_message", "")
            response = chat.send_message(instruction + user_message)
            return (response.text, 200, {"Content-Type": "text/plain"})
        except Exception as e:
            return (f"Error: {str(e)}", 500, {"Content-Type": "text/plain"})
    else:
        try:
            with open(os.path.join(os.path.dirname(__file__), '../templates/index.html')) as f:
                html = f.read()
            return (html, 200, {"Content-Type": "text/html"})
        except Exception as e:
            return (f"Error: {str(e)}", 500, {"Content-Type": "text/plain"})
