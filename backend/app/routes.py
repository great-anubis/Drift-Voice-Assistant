from flask import jsonify, make_response, request

def process_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return make_response(jsonify({'error': 'Invalid input'}), 400)
    input_text = data['text']
    response_text = generate_response(input_text)
    return make_response(jsonify({'response': response_text}), 200)
