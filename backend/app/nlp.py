from transformers import pipeline

# Initialize NLP pipeline
nlp_pipeline = pipeline("text-generation", model="gpt2")

def generate_response(input_text):
    conversation = nlp_pipeline(input_text, max_length=50)
    response = conversation[0]['generated_text']
    return response
