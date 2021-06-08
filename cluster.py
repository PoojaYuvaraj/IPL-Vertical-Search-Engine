from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import corpus as docs
from sklearn.cluster import KMeans
import numpy as np

cluster = {}
n_cluster = 2
vectorizer = TfidfVectorizer(stop_words='english')
doc_matrix = vectorizer.fit_transform(docs)
clusterer = KMeans(n_clusters=n_cluster, verbose=True)
clusterer.fit(doc_matrix)

y_kmeans = list(clusterer.predict(doc_matrix))


labels = list(set(y_kmeans)) 

for j in range(n_cluster):
    indices = [i for i, x in enumerate(y_kmeans) if x == labels[j]]
    cluster[labels[j]] = indices



