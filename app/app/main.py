from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from HIDE's new solution"

@app.route("/menu/")
def menu():
    return render_template('menu.html')

@app.route("/SurveyLandingPage/")
def surveyLandingPage():
    return render_template('SurveyLandingPage.html')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
    #app.run(host='127.0.0.1', debug=True, port=7697)
