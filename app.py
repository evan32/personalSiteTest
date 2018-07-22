from flask import Flask, render_template, request
import random
import dataset

app = Flask(__name__)
db = dataset.connect("postgres://pvroautsocorjp:7ac4c1824b2cceca31291cea46afbd2e72b3a2a143aa53c7c2604a066e6f45df@ec2-23-23-247-222.compute-1.amazonaws.com:5432/d7g9pn5j4jvvru")

userTable = db['user']

userTable.insert(dict(name="Erik", age=20))
print(db.tables)
print(db['user'].columns)
print(list(db['user'].all()))



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
	personBirth = request.form['birthday']\
	
	print(db.tables)

	return render_template("information.html", title= "Submit", firstName=nameFirst, lastName=nameLast, password=personPassword, email = personEmail, message = personMessage, gender = personGender, age = personAge, birthday = personBirth)


if __name__ == "__main__":
	app.run(port= 4000, debug=True)		