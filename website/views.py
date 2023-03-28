from flask import Blueprint, render_template, redirect, url_for, jsonify, request
import openai
import os

views = Blueprint('views', __name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")

@views.route('/generate_names', methods=['POST'])
def generate_names():
    input_text = request.form.get('input_text')
    prompt_text = "Sugira nomes para uma startup com a seguinte descrição: "
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt_text + input_text,
    temperature=0.6,
    max_tokens=150,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1,
    )
    output = response["choices"][0]["text"].strip()
    return jsonify({"output_text": output})