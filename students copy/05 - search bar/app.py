from flask import Flask , flash, redirect, render_template, request, session, abort
import pandas as pd
import mysql.connector
import itertools
# database
def load_db():
  mydb = mysql.connector.connect(
  host="localhost",
  user="tester",
  password="password",
  database = "searchdatabase")
  return mydb
  
def insert_into_db(searchtxt):
  mydb = load_db()
  mycursor = mydb.cursor()
  sql = "INSERT INTO userinputs (searchtxt) VALUES (%s)"
  val = (str(searchtxt),)
  mycursor.execute(sql, val)
  mydb.commit()
  mycursor.close()
  mydb.close()

def get_suggestions():
  mydb = load_db()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM userinputs")
  myresult = mycursor.fetchall()
  myresult = list(itertools.chain.from_iterable(myresult))
  mycursor.close()
  mydb.close()
  return myresult

def remove_suggestions():
  mydb = load_db()
  mycursor = mydb.cursor()
  sql = "DELETE FROM userinputs"
  mycursor.execute(sql)
  mydb.commit()
  mycursor.close()
  mydb.close()

# mycursor.execute("CREATE DATABASE searchdatabase")
# mycursor.execute("CREATE TABLE userinputs (searchtxt VARCHAR(255) )")
#######
app = Flask(__name__)

@app.route("/")
def index():
    myresult = get_suggestions()
    return render_template("index.html",suggestions = myresult)

@app.route("/predict", methods =['POST'])
def predict():
    searchtxt = request.form['search']
    insert_into_db(searchtxt)
    return render_template("result.html",searchinput = searchtxt)

if __name__ == "__main__":
    app.run()