from flask import Flask , flash, redirect, render_template, request, session, abort
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    df_suggestions = pd.read_csv(r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python projects\lesson 6\students copy\05-search bar\data\suggest.csv")
    df_suggestions = df_suggestions['suggestions']
    return render_template("index.html",suggestions = df_suggestions)

@app.route("/predict", methods =['POST'])
def predict():
    searchtxt = request.form['search']
    return render_template("result.html",searchinput = searchtxt)

if __name__ == "__main__":
    app.run()