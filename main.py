import pickle
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder="docs", static_folder="./docs/static")
# housing_Mumbai = pd.read_csv("Mumbai_2023.csv")
pipe_Mumbai = pickle.load(open("pickleFiles/XGB_Mumbai.pkl", "rb"))
# housing_Bangalore = pd.read_csv("Bangalore_2023.csv")
pipe_Bangalore = pickle.load(open("pickleFiles/XGB_Bangalore.pkl", "rb"))

pipe_Chennai = pickle.load(open("pickleFiles/XGB_Chennai.pkl", "rb"))

pipe_Delhi = pickle.load(open("pickleFiles/XGB_Delhi.pkl", "rb"))


@app.route('/')
def index():
    return render_template("index.html")

# to get form data and apply ML model for prediction.


@app.route("/predict", methods=["POST"])
def predict():
    city = request.form.get("city")
    location = request.form.get("location")
    bhk = request.form.get("bhk")
    area = request.form.get("total_sqft")
    if city == "Mumbai":
        input = pd.DataFrame([[location, area, bhk]], columns=[
                             "location", "area", "bhk"])
        prediction = pipe_Mumbai.predict(input)[0]
        return str(prediction)

    elif city == "Bangalore":
        input = pd.DataFrame([[location, area, bhk]], columns=[
                             "location", "area", "bhk"])
        prediction = pipe_Bangalore.predict(input)[0]
        return str(prediction)

    elif city == "Chennai":
        input = pd.DataFrame([[location, area, bhk]], columns=[
                             "location", "area", "bhk"])
        prediction = pipe_Chennai.predict(input)[0]
        return str(prediction)

    elif city == "Delhi":
        input = pd.DataFrame([[location, area, bhk]], columns=[
                             "location", "area", "bhk"])
        prediction = pipe_Delhi.predict(input)[0]
        return str(prediction)


@app.route("/map")  # map tab
def map():
    return render_template("map.html")


@app.route("/about")  # about tab
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
