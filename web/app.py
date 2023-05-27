import sys
import os, io
import json
import openai
import requests
# import whisper
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.dialects.postgresql import JSON, JSONB
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
# from azure.storage.blob import BlobServiceClient, ContainerClient, __version__
# import pandas as pd
# from datetime import datetime, date
# import math
from flask_cors import CORS, cross_origin

# FLASK APP CONF
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['ALLOWED_AUDIO_EXTENSIONS'] = ['.mp3', '.wav', '.mpeg', '.ogg']
api = Api(app)

# OPEN AI MODEL CONF
# model = whisper.load_model("tiny")
openai.api_key = os.getenv("OPENAI_API_KEY")

# FUNCTIONS
def complete(prompt,user):
    response = openai.Completion.create(
        # model='curie:ft-ia-aplicada-2023-02-25-16-59-44',
        # temperature=0.4,
        # max_tokens=200,
        # prompt=prompt
        model='curie:ft-ia-aplicada-2023-03-02-15-36-56', 
        temperature=0.3,
        max_tokens=300,
        prompt=prompt + "\n\n###\n\n",
        stop='###',
        user=user
    )
# 
    response_text = response.choices[0].text.strip()
    return response_text

# # ROUTES
# @app.route('/')
# @cross_origin()
# def welcome():
#     return 'The server is working Julian!' 

@app.route('/model-llm',methods = ['POST'])
@cross_origin()
def model():
    # Use LLM model
    data = request.json
    prompt = data.get('prompt')
    response = complete(prompt,1)

    res = {
        'ok': True,
        'prompt': data.get('prompt'),
        'response': response
    }

    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)