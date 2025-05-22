from model import compute_similarity

# Example
text1 = "Ashutosh is the great person."
text2 = "ashutosh is a best person"

score = compute_similarity(text1, text2)
print(f"Similarity Score: {score}")
