# routes/reports.py

from flask import Flask, render_template, request

from flask import Blueprint

# my utilities
from utils import utilities


bp = Blueprint('reports', __name__)

@bp.route('/amphibian')
def amphibian():
    response = make_response(render_template('reports/belamphibianchertown/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.    
    return response

@bp.route('/belchertown')
def belchertown():
    response = make_response(render_template('reports/belchertown/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/neowxmaterial')
def neowxmaterial():
    response = make_response(render_template('reports/neowxmaterial/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response    

@bp.route('/jas')
def jas():
    response = make_response(render_template('reports/jas/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/nws')
def nws():
    response = make_response(render_template('reports/nws/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/mobile')
def mobile():
    response = make_response(render_template('reports/mobile/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/seasons')
def seasons():
    response = make_response(render_template('reports/seasons/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/simple')
def simple():
    response = make_response(render_template('reports/simple/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/smartphone')
def smartphone():
    response = make_response(render_template('reports/smartphone/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/ss')
def ss():
    response = make_response(render_template('reports/ss/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response

@bp.route('/wdc')
def wdc():

    response = make_response(render_template('reports/wdc/index.html'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    rsponse.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response