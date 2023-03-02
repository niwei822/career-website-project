from flask import Flask, render_template, jsonify
app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst I',
    'location': 'San Jose, CA',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst II',
    'location': 'Sunnyvale, CA',
    'salary': '$110,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst III',
    'location': 'San Jose, CA',
    'salary': '$120,000'
  },
  {
    'id': 4,
    'title': 'Data Analyst I',
    'location': 'Fremont, CA',
    'salary': '$130,000'
  }
]

@app.route("/")
def homepage():
  return render_template("home.html", jobs=jobs, company="HireMe")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)