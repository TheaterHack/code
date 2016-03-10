from flask import Flask 
from flask import render_template
from flask import request
from sendresult import email_result
from gifsender import gif
app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("htmlforpage.html")

@app.route("/signup", methods=['POST'])
def sign_up():
	print "yolo"
	form_data = request.form
	print form_data
	animal_gif =gif(form_data['animal'])
	email_result("uri", "shlee9817@gmail.com", "old vic", animal_gif)


	return "All ok"

app.run(
	debug=True
	)