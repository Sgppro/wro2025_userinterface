from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder="./static")

@app.route("/")
def rootpage():
    return redirect("/main.html")

@app.route("/main.html")
def mainPage():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500)