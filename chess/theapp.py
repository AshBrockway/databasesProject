from flask import Flask, render_template, request
import os

TEST_FOLDER = os.path.join('static', 'plot_photos')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = TEST_FOLDER
app.debug = True

@app.route('/', methods=['GET'])
def Home():
	return """<h1> You're Home!  Placeholder for a site index later </h1>"""    
@app.route('/testPNG')
def showTestImage():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.png')
	return render_template("test1.html", user_image = full_filename)




if __name__ == "__main__":
    app.run()
