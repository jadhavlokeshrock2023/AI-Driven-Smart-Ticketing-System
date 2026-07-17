import pandas as pd
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB


os.makedirs(
    "ai/models",
    exist_ok=True
)


data = pd.read_csv(
    "ai/ticket_data.csv"
)


# Category Model

category_model = Pipeline([

    (
        "tfidf",
        TfidfVectorizer()
    ),

    (
        "classifier",
        MultinomialNB()
    )

])


category_model.fit(
    data["description"],
    data["category"]
)



joblib.dump(
    category_model,
    "ai/models/category_model.pkl"
)



# Priority Model

priority_model = Pipeline([

    (
        "tfidf",
        TfidfVectorizer()
    ),

    (
        "classifier",
        MultinomialNB()
    )

])


priority_model.fit(
    data["description"],
    data["priority"]
)



joblib.dump(
    priority_model,
    "ai/models/priority_model.pkl"
)



print("AI Category and Priority Models Trained")