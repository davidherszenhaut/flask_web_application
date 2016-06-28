from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():

	return render_template("homepage.html")

@app.route("/about")

def about():

	return render_template("about.html")

@app.route("/resume")

def resume():

	return render_template("resume.html")

@app.route("/hobbies")

def hobbies():

	return render_template("hobbies.html")

@app.route("/contact")

def contact():

	return render_template("contact.html")

if __name__ == "__main__":
	app.run()