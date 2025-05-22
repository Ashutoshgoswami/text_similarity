# Semantic Similarity API

This project is designed to compute the **semantic similarity between two paragraphs** using Natural Language Processing techniques. Built with **FastAPI**, the application accepts two text inputs and returns a similarity score between **0 and 1**.

## Technologies Used

- **Programming Language**: Python  
- **Web Framework**: FastAPI  
- **Modeling Approach**: TF-IDF Vectorization + Cosine Similarity  

### Libraries
- `scikit-learn` – for TF-IDF vectorization and cosine similarity
- `pandas` – for data handling
- `FastAPI` – for API development
- `Pydantic` – for request validation
- `Uvicorn` – ASGI server for running FastAPI

### Deployment Platform
- **Heroku**

---

## Project Components

### Model
- Uses **TF-IDF vectorization** combined with **cosine similarity** to compute semantic similarity.
- Vectorizer is trained on a provided dataset and saved for inference.

### API
- A RESTful API built with FastAPI.
- Accepts two paragraph inputs and returns a similarity score.

### Vectorizer
- Pre-trained TF-IDF vectorizer saved and loaded for predictions.

### Deployment
- The entire application is deployed as an API endpoint using **Heroku**.