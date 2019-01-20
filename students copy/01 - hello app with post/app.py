from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=['POST'])
def predict():
    return render_template("hello.html",name = request.form['name'])

if __name__ == "__main__":
    app.run()