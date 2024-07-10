from transformers import pipeline

nlp_pipeline = pipeline('sentiment-analysis')

def analyze_text(text):
    return nlp_pipeline(text)
