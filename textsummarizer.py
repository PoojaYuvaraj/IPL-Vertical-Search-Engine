import heapq
import nltk
from preprocess import summarize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
stop_words = set(stopwords.words("english"))

summaries = []
sentences = []
for s in summarize:
    sentences.append(sent_tokenize(s))
    
for sentence in sentences:
    word_frequencies = {}
    for word in nltk.word_tokenize(','.join(sentence)):
        if word not in stop_words:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
                
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        
    sentence_scores = {}
    for sent in sentence:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30 and len(sent.split(' ')) > 15:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
                        
    summary_sentences = heapq.nlargest(1, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    summaries.append(summary)

