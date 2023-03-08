from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Ikeja, Lagos',
  'salary': '#150,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Lekki, Lagos',
  'salary': '#200,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Festac, Lagos',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Wuse, Abuja',
  'salary': '#300,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Burger')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
