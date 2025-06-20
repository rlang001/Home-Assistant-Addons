#!/usr/bin/python3.13
#
from flask import Flask, render_template, request, redirect, make_response
from configobj import ConfigObj

import time
from pathlib import Path

# my routes
from routes import reports
from routes import config_main
from routes import config_restful
from routes import config_reports
from routes import config_stations
from routes import maintenance

# my utilities
from utils import utilities

app = Flask(__name__)

# Register the routes
app.register_blueprint(reports.bp)
app.register_blueprint(config_main.bp)
app.register_blueprint(config_restful.bp)
app.register_blueprint(config_reports.bp)
app.register_blueprint(config_stations.bp)
app.register_blueprint(maintenance.bp)

@app.route('/')
def index():
    reports = utilities.getReports()
    return render_template('index.html', **reports)

@app.route('/about')
def about():
    
    reports = utilities.getReports()
    return render_template('about.html', **reports)

@app.route('/configuration/home')
def home():
    
    cookie_value = request.cookies.get('defaultreport')

    mypage = "/" + cookie_value + "/index.html"
    # Set the preferred skin
    return redirect(mypage)


############################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
