import joblib
from .preprocess import preprocess_email

svc = joblib.load('svc_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_email(email):
    email = preprocess_email(email)
    email_vectorized = vectorizer.transform([email])
    prediction = svc.predict(email_vectorized)
    return 'Spam' if prediction == 1 else 'Not Spam'
