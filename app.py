from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
    gaz = parse_from_csv()
    return render_template("home.html", gaz = gaz)

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		dump_to_csv(request.form)
		return redirect(url_for('home'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	return render_template("timeline.html", gaz = gaz)

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    response.access_control_allow_origin = '*'
    return response

def parse_from_csv():
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row[1]) < 280:
				gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	if len(d["user-text"]) < 280:
		donnees = [d["user-name"],d["user-text"] ]
		with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
			writer = csv.writer(f)
			writer.writerow(donnees)