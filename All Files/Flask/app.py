from flask import Flask, render_template
import pandas as pd



app = Flask(__name__)
data = ['a', 'b']
@app.route("/")
def home():
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)