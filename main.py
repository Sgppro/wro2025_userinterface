from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder="./static")

@app.route("/")
def rootpage():
    return redirect("/detection.html")

@app.route("/detection.html")
def detectionPage():
    return render_template("detection.html")

@app.route("/astronaut.html")
def astronautPage():
    return render_template("astronaut.html")

@app.route("/docking.html")
def dockingPage():
    return render_template("docking.html")

@app.route("/port.html")
def portPage():
    return render_template("port.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500)
