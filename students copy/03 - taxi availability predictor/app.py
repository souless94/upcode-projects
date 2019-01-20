from flask import Flask, flash, redirect, render_template, request, session, abort
# From notebook
import pandas as pd

# helper functions 
df_total_taxis = pd.read_csv(r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python projects\lesson 6\students copy\03 - taxi availability predictor\data\public-transport-capacity-monthly-taxi-population.csv")
def get_available_taxi(date,hour):
    df_taxis = pd.read_csv(r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python projects\lesson 6\students copy\03 - taxi availability predictor\data\{}.csv".format(date))
    if hour < 10: # format the timestamp to include 0 padding
        h = "0{}".format(hour)
    else:
        h = hour
    timestamp = "{}T{}:00:00".format(date,h)
    return df_taxis.loc[df_taxis['timestamp'] == timestamp].available_taxis.iloc[0]

def get_total_number_of_taxi_by_year_month(year_month):
    return df_total_taxis.loc[df_total_taxis['month']==year_month]["taxi_fleet"].sum()


def predictor(year,month,date,hour):
    if date < 10:
        d = "0{}".format(date)
    else:
        d = date
    total_taxis = get_total_number_of_taxi_by_year_month("{}-{}".format(year,month))
    available_taxis = get_available_taxi("{}-{}-{}".format(year,month,d),hour)
    return available_taxis/total_taxis * 100

######
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods =['POST'])
def predict():
    day = request.form['day']
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    date = int(days.index(day)) + 4
    hour = int(request.form['hour'])
    year = 2017
    month = 12
    probability = round(predictor(year,month,date,hour),2)
    return render_template("result.html",probability = probability)

if __name__ == "__main__":
    app.run()