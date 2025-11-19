from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mice')
def mice():
    return render_template('mice.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/personal_loan')
def personal_loan():
    return render_template('personal_loan.html')

@app.route('/business_loan')
def business_loan():
    return render_template('business_loan.html')

@app.route('/home_loan')
def home_loan():
    return render_template('home_loan.html')

@app.route('/machine_loan')
def machine_loan():
    return render_template('machine_loan.html')

if __name__ == '__main__':
    app.run(debug=True)
