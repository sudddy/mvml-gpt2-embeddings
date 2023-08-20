from flask import Flask,request
from db import store_db 

app = Flask(__name__)

@app.route("/add", methods=['POST'])
def process_input():
    request_data = request.get_json()
    input = request_data['input']
    response = store_db(input)
    if response == True:
        return { "success" : "Embeddings stored in db" }
    else: 
        return { "failure" : "Something went wrong"}