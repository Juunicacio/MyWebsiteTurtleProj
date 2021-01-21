from flask import Flask, render_template
# adding Dash, to see it with flask, see the folder:...

app = Flask(__name__)

@app.route('/')
def index():
	# create a variable for the title
	title = "homepage"
	# pull in index.html page
	return render_template("index.html", title=title)

# The Flask Application Factory refers to a common "pattern":
# https://hackersandslackers.com/flask-application-factory/


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)