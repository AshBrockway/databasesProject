from flask import Flask, render_template, request
import os

TEST_FOLDER = os.path.join('static', 'plot_photos')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = TEST_FOLDER
app.debug = True

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/cool_form', methods=['GET','POST'])
def cool_form():
	if request.method == 'POST':
		return redirect(url_for('index'))
	return render_template('cool_form.html')

@app.route('/testPNG')
def showTestImage():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.png')
	return render_template("test1.html", user_image = full_filename)




if __name__ == "__main__":
    app.run()
