from flask import Flask, render_template


# Initlaize Flask service
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CPS3500!"

@app.route("/new_page")
def new_page():
    return "This is a New Page!"

@app.route('/user/<username>')
def user(username):
    return render_template ("user.html", username=username)

@app.route("/lookup/<username>")
def lookup(username):
    return "Your ID is: " + str(username)

@app.route("/template")
def display():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


