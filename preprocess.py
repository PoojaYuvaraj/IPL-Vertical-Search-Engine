#import libraries
import glob
import json 
import string 
import re
from collections import defaultdict
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim import corpora
import gensim


#input query
#query = "Rohit Sharma"

#load all documents
documents = glob.glob("Documents/*.json")

#preprocess test
lemmatizer = WordNetLemmatizer() 
stop_words = set(stopwords.words("english"))
translator = str.maketrans('', '', string.punctuation)

#load content from json file
corpus = []
url = []
tag_list = []
summarize = []

for id_,doc in enumerate(documents):
    text = ''
    with open(doc) as f:
         data = json.load(f)
         
         text = text + str(data['text']) + str(data['title'])
         summarize.append(','.join(data['text']))
         url.append(data['url'])
         text = text.lower()
         text = re.sub(r'\d+', '', text)
         text = text.translate(translator)
         word_tokens = word_tokenize(text) 
         filtered_text = [word for word in word_tokens if word not in stop_words]
         lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in filtered_text]
         dictionary = corpora.Dictionary([lemmas])
         corp = [dictionary.doc2bow(text) for text in [lemmas]]
         NUM_TOPICS = 1
         ldamodel = gensim.models.ldamodel.LdaModel(corp, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
         topics = ldamodel.print_topics(num_words=2)
         for topic in topics:
             words = re.findall(r"[a-zA-z]*",topic[1])
             tags = [word for word in words if len(word) > 1]
             tag_list.append(tags) 
         corpus.append(text)