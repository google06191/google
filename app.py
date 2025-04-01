from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'

@app.route('/check-spelling', methods=['POST'])
def check_spelling():
    text = request.json['text']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"แก้ไขคำผิดในข้อความนี้: {text}",
        max_tokens=100
    )
    return jsonify({'corrected_text': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)