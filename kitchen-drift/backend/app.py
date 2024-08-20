from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React frontend

# Initialize Cohere client with API key from environment variables
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("Cohere API key not found. Please set COHERE_API_KEY in your .env file.")
co = cohere.Client(cohere_api_key)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Generate a response from Cohere
        response = co.generate(
            model='command',
            prompt=(
                "You are Drift, a highly knowledgeable kitchen assistant. "
                "Your primary focus is to help with kitchen tasks, cooking advice, and recipes. "
                "Please provide clear, concise, and practical advice related to the kitchen. "
                f"Question: {user_input}"
            ),
            max_tokens=250,
            temperature=0.7
        )

        # Extract and clean the generated text
        if response.generations and response.generations[0].text:
            message = response.generations[0].text.strip()
            return jsonify({"message": message})
        else:
            return jsonify({"error": "No response generated by Cohere"}), 500

    except cohere.CohereError as e:
        # Handle Cohere API-specific errors
        return jsonify({"error": f"Cohere API error: {str(e)}"}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask app with debug mode on for development
    app.run(debug=True)