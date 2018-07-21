from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def base():
	return render_template("base.html", title= "This is my Home Page!")

@app.route("/contact")
def body():
	return render_template("body.html", title = "Pls Contact Me!")

@app.route("/about")
def about():
	return render_template("aboutMe.html", title = "This is About Me!")

@app.route("/backToHome", methods=['POST'])
def back():
	nameFirst = request.form['firstName']
	nameLast = request.form['lastName']
	personPassword = request.form['password']
	personEmail = request.form['email']
	personMessage = request.form['message']
	personGender = request.form['gender']
	personAge = request.form['age']
	personBirth = request.form['birthday']

	return render_template("information.html", title= "Submit", firstName=nameFirst, lastName=nameLast, password=personPassword, email = personEmail, message = personMessage, gender = personGender, age = personAge, birthday = personBirth)


if __name__ == "__main__":
	app.run(port= 4000, debug=True)		