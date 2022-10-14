from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
#from new_data_doc_main import prediction, forest
import pickle

app = Flask(__name__)

model = pickle.load(open('prediction_model.pkl', 'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction_model", methods=['POST','GET'])
def prediction_model():

    symptoms = request.form.getlist('#ID name')
    prediction = model.prediction(symptoms)
    pred_output = prediction(symptoms)
    return render_template("sample-inner-page.html", pred_output=pred_output, prediction=prediction, symptoms=symptoms)

if __name__ == "__main__":
    app.run(debug=True)