import pickle

def predict_sales(model_path, day):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([[day]])
    return prediction[0]
