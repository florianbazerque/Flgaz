"""
Principal module of the application, redirect to all road of the app
"""
import csv
from flask import Flask, request, render_template, redirect, url_for

APP = Flask(__name__)

@APP.route('/')
def home():
    """
    home : return home view
    Parameters
    ----------
    none
    Return
    -------
    html page
    """
    gaz = parse_from_csv()
    return render_template("home.html", gaz=gaz)

@APP.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """
    save_gazouille : return gazouille view
    Parameters
    ----------
    none
    Return
    -------
    html page
    """
    if request.method == 'POST':
        print(request.form)
        dump_to_csv(request.form)
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('gaz_t.html')
    return redirect(url_for('home'))

@APP.route('/timeline', methods=['GET'])
def timeline():
    """
    timeline : return timeline view
    Parameters
    ----------
    none
    Return
    -------
    html page
    """
    gaz = parse_from_csv()
    return render_template("timeline_t.html", gaz=gaz)

@APP.route('/timeline/<user_name>/', methods=['GET'])
def timeline_user(user_name):
    """
    timeline_user : return timeline for user
    Parameters
    ----------
    string user_name
    Return
    -------
    html page
    """
    user = str(user_name)
    gaz_list = parse_from_csv()
    user_gaz = []
    nb_gaz = 0
    for gaz in gaz_list:
        if user == gaz['user']:
            user_gaz.append(gaz)
            nb_gaz += 1
    return render_template("timeline_t.html", gaz=user_gaz) if nb_gaz else redirect(url_for('home'))


@APP.after_request
def add_header(response):
    """
    add_header : return response
    Parameters
    ----------
    reponse
    Return
    -------
    response_header cache_control and access_control_allow_origin
    """
    response.cache_control.max_age = 300
    response.access_control_allow_origin = '*'
    return response

def parse_from_csv():
    """
    parse_from_csv : return list of all gaz
    Parameters
    ----------
    none
    Return
    -------
    return list
    """
    gaz = []
    with open('./gazouilles.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row[0]) < 20 and len(row[1]) < 280 and len(row[0]) > 0 and len(row[1]) > 0:
                gaz.append({"user":row[0], "text":row[1]})
    return gaz

def dump_to_csv(data):
    """
    dump_to_csv : take data from save_gazouille and put it in csv
    Parameters
    ----------
    dict d
    Return
    -------
    none
    """
    if len(data["user-text"]) < 280:
        donnees = [data["user-name"], data["user-text"]]
        with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(donnees)
