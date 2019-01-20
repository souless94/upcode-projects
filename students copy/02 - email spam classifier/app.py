from flask import Flask, flash, redirect, render_template, request, session, abort
# From notebook
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

filename_classifier = r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python-flask\students copy\02 - email spam classifier\classifier.sav"
classifier = pickle.load(open(filename_classifier, 'rb'))
filename_vectorizer = r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python-flask\students copy\02 - email spam classifier\vectorizer.sav"
vectorizer = pickle.load(open(filename_vectorizer, 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods =['POST'])
def predict():
    examples = [request.form['value']]
    example_count = vectorizer.transform(examples)
    print(example_count)
    predictions = classifier.predict(example_count)
    return render_template("result.html",classification = predictions[0])

if __name__ == "__main__":
    app.run()