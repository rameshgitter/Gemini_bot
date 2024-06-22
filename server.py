from flask import Flask, render_template, request
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "There is a cancer patient and you are a medical guidance expert who makes the patient feel good."

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]
    response = chat.send_message(instruction + user_message)
    return response.text


