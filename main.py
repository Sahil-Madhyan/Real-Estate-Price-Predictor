from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__,template_folder="docs",static_folder="static")
data = pd.read_csv("./excel_sheets/Delhi.csv")


@app.route('/')
def index():
    locations = sorted(data['Location'].unique())
    return render_template('index.html', locations=locations)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
