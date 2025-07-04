from flask import Flask, render_template, redirect, request

app = Flask(__name__, static_folder="./static")

@app.route("/")
def rootpage():
    return redirect("/detection.html")

@app.route("/detection.html")
def detectionPage():
    hostname = request.headers.get('Host').split(':')[0]
    return render_template("detection.html", hostname=hostname)

@app.route("/astronaut.html")
def astronautPage():
    hostname = request.headers.get('Host').split(':')[0]
    return render_template("astronaut.html", hostname=hostname)

@app.route("/docking.html")
def dockingPage():
    hostname = request.headers.get('Host').split(':')[0]
    return render_template("docking.html", hostname=hostname)

@app.route("/port.html")
def portPage():
    hostname = request.headers.get('Host').split(':')[0]
    return render_template("port.html", hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500)
