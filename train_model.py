import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
import pickle

print("Loading dataset...")
df=pd.read_csv('spam.csv',encoding="utf-8")
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True, errors='ignore')
df.rename(columns={'v1':'target','v2':'text'},inplace=True)

encoder=LabelEncoder()
df['target']=encoder.fit_transform(df['target'])
df=df.drop_duplicates(keep='first')

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps=PorterStemmer()

def transform_text(text):
    text=str(text).lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

print("Preprocessing text...")
df['transformed_text']=df['text'].apply(transform_text)

print("Vectorizing...")
tfidf=TfidfVectorizer(max_features=3000)
X=tfidf.fit_transform(df['transformed_text']).toarray()
y=df['target'].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

print("Training model...")
mnb=MultinomialNB()
mnb.fit(X_train,y_train)
y_pred2=mnb.predict(X_test)
print("Accuracy:", accuracy_score(y_test,y_pred2))
print("Precision:", precision_score(y_test,y_pred2))

print("Saving the vectorizer and model to disk...")
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)
with open('model.pkl', 'wb') as f:
    pickle.dump(mnb, f)
print("Model saved successfully as model.pkl and vectorizer.pkl.")
