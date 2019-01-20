from flask import Flask, flash, redirect, render_template, request, session, abort
import pygal
from pygal.style import DarkSolarizedStyle
# From notebook
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\wen kai\Downloads\y4s1\upcode-python\upcode-python projects\lesson 6\students copy\04 - psi predictor\psi data\december-2017-psi.csv")
median_values = []
for i in range(23):
    median_values.append(df.loc[df['hour'] == i].psi.median())
new_df = pd.DataFrame({"hour": range(len(median_values)), "psi" : median_values})

# function
p_median = np.poly1d(np.polyfit(new_df["hour"],new_df["psi"],6))
graph_values = list(map(p_median,range(0, 24)))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods =['POST'])
def predict():
    hour = int(request.form['hour'])
    predicted_psi = round(p_median(hour),2)
    line_chart = pygal.Line(style=DarkSolarizedStyle,disable_xml_declaration=True)
    line_chart.title = 'Psi chart'
    line_chart.x_labels = map(str, range(0, 24))
    line_chart.add('psi',graph_values)
    return render_template("result.html", psi = predicted_psi ,thegraph = line_chart)

if __name__ == "__main__":
    app.run()