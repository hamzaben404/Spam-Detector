import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from .preprocess.py import preprocess_email
import joblib

def load_dataset(spam_dir, ham_dir):
    emails = []
    labels = []
    
    for filename in os.listdir(spam_dir):
        with open(os.path.join(spam_dir, filename), 'r', encoding='latin-1') as file:
            emails.append(preprocess_email(file.read()))
            labels.append(1)
            
    for filename in os.listdir(ham_dir):
        with open(os.path.join(ham_dir, filename), 'r', encoding='latin-1') as file:
            emails.append(preprocess_email(file.read()))
            labels.append(0)
    
    return emails, labels

spam_dir = './data/spam'  # Update this to your actual path
ham_dir = './data/ham'    # Update this to your actual path

emails, labels = load_dataset(spam_dir, ham_dir)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

svc = svm.SVC(kernel='linear')
svc.fit(X_train, y_train)

joblib.dump(svc, 'svc_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

accuracy = svc.score(X_test, y_test)
print(f'Test accuracy: {accuracy * 100:.2f}%')
