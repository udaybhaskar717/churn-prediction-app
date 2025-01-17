import os
import numpy as np
import mlflow.sklearn
from flask import Flask, render_template, request,jsonify
import mlflow

import mlflow

mlflow.set_tracking_uri("file:///C:/Users/udayb/OneDrive/Desktop/MLprojects/1.%20ChurnProject/mlruns")

model_uri = 'runs:/63779fd59fdd45a9a98a1dd02b93a47d/model'
model = mlflow.sklearn.load_model(model_uri)


# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract features from form input (assuming features are provided in the order they are required)
        features = [float(request.form[f"feature{i}"]) for i in range(1, 20)]

        # Convert to numpy array
        features = np.array(features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features).tolist()[0]

        # Return the result as a rendered template
        return render_template("result.html", prediction=prediction, probability=probability)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
