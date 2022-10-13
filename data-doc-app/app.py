from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from new_data_doc_main import prediction 


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)