# file: app.py
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send-sms', methods=['POST'])
def send_sms():
    to_number = request.json.get('to')
    if not to_number:
        return jsonify({'error': 'Missing "to" number'}), 400

    account_sid = 'AC690800c168c55a420ec166a8ddfb3d94'
    auth_token = '9082ac3b45defaf9b4d0352c322b2574'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_='+19402835883',
      body='HEllo from python test 2003',
      to='+919168368554'
    )
    print(message.sid)

    return jsonify({'sid': message.sid})
