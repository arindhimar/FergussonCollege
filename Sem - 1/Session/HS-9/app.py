from flask import Flask,render_template,redirect,request


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about12")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)