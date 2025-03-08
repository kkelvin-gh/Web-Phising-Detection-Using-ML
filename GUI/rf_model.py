import pickle
import pandas as pd


def predictor(splitted_data):
    print("\nScript rf_model")

    # Load the model from disk
    filename = r'C:\Users\Kelvin\Music\Web Phishing Detection Using Machine Learning\GUI\forest_model1.sav'
    try:
        loaded_model = pickle.load(open(filename, 'rb'))
        print("Model loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

    # Check the shape and columns of the input data
    print(splitted_data.shape)
    print(list(splitted_data.columns))

    # Define the feature columns
    feature_cols = splitted_data.columns[3:14]

    # Ensure the dataframe contains the expected columns
    if not all(col in splitted_data.columns for col in feature_cols):
        print("Feature columns are missing from the input data")
        return None

    # Predict using the loaded model
    try:
        print('Predictions: ')
        preds = loaded_model.predict(splitted_data[feature_cols])
        print("Prediction complete")
        print(preds)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

    # Interpret the prediction
    if preds[0] == 0:
        result = "Phished Webpage"
    else:
        result = "Legitimate Webpage"

    # Optionally, get prediction probabilities
    try:
        score = loaded_model.predict_proba(splitted_data[feature_cols])
        print(f"Prediction probabilities: {score}")
    except Exception as e:
        print(f"Error getting prediction probabilities: {e}")

    return result
