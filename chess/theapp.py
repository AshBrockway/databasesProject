from flask import Flask, render_template, request
import os


app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/violin')
def violin():
	return render_template('violin.html')

@app.route('/moves')
def moves():
        return render_template('moves.html')
@app.route('/movevtime')
def movevtime():
	return render_template('movevtime.html')
@app.route('/heat')
def heat():
	return render_template('heat.html')
if __name__ == "__main__":
    app.run()
