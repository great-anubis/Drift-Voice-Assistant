from transformers import pipeline
from huggingface_hub import login

# Authenticate with Hugging Face
login(token='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')

# Initialize the Hugging Face pipeline for text generation
text_generator = pipeline('text-generation', model='gpt2')

def generate_response(text):
    # Use the pipeline to generate a response
    result = text_generator(text, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']
