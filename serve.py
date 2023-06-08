from flask import Flask, request, jsonify
from your_package.translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french():
    data = request.get_json()
    english_text = data.get('text')
    french_text = english_to_french(english_text)
    response = {'translated_text': french_text}
    return jsonify(response)

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english():
    data = request.get_json()
    french_text = data.get('text')
    english_text = french_to_english(french_text)
    response = {'translated_text': english_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
