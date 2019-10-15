from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
from googlesearch import search



# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
  return'Hello World!'

@app.route('/webhook', methods=['POST'])
def webhook():
  data = request.get_json(silent=True)
  print(data)
  food = data['queryResult']['parameters']['food']

  for url in search("Pizza",stop=1):
    item=url

  print(item)

  response= item
  reply={
      "fulfillmentText": response,
      "fulfillmentMessages": [
          {
            "basicCard": {
              "title": "Link to your question!",
              "subtitle": "Smart-Kitchen",
              "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
              "buttons": [
                {
                  "text": "Learn more in detail",
                  "postback": response
                }
              ]
            }
          }
        ]
      }
  return jsonify(reply)



# def detect_intent_texts(project_id, session_id, text, language_code):
#   session_client = dialogflow.SessionsClient()
#   session = session_client.session_path(project_id, session_id)

#   if text:
#     text_input = dialogflow.types.TextInput(
#     text=text, language_code=language_code)
#     query_input = dialogflow.types.QueryInput(text=text_input)
#     response = session_client.detect_intent(
#     session=session, query_input=query_input)

#   return response.query_result.fulfillment_text

# @app.route('/send_message', methods=['POST'])
# def send_message():
#   message = request.form['message']
#   project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
#   fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
#   response_text = { "message":  fulfillment_text }

#   return jsonify(response_text)

if __name__ == '__main__':
   app.run() 