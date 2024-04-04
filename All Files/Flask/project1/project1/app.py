from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['GET','POST'])
def percentage():
    python  = float(request.form['python'])
    java    = float(request.form['java'])
    javascript = float(request.form['javascript'])
    typescript = float(request.form['typescript'])
    flask = float(request.form['flask'])
    
    percentage = (python+java+javascript+typescript+flask)/500*100
    
    return render_template('result.html', percentage=percentage)       
    


if __name__ == "__main__":
    app.run(debug=True, port=5000)