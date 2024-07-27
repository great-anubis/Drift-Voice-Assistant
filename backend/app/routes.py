from flask import Flask, request, jsonify
from app.nlp import generate_response

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        user_input = data.get('text', '')
        if not user_input:
            return jsonify({'error': 'No input text provided'}), 400
        response = generate_response(user_input)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
