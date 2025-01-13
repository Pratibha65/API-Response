from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '7jHUusH5.aFMt8jDltFIhuvw2giqQBzsUtVKoF5s6'
API_URL = "https://payload.vextapp.com/hook/7AMKJVV1GX/catch/$(anshika20021028)"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    # Get user query from the form
    user_query = request.form.get('query')

    # Call the external API
    headers = {
        'Content-Type': 'application/json',
        'Apikey': f'Api-Key {API_KEY}'
    }
    data = {
        "payload": user_query
    }
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200:
            res_text = response.json().get('text', 'No response text found.')
            return jsonify({'response': res_text})
        else:
            return jsonify({'response': f"API Error: {response.status_code}"})
    except requests.exceptions.RequestException as e:
        return jsonify({'response': f"Request failed: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
