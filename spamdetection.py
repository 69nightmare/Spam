import pandas as pd
import numpy as np
df=pd.read_csv('spam.csv',encoding="utf-8")
df.head(3)
df.shape
df.info()
df.head()
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
df.sample(5)
df.rename(columns={'v1':'target','v2':'text'},inplace=True)
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
encoder.fit(df['target'])
df['target']=encoder.transform(df['target'])
df.head()
df.isnull().sum()
df.duplicated().sum()
df=df.drop_duplicates(keep='first')
df.duplicated().sum()
df.shape
import matplotlib.pyplot as plt
import seaborn as sns
df['target'].value_counts()
plt.pie(df['target'].value_counts(),labels=['ham','spam'],autopct='%0.2f')
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
df['num_characters']=df['text'].apply(len)
df.head()
df['num_words']=df['text'].apply(lambda x:len(nltk.word_tokenize(x)))
df['num_sentences']=df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))
df
df.describe()
df[df['target']==0][['num_characters','num_words','num_sentences']].describe()
df[df['target']==1][['num_characters','num_words','num_sentences']].describe()
sns.histplot(df[df['target']==0]['num_characters'])
sns.histplot(df[df['target']==1]['num_characters'],color='red')
sns.pairplot(df,hue='target')
numeric_df = df[['target','num_characters','num_words','num_sentences']]
sns.heatmap(numeric_df.corr(), annot=True)
df.head()
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
ps.stem('loving')
import string
def transform_text(text):
    text=text.lower()
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
transform_text('Shivam is LoviNg 20%^&8U')
df['transformed_text']=df['text'].apply(transform_text)
df.head()
from wordcloud import WordCloud
wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
spam_wc=wc.generate(df[df['target']==1]['transformed_text'].str.cat(sep=" "))
ham_wc=wc.generate(df[df['target']==0]['transformed_text'].str.cat(sep=" "))
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=3000)
X=tfidf.fit_transform(df['transformed_text']).toarray()
X
X.shape
y=df['target'].values
y
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
mnb=MultinomialNB()
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,ConfusionMatrixDisplay
mnb.fit(X_train,y_train)
y_pred2=mnb.predict(X_test)
cm=confusion_matrix(y_test,y_pred2)
print(accuracy_score(y_test,y_pred2))
print(cm)
print(precision_score(y_test,y_pred2))
disp=ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test,y_pred2))
import pickle
print("Saving the vectorizer and model to disk...")
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)
with open('model.pkl', 'wb') as f:
    pickle.dump(mnb, f)
print("Model saved successfully as model.pkl and vectorizer.pkl.")
