from flask import Flask, render_template, request
import os

TEST_FOLDER = os.path.join('static', '')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = TEST_FOLDER
app.debug = True

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/violin')
def violin():
	return render_template('violin.html')

if __name__ == "__main__":
    app.run()
