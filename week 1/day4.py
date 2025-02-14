# def whatsapp_ban(name):
#     return f"Ban {name} from WhatsApp"
# print(whatsapp_ban("John"))


# to create a whatsapp bot
# you can use the following code to create a whatsapp bot
# this code will send a message to a user when they send a message to the bot
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio import twiml

# continue coding
# create a flask app
app = Flask(__name__)
CORS(app)

# next line
# create a Twilio client
account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# continue
# create a route for the bot
@app.route("/bot", methods=["POST"])
def bot():
    # get the message from the user
    message = request.form["Body"]
    # send a response back to the user
    response = MessagingResponse()
    response.message("Hello, {0}!".format(message))
    return str(response)

# continue
# run the app
if __name__ == "__main__":
    app.run(debug=True)
