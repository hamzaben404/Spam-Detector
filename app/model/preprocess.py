import re
import string

def preprocess_email(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http[s]?://\S+', 'httpaddr', text)
    text = re.sub(r'\S+@\S+', 'emailaddr', text)
    text = re.sub(r'\b\d+\b', 'number', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text
