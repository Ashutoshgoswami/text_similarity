import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv('data\DataNeuron_Text_Similarity.csv')

vectorizer = TfidfVectorizer()

all_texts = df['text1'].tolist() + df['text2'].tolist()
vectorizer.fit(all_texts)

with open('saved_models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Vectorizer saved. No model training required for cosine similarity.")
