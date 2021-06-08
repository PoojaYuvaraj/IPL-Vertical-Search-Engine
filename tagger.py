from preprocess import lemmas
from gensim import corpora
import gensim
import re

tag_list = []
dictionary = corpora.Dictionary([lemmas])
corp = [dictionary.doc2bow(text) for text in [lemmas]]
NUM_TOPICS = 1
ldamodel = gensim.models.ldamodel.LdaModel(corp, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics(num_words=2)
for topic in topics:
    words = re.findall(r"[a-zA-z]*",topic[1])
    tags = [word for word in words if len(word) > 1]
    tag_list.append(tags) 
    
print(tag_list)