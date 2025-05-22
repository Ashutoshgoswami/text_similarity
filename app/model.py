import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open('saved_models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def compute_similarity(text1: str, text2: str) -> float:
    vectors = vectorizer.transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(float(similarity), 3)
