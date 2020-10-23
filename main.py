import requests
import os
from flask import Flask
from flask import request
app = Flask(__name__)
import json
import io
from twilio.rest import Client

account_sid = "AC7a15814cc0850e87d0168b1744d12561"
auth_token  = "c6346342a32471b7a929b52e1659cef4"
FROM="+12015483553"

def sendMessageFunc(data):
        try:
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                        to=data['to'],
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
    

    
        
