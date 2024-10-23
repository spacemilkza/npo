from flask import Flask, render_template, request #import the Flask class

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/") #we create an instance of the class

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/donate")
def donate():
    return render_template("donate.html") 

@app.route("/join")
def join():
    return render_template("/join.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.get("/signin")
def signin():
    return render_template("signin.html")

@app.route("/admin", methods=["GET", "POST"]) #we tie the response function a url
def admin():
    if request.method == "GET":
        return render_template("signin.html", data=data)
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return render_template("admin.html")