from flask import Flask, render_template, request


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def percentage():
    
    python = float(request.form['python'])
    javascript = float(request.form['javascript'])
    react = float(request.form['react'])
    percentage = (python+javascript+react)/300*100
    
    return render_template('result.html', percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True, port=5000)