#!/usr/bin/python3.13
#
from flask import Flask, render_template, request, redirect, make_response
from configobj import ConfigObj
import shutil
import subprocess as sp
import time
from pathlib import Path

app = Flask(__name__)

def getReports():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    
    e_amphibian = config['StdReport']['amphibian']['enable']
    try:
        n_amphibian = config['StdReport']['amphibian']['new_window']
    except: 
        n_amphibian = "false"

    e_belchertown = config['StdReport']['Belchertown']['enable']
    try:
        n_belchertown = config['StdReport']['Belchertown']['new_window']
    except: 
        n_belchertown = "false"

    e_jas = config['StdReport']['jas']['enable']
    try:
        n_jas = config['StdReport']['jas']['new_window']
    except: 
        n_jas = "false"

    e_neowxmaterial = config['StdReport']['NeoWX-Material']['enable']
    try:
        n_neowxmaterial = config['StdReport']['NeoWX-Material']['new_window']
    except: 
        n_neowxmaterial = "false"

    e_nws = config['StdReport']['NWSReport']['enable']
    try:
        n_nws = config['StdReport']['NWSReport']['new_window']
    except: 
        n_nws = "false"

    e_seasons = config['StdReport']['SeasonsReport']['enable']
    try:
        n_seasons = config['StdReport']['SeasonsReport']['new_window']
    except: 
        n_seasons = "false"

    e_simple = config['StdReport']['simple']['enable']
    try:
        n_simple = config['StdReport']['simple']['new_window']
    except: 
        n_simple = "false"

    e_smartphone = config['StdReport']['SmartphoneReport']['enable']
    try:
        n_smartphone = config['StdReport']['SmartphoneReport']['new_window']
    except: 
        n_smartphone = "false"

    e_ss = config['StdReport']['SteelSeries']['enable']
    try:
        n_ss = config['StdReport']['SteelSeries']['new_window']
    except: 
        n_ss = "false"
    
    e_wdc = config['StdReport']['WdcReport']['enable']
    try:
        n_wdc = config['StdReport']['WdcReport']['new_window']
    except: 
        n_wdc = "false"


    reports = dict(e_amphibian = e_amphibian, n_amphibian = n_amphibian,
                e_belchertown = e_belchertown, n_belchertown = n_belchertown,
                e_jas = e_jas, n_jas = n_jas,
                e_neowxmaterial = e_neowxmaterial, n_neowxmaterial = n_neowxmaterial,
                e_nws = e_nws, n_nws = n_nws,
                e_seasons = e_seasons, n_seasons = n_seasons,
                e_simple = e_simple, n_simple = n_simple,
                e_smartphone = e_smartphone, n_smartphone = n_smartphone,
                e_ss = e_ss, n_ss = n_ss,
                e_wdc = e_wdc, n_wdc = n_wdc)

    return reports

@app.route('/')
def index():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    
    e_amphibian = config['StdReport']['amphibian']['enable']
    try:
        n_amphibian = config['StdReport']['amphibian']['new_window']
    except: 
        n_amphibian = "false"

    e_belchertown = config['StdReport']['Belchertown']['enable']
    try:
        n_belchertown = config['StdReport']['Belchertown']['new_window']
    except: 
        n_belchertown = "false"

    e_jas = config['StdReport']['jas']['enable']
    try:
        n_jas = config['StdReport']['jas']['new_window']
    except: 
        n_jas = "false"

    e_neowxmaterial = config['StdReport']['NeoWX-Material']['enable']
    try:
        n_neowxmaterial = config['StdReport']['NeoWX-Material']['new_window']
    except: 
        n_neowxmaterial = "false"

    e_nws = config['StdReport']['NWSReport']['enable']
    try:
        n_nws = config['StdReport']['NWSReport']['new_window']
    except: 
        n_nws = "false"

    e_seasons = config['StdReport']['SeasonsReport']['enable']
    try:
        n_seasons = config['StdReport']['SeasonsReport']['new_window']
    except: 
        n_seasons = "false"

    e_simple = config['StdReport']['simple']['enable']
    try:
        n_simple = config['StdReport']['simple']['new_window']
    except: 
        n_simple = "false"

    e_smartphone = config['StdReport']['SmartphoneReport']['enable']
    try:
        n_smartphone = config['StdReport']['SmartphoneReport']['new_window']
    except: 
        n_smartphone = "false"

    e_ss = config['StdReport']['SteelSeries']['enable']
    try:
        n_ss = config['StdReport']['SteelSeries']['new_window']
    except: 
        n_ss = "false"
    
    e_wdc = config['StdReport']['WdcReport']['enable']
    try:
        n_wdc = config['StdReport']['WdcReport']['new_window']
    except: 
        n_wdc = "false"


    reports = dict(e_amphibian = e_amphibian, n_amphibian = n_amphibian,
                e_belchertown = e_belchertown, n_belchertown = n_belchertown,
                e_jas = e_jas, n_jas = n_jas,
                e_neowxmaterial = e_neowxmaterial, n_neowxmaterial = n_neowxmaterial,
                e_nws = e_nws, n_nws = n_nws,
                e_seasons = e_seasons, n_seasons = n_seasons,
                e_simple = e_simple, n_simple = n_simple,
                e_smartphone = e_smartphone, n_smartphone = n_smartphone,
                e_ss = e_ss, n_ss = n_ss,
                e_wdc = e_wdc, n_wdc = n_wdc)

    return render_template('index.html', **reports)

@app.route('/about')
def about():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    
    e_amphibian = config['StdReport']['amphibian']['enable']
    try:
        n_amphibian = config['StdReport']['amphibian']['new_window']
    except: 
        n_amphibian = "false"

    e_belchertown = config['StdReport']['Belchertown']['enable']
    try:
        n_belchertown = config['StdReport']['Belchertown']['new_window']
    except: 
        n_belchertown = "false"

    e_jas = config['StdReport']['jas']['enable']
    try:
        n_jas = config['StdReport']['jas']['new_window']
    except: 
        n_jas = "false"

    e_neowxmaterial = config['StdReport']['NeoWX-Material']['enable']
    try:
        n_neowxmaterial = config['StdReport']['NeoWX-Material']['new_window']
    except: 
        n_neowxmaterial = "false"

    e_nws = config['StdReport']['NWSReport']['enable']
    try:
        n_nws = config['StdReport']['NWSReport']['new_window']
    except: 
        n_nws = "false"

    e_seasons = config['StdReport']['SeasonsReport']['enable']
    try:
        n_seasons = config['StdReport']['SeasonsReport']['new_window']
    except: 
        n_seasons = "false"

    e_simple = config['StdReport']['simple']['enable']
    try:
        n_simple = config['StdReport']['simple']['new_window']
    except: 
        n_simple = "false"

    e_smartphone = config['StdReport']['SmartphoneReport']['enable']
    try:
        n_smartphone = config['StdReport']['SmartphoneReport']['new_window']
    except: 
        n_smartphone = "false"

    e_ss = config['StdReport']['SteelSeries']['enable']
    try:
        n_ss = config['StdReport']['SteelSeries']['new_window']
    except: 
        n_ss = "false"
    
    e_wdc = config['StdReport']['WdcReport']['enable']
    try:
        n_wdc = config['StdReport']['WdcReport']['new_window']
    except: 
        n_wdc = "false"


    reports = dict(e_amphibian = e_amphibian, n_amphibian = n_amphibian,
                e_belchertown = e_belchertown, n_belchertown = n_belchertown,
                e_jas = e_jas, n_jas = n_jas,
                e_neowxmaterial = e_neowxmaterial, n_neowxmaterial = n_neowxmaterial,
                e_nws = e_nws, n_nws = n_nws,
                e_seasons = e_seasons, n_seasons = n_seasons,
                e_simple = e_simple, n_simple = n_simple,
                e_smartphone = e_smartphone, n_smartphone = n_smartphone,
                e_ss = e_ss, n_ss = n_ss,
                e_wdc = e_wdc, n_wdc = n_wdc)

    return render_template('about.html', **reports)

@app.route('/configuration/nav')
def nav():

    return render_template('nav.html')

@app.route('/amphibian')
def amphibian():
    return render_template('/reports/amphibian/index.html')
    

@app.route('/belchertown')
def belchertown():
    return render_template('/reports/belchertown/index.html')

@app.route('/neowxmaterial')
def neowxmaterial():
    return render_template('/reports/neowxmaterial/index.html')

@app.route('/jas')
def jas():
    return render_template('reports/jas/index.html')


@app.route('/nws')
def nws():
    return render_template('reports/nws/index.html')

@app.route('/mobile')
def mobile():
    return render_template('reports/mobile/index.html')

@app.route('/seasons')
def seasons():
    return render_template('reports/seasons/index.html')

@app.route('/simple')
def simple():
    return render_template('reports/simple/index.html')

@app.route('/ss')
def ss():
    return render_template('reports/ss/index.html')

@app.route('/wdc')
def wdc():
    return render_template('reports/wdc/index.html')

@app.route('/smartphone')
def smartphone():
    return render_template('reports/smartphone/index.html')



@app.route('/configuration/home')
def home():
    
    cookie_value = request.cookies.get('defaultreport')

    mypage = "/" + cookie_value + "/index.html"
    # Set the preferred skin
    return redirect(mypage)

#############################################################
# Configuation
#############################################################
# Overall Section
@app.route('/configuration/c_overall', methods=['POST','GET'])
def c_overall():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    e_amphibian = config['StdReport']['amphibian']['enable']
    try:
        n_amphibian = config['StdReport']['amphibian']['new_window']
    except: 
        n_amphibian = "false"

    e_belchertown = config['StdReport']['Belchertown']['enable']
    try:
        n_belchertown = config['StdReport']['Belchertown']['new_window']
    except: 
        n_belchertown = "false"

    e_jas = config['StdReport']['jas']['enable']
    try:
        n_jas = config['StdReport']['jas']['new_window']
    except: 
        n_jas = "false"

    e_neowxmaterial = config['StdReport']['NeoWX-Material']['enable']
    try:
        n_neowxmaterial = config['StdReport']['NeoWX-Material']['new_window']
    except: 
        n_neowxmaterial = "false"

    e_nws = config['StdReport']['NWSReport']['enable']
    try:
        n_nws = config['StdReport']['NWSReport']['new_window']
    except: 
        n_nws = "false"

    e_seasons = config['StdReport']['SeasonsReport']['enable']
    try:
        n_seasons = config['StdReport']['SeasonsReport']['new_window']
    except: 
        n_seasons = "false"

    e_simple = config['StdReport']['simple']['enable']
    try:
        n_simple = config['StdReport']['simple']['new_window']
    except: 
        n_simple = "false"

    e_smartphone = config['StdReport']['SmartphoneReport']['enable']
    try:
        n_smartphone = config['StdReport']['SmartphoneReport']['new_window']
    except: 
        n_smartphone = "false"

    e_ss = config['StdReport']['SteelSeries']['enable']
    try:
        n_ss = config['StdReport']['SteelSeries']['new_window']
    except: 
        n_ss = "false"
    
    e_wdc = config['StdReport']['WdcReport']['enable']
    try:
        n_wdc = config['StdReport']['WdcReport']['new_window']
    except: 
        n_wdc = "false"


    if request.method == 'POST':
        config['debug'] = request.form.get('debug')
        config['log_success'] = request.form.get('log_success')
        config['log_failure'] = request.form.get('log_failure')

        config.write()

    myoverall = dict(version = config['version'], 
                    debug = config['debug'], 
                    log_success = config['log_success'].lower(), 
                    log_failure = config['log_failure'].lower(),
                    e_amphibian = e_amphibian, n_amphibian = n_amphibian,
                    e_belchertown = e_belchertown, n_belchertown = n_belchertown,
                    e_jas = e_jas, n_jas = n_jas,
                    e_neowxmaterial = e_neowxmaterial, n_neowxmaterial = n_neowxmaterial,
                    e_nws = e_nws, n_nws = n_nws,
                    e_seasons = e_seasons, n_seasons = n_seasons,
                    e_simple = e_simple, n_simple = n_simple,
                    e_smartphone = e_smartphone, n_smartphone = n_smartphone,
                    e_ss = e_ss, n_ss = n_ss,
                    e_wdc = e_wdc, n_wdc = n_wdc
                    )
    return render_template('menu/config/overall.html', **myoverall)

# Station Section
@app.route('/configuration/c_station', methods=['POST','GET'])
def c_station():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    if request.method == 'POST':

        config['Station']['location'] = request.form.get('location')
        config['Station']['latitude'] = request.form.get('latitude')
        config['Station']['longitude'] = request.form.get('longitude')
        config['Station']['altitude'] = request.form.get('altitude')
        config['Station']['station_type'] = request.form.get('station_type')
        config['Station']['rain_year_start'] = request.form.get('rain_year_start')
        config['Station']['week_start'] = request.form.get('week_start')

        config.write()

    mystation = dict(config['Station'])
    return render_template('menu/config/station.html', **mystation)

# Logging Section
@app.route('/configuration/c_logging', methods=['POST','GET'])
def c_logging():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    service = "weewx.engine.StdPrint"
    reportservices = config['Engine']['Services']['report_services']
    if service in reportservices:
        stdprint = "true"
    else:
        stdprint = "false"

    if request.method == 'POST':
        config['Logging']['handlers']['rotate']['level'] = request.form.get('level')
        config['Logging']['handlers']['rotate']['formatter'] = request.form.get('formatter')
        config['Logging']['handlers']['rotate']['maxBytes'] = request.form.get('maxBytes')
        config['Logging']['handlers']['rotate']['backupCount'] = request.form.get('backupCount')
        stdprint = request.form.get('stdprint')

        if (stdprint == "true") and (service not in reportservices):
            # Add it
            config['Engine']['Services']['report_services'] = config['Engine']['Services']['report_services'] + ", " + service

        elif (stdprint == "false") and (service in reportservices):
            # Remove it
            s = reportservices.replace(service, "").strip().strip(",")
            config['Engine']['Services']['report_services'] = s

        config.write()

    
    mylogging = dict(config['Logging']['handlers']['rotate'])

    return render_template('menu/config/logging.html', **mylogging, stdprint = stdprint)

# DerivedValues Section
@app.route('/configuration/c_derivedvalues', methods=['POST','GET'])
def c_derivedvalues():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdWXCalculate']['Calculations']['pressure'] = request.form.get('pressure')
        config['StdWXCalculate']['Calculations']['altimeter'] = request.form.get('altimeter')
        config['StdWXCalculate']['Calculations']['appTemp'] = request.form.get('appTemp')
        config['StdWXCalculate']['Calculations']['barometer'] = request.form.get('barometer')

        config['StdWXCalculate']['Calculations']['cloudbase'] = request.form.get('cloudbase')
        config['StdWXCalculate']['Calculations']['dewpoint'] = request.form.get('dewpoint')
        config['StdWXCalculate']['Calculations']['ET'] = request.form.get('ET')
        config['StdWXCalculate']['Calculations']['heatindex'] = request.form.get('heatindex')

        config['StdWXCalculate']['Calculations']['humidex'] = request.form.get('humidex')
        config['StdWXCalculate']['Calculations']['inDewpoint'] = request.form.get('inDewpoint')
        config['StdWXCalculate']['Calculations']['maxSolarRad'] = request.form.get('maxSolarRad')
        config['StdWXCalculate']['Calculations']['rainRate'] = request.form.get('rainRate')

        config['StdWXCalculate']['Calculations']['windchill'] = request.form.get('windchill')
        config['StdWXCalculate']['Calculations']['windrun'] = request.form.get('windrun')

        config.write()

    myderivedvalues = dict(config['StdWXCalculate']['Calculations'])
    return render_template('menu/config/derivedvalues.html', **myderivedvalues)

# MQTTSubscribeService
@app.route('/configuration/c_mqttsubscribeservice', methods=['POST','GET'])
def c_mqttsubscribeservice():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    if request.method == 'POST':
        config['MQTTSubscribeService']['enable'] = request.form.get('enable')
        config['MQTTSubscribeService']['host'] = request.form.get('host')
        config['MQTTSubscribeService']['port'] = request.form.get('port')
        config['MQTTSubscribeService']['keepalive'] = request.form.get('keepalive')
        config['MQTTSubscribeService']['username'] = request.form.get('username')
        config['MQTTSubscribeService']['password'] = request.form.get('password')
        config['MQTTSubscribeService']['binding'] = request.form.get('binding')

        # Does user.MQTTSubscribe.MQTTSubscribeService exist in data_services?
        # service = "user.MQTTSubscribe.MQTTSubscribeService"
        # data_services = config['Engine']['Services']['data_services']
        
        # if (config['MQTTSubscribeService']['enable'] == "true") and (mqttsubscribeservice not in data_services):
            # config['Engine']['Services']['data_services'] = config['Engine']['Services']['data_services'] + ", " + service

        # elif (config['MQTTSubscribeService']['enable']  == "false") and (mqttsubscribeservice in data_services):
            # s = data_services.replace(service, "").strip().strip(",")
            # config['Engine']['Services']['data_services'] = s

        config.write()

    mymqttsubscribeservice = dict(config['MQTTSubscribeService'])
    return render_template('menu/config/mqttsubscribeservice.html', **mymqttsubscribeservice)

# NWS
@app.route('/configuration/c_nws', methods=['POST','GET'])
def c_nws():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # Does user.nws.NWS exiset in the data_services?
    nws = "user.nws.NWS"
    services = config['Engine']['Services']['data_services']
    if nws in services:
        config['NWS']['enable'] = "true"
    else:
        config['NWS']['enable'] = "false"

    if request.method == 'POST':
        # Station registry
        nws_enable  = request.form.get('enable')
        config['NWS']['enable'] = nws_enable

        # config['NWS']['data_binding'] = request.form.get('data_binding')

        config['NWS']['days_to_keep'] = request.form.get('days_to_keep')
        config['NWS']['poll_secs'] = request.form.get('poll_secs')
        config['NWS']['alert_poll_secs'] = request.form.get('alert_poll_secs')
        config['NWS']['retry_wait_secs'] = request.form.get('retry_wait_secs')
        config['NWS']['alert_retry_wait_secs'] = request.form.get('alert_retry_wait_secs')
        config['NWS']['timeout_secs'] = request.form.get('timeout_secs')
        config['NWS']['User-Agent'] = '"' + request.form.get('user_agent') + '"'

        if nws_enable == 'true':
            # Add the service
            if  nws.lower() not in services.lower():
                config['Engine']['Services']['data_services'] = services +", " + nws
        else:
            # Remove the service
            new_services = services.replace(nws, "")
            s1= new_services.rstrip(", ")
            config['Engine']['Services']['data_services'] = s1

        # Remove ['NWS']['enable'] from the dictionary so as not to write it to the config file
        del config['NWS']['enable']
        config.write()

    config['NWS']['user_agent'] = config['NWS']['User-Agent'].strip('"')

    mynws = dict(config['NWS'])
    # nws_enable  = request.form.get('enable')
    return render_template('menu/config/nws.html', **mynws)

############################################################

# Restful/stationregistry
@app.route('/configuration/c_stationregistry', methods=['POST','GET'])
def c_stationregistry():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        # Station registry
        config['StdRESTful']['StationRegistry']['register_this_station'] = request.form.get('register_this_station')

        config.write()

    mystationregistry = dict(register_this_station = config['StdRESTful']['StationRegistry']['register_this_station'].lower())

    return render_template('menu/config/restful/stationregistry.html', **mystationregistry)

# Restful/AWEKAS
@app.route('/configuration/c_awekas', methods=['POST','GET'])
def c_awekas():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['AWEKAS']['enable'] = request.form.get('enable')
        config['StdRESTful']['AWEKAS']['username'] = request.form.get('username')
        config['StdRESTful']['AWEKAS']['password'] = '"' + request.form.get('password') + '"'

        config.write()


    myawekas = dict(enable = config['StdRESTful']['AWEKAS']['enable'].lower(), 
                    username = config['StdRESTful']['AWEKAS']['username'], 
                    password = config['StdRESTful']['AWEKAS']['password'])

    return render_template('menu/config/restful/awekas.html', **myawekas)

# Restful/CWOP
@app.route('/configuration/c_cwop', methods=['POST','GET'])
def c_cwop():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['CWOP']['enable'] = request.form.get('enable')
        config['StdRESTful']['CWOP']['station'] = request.form.get('station')
        config['StdRESTful']['CWOP']['passcode'] = request.form.get('passcode')

        config.write()

    mycwop = dict(enable = config['StdRESTful']['CWOP']['enable'].lower(), 
                    station = config['StdRESTful']['CWOP']['station'], 
                    passcode = config['StdRESTful']['CWOP']['passcode'])

    return render_template('menu/config/restful/cwop.html', **mycwop)

# Restful/PWSWeather
@app.route('/configuration/c_pwsweather', methods=['POST','GET'])
def c_pwsweather():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['PWSweather']['enable'] = request.form.get('enable')
        config['StdRESTful']['PWSweather']['station'] = request.form.get('station')
        config['StdRESTful']['PWSweather']['password'] = '"' + request.form.get('password') + '"'

        config.write()

    mypwsweather = dict(enable = config['StdRESTful']['PWSweather']['enable'].lower(),
                        station = config['StdRESTful']['PWSweather']['station'],
                        password = config['StdRESTful']['PWSweather']['password'])

    return render_template('menu/config/restful/pwsweather.html', **mypwsweather)

# Restful/WOW
@app.route('/configuration/c_wow', methods=['POST','GET'])
def c_wow():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['WOW']['enable'] = request.form.get('enable')
        config['StdRESTful']['WOW']['station'] = request.form.get('station')
        config['StdRESTful']['WOW']['password'] = '"' + request.form.get('password') + '"'

        config.write()

    mywow =  dict(enable = config['StdRESTful']['WOW']['enable'].lower(),
                station = config['StdRESTful']['WOW']['station'],
                password = config['StdRESTful']['WOW']['password'])

    return render_template('menu/config/restful/wow.html', **mywow)

# Restful/Wunderground
@app.route('/configuration/c_wunderground', methods=['POST','GET'])
def c_wunderground():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['Wunderground']['enable'] = request.form.get('enable')
        config['StdRESTful']['Wunderground']['station'] = request.form.get('station')
        config['StdRESTful']['Wunderground']['password'] = request.form.get('password')
        config['StdRESTful']['Wunderground']['rapidfire'] = request.form.get('rapidfire')
        config.write()

    mywunderground = dict(enable = config['StdRESTful']['Wunderground']['enable'].lower(),
                        station = config['StdRESTful']['Wunderground']['station'],
                        password = config['StdRESTful']['Wunderground']['password'],
                        rapidfire = config['StdRESTful']['Wunderground']['rapidfire'].lower())

    return render_template('menu/config/restful/wunderground.html', **mywunderground)

# Restful/MQTT
@app.route('/configuration/c_mqtt', methods=['POST','GET'])
def c_mqtt():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdRESTful']['MQTT']['enable'] = request.form.get('enable')
        config['StdRESTful']['MQTT']['server_url'] = request.form.get('server_url')
        config['StdRESTful']['MQTT']['topic'] = request.form.get('topic')
        config['StdRESTful']['MQTT']['binding'] = request.form.get('binding')
        config['StdRESTful']['MQTT']['unit_system'] = request.form.get('unit_system')
        config['StdRESTful']['MQTT']['aggregation'] = request.form.get('aggregation')
        # config['StdRESTful']['MQTT']['ha_discovery'] = request.form.get('ha_discovery')
        # config['StdRESTful']['MQTT']['ha_device_name'] = request.form.get('ha_device_name')
        # config['StdRESTful']['MQTT']['ha_discovery_topic'] = request.form.get('ha_discovery_topic')

        config.write()

    mymqtt = dict(enable =config['StdRESTful']['MQTT']['enable'].lower(),
                server_url = config['StdRESTful']['MQTT']['server_url'],
                topic = config['StdRESTful']['MQTT']['topic'], 
                binding = config['StdRESTful']['MQTT']['binding'].lower(),
                unit_system = config['StdRESTful']['MQTT']['unit_system'],
                aggregation = config['StdRESTful']['MQTT']['aggregation'].lower())

    return render_template('menu/config/restful/mqtt.html', **mymqtt)

############################################################
# Reports Section
@app.route('/configuration/c_stdreports', methods=['POST','GET'])
def c_stdreports():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    #defaultreport = "seasons"

    e_amphibian = config['StdReport']['amphibian']['enable']

    try:
        n_amphibian = config['StdReport']['amphibian']['new_window']
    except: 
        n_amphibian = "false"

    e_belchertown = config['StdReport']['Belchertown']['enable']
    try:
        n_belchertown = config['StdReport']['Belchertown']['new_window']
    except:
        n_belchertown = "false"

    e_jas = config['StdReport']['jas']['enable']
    try:
        n_jas = config['StdReport']['jas']['new_window']
    except:
        n_jas = "false"

    e_neowxmaterial = config['StdReport']['NeoWX-Material']['enable']
    try:
        n_neowxmaterial = config['StdReport']['NeoWX-Material']['new_window']
    except:
        n_neowxmaterial = "false"

    e_nws = config['StdReport']['NWSReport']['enable']
    try:
        n_nws = config['StdReport']['NWSReport']['new_window']
    except:
        n_nws = "false"

    e_seasons = config['StdReport']['SeasonsReport']['enable']
    try:
        n_seasons = config['StdReport']['SeasonsReport']['new_window']
    except:
        n_seasons = "false"

    e_simple = config['StdReport']['simple']['enable']
    try:
        n_simple = config['StdReport']['simple']['new_window']
    except:
        n_simple = "false"

    e_smartphone = config['StdReport']['SmartphoneReport']['enable']
    try:
        n_smartphone = config['StdReport']['SmartphoneReport']['new_window']
    except:
        n_smartphone = "false"

    e_ss = config['StdReport']['SteelSeries']['enable']
    try:
        n_ss = config['StdReport']['SteelSeries']['new_window']
    except:
        n_ss = "false"
    
    e_wdc = config['StdReport']['WdcReport']['enable']
    try:
        n_wdc = config['StdReport']['WdcReport']['new_window']
    except:
        n_wdc = "false"


    if request.method == 'POST':
        #defaultreport =  request.form.get('defaultreport')
        config['StdReport']['amphibian']['enable'] = request.form.get('e_amphibian')
        config['StdReport']['amphibian']['new_window'] = request.form.get('n_amphibian')
        
        config['StdReport']['Belchertown']['enable'] = request.form.get('e_belchertown')
        config['StdReport']['Belchertown']['new_window'] = request.form.get('n_belchertown')

        config['StdReport']['jas']['enable'] = request.form.get('e_jas')
        config['StdReport']['jas']['new_window'] = request.form.get('n_jas')
        
        config['StdReport']['NeoWX-Material']['enable'] = request.form.get('e_neowxmaterial')
        config['StdReport']['NeoWX-Material']['new_window'] = request.form.get('n_neowxmaterial')

        config['StdReport']['NWSReport']['enable'] = request.form.get('e_nws')
        config['StdReport']['NWSReport']['new_window'] = request.form.get('n_nws')
                
        config['StdReport']['SeasonsReport']['enable'] = request.form.get('e_seasons')
        config['StdReport']['SeasonsReport']['new_window'] = request.form.get('n_seasons')

        config['StdReport']['simple']['enable'] = request.form.get('e_simple')
        config['StdReport']['simple']['new_window'] = request.form.get('n_simple')

        config['StdReport']['SmartphoneReport']['enable'] = request.form.get('e_smartphone')
        config['StdReport']['SmartphoneReport']['new_window'] = request.form.get('n_smartphone')

        config['StdReport']['SteelSeries']['enable'] = request.form.get('e_ss')
        config['StdReport']['SteelSeries']['new_window'] = request.form.get('n_ss')

        config['StdReport']['WdcReport']['enable'] = request.form.get('e_wdc')
        config['StdReport']['WdcReport']['new_window'] = request.form.get('n_wdc')

        config.write()


    myreports = dict(e_amphibian = e_amphibian, n_amphibian = n_amphibian,
                    e_belchertown = e_belchertown, n_belchertown = n_belchertown, 
                    e_jas = e_jas, n_jas = n_jas, 
                    e_neowxmaterial = e_neowxmaterial, n_neowxmaterial = n_neowxmaterial, 
                    e_nws = e_nws, n_nws = n_nws, 
                    e_seasons = e_seasons, n_seasons = n_seasons, 
                    e_simple = e_simple, n_simple = n_simple, 
                    e_ss = e_ss, n_ss = n_ss, 
                    e_smartphone = e_smartphone, n_smartphone = n_smartphone, 
                    e_wdc = e_wdc, n_wdc = n_wdc
                    )

    return render_template('menu/config/reports/stdreports.html', **myreports)

# Reports/ftp Section
@app.route('/configuration/c_ftp', methods=['POST','GET'])
def c_ftp():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        
        config['StdReport']['FTP']['enable'] = request.form.get('enable')
        config['StdReport']['FTP']['user'] = request.form.get('user')
        config['StdReport']['FTP']['password'] = request.form.get('password')
        config['StdReport']['FTP']['server'] = request.form.get('server')
        config['StdReport']['FTP']['path'] = request.form.get('path')
        config['StdReport']['FTP']['secure_ftp'] = request.form.get('secure_ftp')
        config['StdReport']['FTP']['port'] = request.form.get('port')
        config['StdReport']['FTP']['passive'] = request.form.get('passive')

        config.write()

    myftp = dict((config['StdReport']['FTP']))
    return render_template('menu/config/reports/ftp.html', **myftp)

############################################################
# reports/Rsync Section
@app.route('/configuration/c_rsync', methods=['POST','GET'])
def c_rsync():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        config['StdReport']['RSYNC']['enable'] = request.form.get('enable')
        config['StdReport']['RSYNC']['server'] = request.form.get('server')
        config['StdReport']['RSYNC']['user'] = request.form.get('user')
        config['StdReport']['RSYNC']['path'] = request.form.get('path')
        config['StdReport']['RSYNC']['delete'] = request.form.get('delete')

        config.write()


    myrsync = dict((config['StdReport']['RSYNC']))


    return render_template('menu/config/reports/rsync.html', **myrsync)



############################################################
# Maintenance Section
# Service Section
@app.route('/configuration/m_service', methods=['POST','GET'])
def m_service():

    status = "false"
    getpidcmd = "pgrep -i weewxd"
    ret = sp.run(getpidcmd, capture_output=True, text=True, shell=True, executable='/bin/bash')
    weewx_pid = ret.stdout.rstrip()

    if weewx_pid:
        status = "true"

    start_cmd = "source ~/weewx-venv/bin/activate; weewxd --config=/config/weewx.conf &"
    stop_cmd = "kill -9 " + weewx_pid


    if request.method == 'POST':
        serviceaction = request.form.get('serviceaction')
        if serviceaction == "Restart":
            # Stop it
            sp.Popen(stop_cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, executable='/bin/bash')

            # Start it
            sp.Popen(start_cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, executable='/bin/bash')
            status = "true"

        elif serviceaction == "Stop":
            # Stop it
            sp.Popen(stop_cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, executable='/bin/bash')
            status = "false"

        else:
            # Start it
            sp.Popen(start_cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, executable='/bin/bash')
            status = "true"



    myret = dict(status = status)

    return render_template('menu/maintenance/service.html', **myret)

# Set Defaults Section
@app.route('/configuration/m_setdefaults', methods=['POST','GET'])
def m_setdefaults():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False, interpolation=False)
    defaultconfig = ConfigObj('/root/weewx-data/weewx.conf', list_values=False, interpolation=False)

    # Set the initial defaults
    entire = "true"
    station = "false"
    logging = "false"
    engine = "false"
    mqttsubscribeservice = "false"
    nws = "false"

    if request.method == 'POST':
        entire = request.form.get('entire')
        station = request.form.get('station')
        logging = request.form.get('logging')
        engine = request.form.get('engine')
        mqttsubscribeservice = request.form.get('mqttsubscribeservice')
        nws = request.form.get('nws')

        if entire == "true":
            # Copy the entire file over
            # Do this without shutil
            shutil.copyfile("/root/weewx-data/weewx.conf", "/config/weewx.conf")

        else:
            if station == "true":
                config['Station'] = defaultconfig['Station']
            if logging == "true":
                config['Logging'] = defaultconfig['Logging']

                # Does weewx.engine.StdPrint exiset in report_services?
                service = "weewx.engine.StdPrint"
                report_services = config['Engine']['Services']['report_services']

                if service not in report_services:
                    stdprintservice = "true"

                    # Change the report_services = weewx.engine.StdPrint, weewx.engine.StdReport
                    config['Engine']['Services']['report_services'] = config['Engine']['Services']['report_services'] + ", " + stdprint

            if engine == "true":
                config['Engine'] = defaultconfig['Engine']
            if mqttsubscribeservice == "true":
                config['MQTTSubscribeService'] = defaultconfig['MQTTSubscribeService']
            if nws == "true":
                config['NWS'] = defaultconfig['NWS']

            config.write()

    mydefaults = dict(entire = entire, station = station, logging = logging, engine = engine, mqttsubscribeservice = mqttsubscribeservice)
    return render_template('menu/maintenance/setdefaults.html', **mydefaults)

# Run Reports
@app.route('/configuration/m_runreports', methods=['POST','GET'])
def m_runreports():

    # Set the initial defaults
    all = "true"
    amphibian = "false"
    belchertown = "false"
    jas = "false"
    neowxmaterial = "false"
    nws = "false"
    seasons = "false"
    simple = "false"
    smartphone = "false"
    ss = "false"

    if request.method == 'POST':
        all = request.form.get('all')
        amphibian = request.form.get('amphibian')
        belchertown = request.form.get('belchertown')
        jas = request.form.get('jas')
        neowxmaterial = request.form.get('neowxmaterial')
        nws = request.form.get('nws')
        seasons = request.form.get('seasons')
        simple = request.form.get('simple')        
        smartphone = request.form.get('smartphone')
        ss = request.form.get('ss')
        wdc = request.form.get('wdc')
        
        reports = ""

        # Run the reports here
        # source ~/weewx-venv/bin/activate
        # weectl report run Seasons

        # Build the comnmand
        if all == "true":
            command = "source /root/weewx-venv/bin/activate; weectl report run --config=/config/weewx.conf"

        else:
            # build the command
            if amphibian == "true":
                reports = reports + " amphibian"
            if belchertown == "true":
                reports = reports + " Belchertown"
            if jas == "true":
                reports = reports + " jas"                
            if neowxmaterial == "true":
                reports = reports + " NeoWX-Material"
            if nws == "true":
                reports = reports + " NWSReport"
            if seasons == "true":
                reports = reports + " SeasonsReport"
            if simple == "true":
                reports = reports + " simple"
            if smartphone == "true":
                reports = reports + " SmartphoneReport"
            if ss == "true":
                reports = reports + " SteelSeries"
            if wdc == "true":
                reports = reports + " WdcReport"

            command = "source /root/weewx-venv/bin/activate; weectl report run " + reports + " --config=/config/weewx.conf"

        
        # Run the report(s)
        # probably out to use popen as the sp.run waits for completion
        ret = sp.run(command, capture_output=True, shell=True, executable='/bin/bash')

    myreports = dict(all = all, seasons = seasons, nws = nws, smartphone = smartphone, neowxmaterial = neowxmaterial, belchertown = belchertown)
    return render_template('menu/maintenance/runreports.html', **myreports)

@app.route('/configuration/m_resetdefaults', methods=['POST','GET'])
def m_resetdefaults():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # Set the initial defaults
    myentire = "true"
    mystation = "false"
    mylogging = "false"
    myengine = "false"
    mymqttsubscribeservice = "false"


    if request.method == 'POST':
        # Get the sections to reset
        myentire = request.form.get('entire')
        mystation = request.form.get('station')
        mylogging = request.form.get('logging')
        myengine =  request.form.get('engine')
        mytest =  request.form.get('test')
        mymqttsubscribeservice = request.form.get('mqttsubscribeservice')

        #if myentire == "true":
        mystation = "true"
        mytest = mytest + " POSTED"
        #   # copy the default config file
        #   shutil.copyfile("/root/weewx-data/weewx.conf", "/config/weewx.conf")

    mydefaults = dict(entire = myentire, station = mystation, logging = mylogging, engine = myengine, mqttsubscribeservice = mymqttsubscribeservice)
    return render_template('menu/maintenance/resetdefaults.html', **mydefaults)


############################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
