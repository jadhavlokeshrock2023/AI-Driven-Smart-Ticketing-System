import joblib
import os


category_model = joblib.load(
    "ai/models/category_model.pkl"
)


priority_model = joblib.load(
    "ai/models/priority_model.pkl"
)



def predict_category(description):

    return category_model.predict(
        [description]
    )[0]



def predict_priority(description):

    return priority_model.predict(
        [description]
    )[0]