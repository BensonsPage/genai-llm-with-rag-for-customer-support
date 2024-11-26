from flask import Flask, jsonify, request, render_template, url_for, json
# import packages
from datetime import date
from forms import Request
from os import environ

import textwrap
from createcromadatabase import embed_fn, db

import google.generativeai as genai

import os
from dotenv import load_dotenv
from IPython.display import Markdown

app = Flask(__name__)

# Get Environment Variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Get configs
app.config.from_object('config.Config')

# creating the date object of today's date
today_date = date.today()
current_year = str(today_date.year)

# Copyright
app_copyright = (" © " + current_year + " LLM Customer Support")

# Markdown to display response
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    form = Request()

    if form.validate_on_submit():
        # Switch to query mode when generating embeddings.
        embed_fn.document_mode = False

        # receive customer query
        customer_query = form.customer_query.data

        result = db.query(query_texts=[customer_query], n_results=1)
        [[content]] = result["documents"]

        content_oneline = content.replace("\n", " ")
        customer_query_oneline = customer_query.replace("\n", " ")

        # This prompt is where you can specify any guidance on tone, or what topics the model should stick to, or avoid.
        prompt = f"""You are a helpful and informative customer service bot that answers questions using text from the reference content included in the documents directory. 
        Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. 
        However, you are talking to a non-technical audience, so be sure to break down complicated concepts and 
        strike a friendly and conversational tone. If the passage is irrelevant to the answer, you may ignore it.

        QUESTION: {customer_query_oneline}
        PASSAGE: {content_oneline}
        """
        print(prompt)



        # Selecting text model
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        # Write any prompt of your choice
        response = model.generate_content(prompt)
        to_markdown(response.text)

        for chunk in response:
            print(chunk.text)
            print("_" * 80)

    return render_template(
        "index.html",
        form=form,
        response=response.text,
        app_copyright=app_copyright
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", app_copyright=app_copyright), 404

