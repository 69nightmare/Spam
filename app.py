from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

app = Flask(__name__)
CORS(app)

try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    print("Warning: Model or vectorizer not found. Please run spamdetection.py first.")

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    try:
        text = nltk.word_tokenize(text)
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        text = nltk.word_tokenize(text)
        
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    
    try:
        stop_words = stopwords.words('english')
    except LookupError:
        nltk.download('stopwords')
        stop_words = stopwords.words('english')
        
    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    transformed_msg = transform_text(text)
    vector_input = tfidf.transform([transformed_msg]).toarray()
    
    result = model.predict(vector_input)[0]
    probabilities = model.predict_proba(vector_input)[0]
    spam_prob = round(probabilities[1] * 100, 2)
    ham_prob = round(probabilities[0] * 100, 2)
    
    return jsonify({
        'prediction': int(result),
        'label': 'Spam' if result == 1 else 'Ham',
        'spam_probability': spam_prob,
        'ham_probability': ham_prob
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
