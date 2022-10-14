from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from new_data_doc_main import prediction, data, clf
import pickle

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction_model")
def prediction_model():
    return render_template("sample-inner-page.html")

if __name__ == "__main__":
    app.run(debug=True)