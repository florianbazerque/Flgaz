from flask import Flask, request, render_template, redirect, url_for
#from flask_mysqldb import MySQL
import csv, yaml


app = Flask(__name__)

#Configuration base de données
#db = yaml.load(open('settings.yaml'))
#app.config['MYSQL_HOST'] = db['MYSQL_HOST']
#app.config['MYSQL_USER'] = db['MYSQL_USER']
#app.config['MYSQL_PASSWORD'] = db['MYSQL_PASSWORD']
#app.config['MYSQL_DB'] = db['MYSQL_DB']

#mysql = MySQL(app)

@app.route('/')
def home():
    try:
	    cur = mysql.connection.cursor()
    except:
	    print('oups')
    
    gaz = parse_from_csv()
    return render_template("home.html", gaz = gaz)

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		dump_to_csv(request.form)
		return redirect(url_for('timeline'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	for g in gaz:
		g = g[:75]
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
			gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)