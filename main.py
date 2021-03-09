import os
import openai
from twilio.rest import Client
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse, Message
from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok

openai.api_key = "sk-o608FaXpso8YrUx1KSWdyekG32pwqyhU19YmuEHQ"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def answer(question):
  response = openai.Completion.create(
    engine="davinci",
    prompt="Human:"+question+"\nAI:",
    temperature=0.5,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n", " Human:", " AI:"]
  )
  thing = (response.choices)
  return(thing[0].text)

account_sid = "AC94ef7ded7a49a83b7fdbf6cdd5977c77"
# Your Auth Token from twilio.com/console
auth_token  = "d5829111cb8ba4a2745d177909e83456"
client = Client(account_sid, auth_token)
app = Flask(__name__)
#run_with_ngrok(app)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    resp.message(answer(request.form['Body']))

    return str(resp)

@app.route("/", methods=['GET'])
def index():
    return "Ahoy"

