import spacy
import re
nlp = spacy.load('en')
import contractions
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')


def preprocessing(text):
  text = text.replace('#','')
  text = contractions.fix(text)
  text = re.sub('\S*@\S*\s?',' ',text)
  text = re.sub('https?://\S+|www\.\S+',' ',text)
  text = re.sub('<.*?>',' ',text)
  token= list()
  text = re.sub('[^A-z]', ' ',text)

  lemmatizer = WordNetLemmatizer()
  stop_words = set(stopwords.words('english'))
  preprocessed_sent = ' '.join([lemmatizer.lemmatize(temp.lower()) for temp in text.split() if len(temp)>2])
  return preprocessed_sent