import requests
import os
from flask import Flask
from flask import request
app = Flask(__name__)
import json
import io
from twilio.rest import Client
from flask_cors import CORS, cross_origin
CORS(app)

account_sid = "AC0eda81b4d60ae7f31eb5ae99e6a33bf2"
auth_token  = "078e2dae8f2f431f9fe6f9b48f2f1372"
FROM="+18305212188"

def sendMessageFunc(data):
        try:
                for number in data['to']:
                         client = Client(account_sid, auth_token)
                         message = client.messages.create(
                                 to=number,
                                 from_=FROM,
                                 body=data['message'])
        except Exception as e:
                print(e)
        return "success"

@app.route('/sendMessage', methods=['POST'])
def sendMail():
    data=request.get_json()
    r=sendMessageFunc(data)
    if r=="success":
        return json.dumps({"message": "Message sent successfully"})
    return json.dumps({"message": "Failed"})

@app.route('/', methods=['GET'])
def getData():
    return json.dumps({"msg": "hello-m"})   

if __name__ == '__main__':
    app.run()
    

    
        
