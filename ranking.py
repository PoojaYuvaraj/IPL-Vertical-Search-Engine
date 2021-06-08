#import limbraries 
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import random

#import corpus,query and urls


from cluster import cluster,y_kmeans

#from collections import defaultdict
from textsummarizer import summaries
from preprocess  import corpus,url
from preprocess import tag_list
       

    
def ranker(q):
    query = q

    #Create Tfidf matrix from corpus
    dic = {}
    doc_vectors = TfidfVectorizer().fit_transform([query]+corpus)
    cosine_similarities = linear_kernel(doc_vectors,doc_vectors[0]).flatten()
    
    #Ranking
    for i in range(1,len(cosine_similarities)):
        if cosine_similarities[i] >= 0.01:
            recommend = cluster[y_kmeans[i-1]]
            rec = random.sample(recommend,k=1)
            dic[url[i-1]] = tag_list[i-1],summaries[i-1],url[rec[0]]
            
            
    result = sorted(dic.items(),key = lambda x:x[1],reverse=True)

    print(result)
    #return result
    
ranker('ipl')















