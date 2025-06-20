# routes/config_main.py

from flask import Flask, render_template, request
from configobj import ConfigObj
import subprocess as sp


from flask import Blueprint
from utils import utilities


bp = Blueprint('config_main', __name__)

#############################################################
# Configuation
#############################################################
# Overall Section
@bp.route('/configuration/c_overall', methods=['POST','GET'])
def c_overall():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)


    if request.method == 'POST':
        config['debug'] = request.form.get('debug')
        config['log_success'] = request.form.get('log_success')
        config['log_failure'] = request.form.get('log_failure')

        config.write()

    myoverall = dict(version = config['version'], 
                    debug = config['debug'], 
                    log_success = config['log_success'].lower(), 
                    log_failure = config['log_failure'].lower()
                    )

    reports = utilities.getReports()
    # z = {**reports, **myoverall}

    return render_template('menu/config/overall.html', **myoverall, **reports)

# Station Section
@bp.route('/configuration/c_station', methods=['POST','GET'])
def c_station():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    # Get the current station type
    current_station_type = config['Station']['station_type']

    if request.method == 'POST':

        config['Station']['location'] = request.form.get('location').strip()
        config['Station']['latitude'] = request.form.get('latitude').strip()
        config['Station']['longitude'] = request.form.get('longitude').strip()
        config['Station']['altitude'] = request.form.get('altitude').strip()
        config['Station']['altitude'] = request.form.get('altitude') + "," + request.form.get('altitude_unit') 
        config['Station']['station_type'] = request.form.get('station_type')
        config['Station']['rain_year_start'] = request.form.get('rain_year_start')
        config['Station']['week_start'] = request.form.get('week_start')

        new_station_type = request.form.get('station_type')
        # Swap the station section if a new type is selected
        if current_station_type != new_station_type:
            # Save the old one to /config/stations 
            filename = '/config/stations/' + current_station_type.lower() + ".conf"
            station = ConfigObj(filename, list_values=False)
            station_data = config[current_station_type]
            station[current_station_type] = station_data
            station.write()
            # and remove the section
            config.pop(current_station_type)
            # Add the new in
            new_station = ConfigObj('/config/stations/' + new_station_type.lower() + ".conf", list_values=False, interpolation=False)
            config.merge(new_station)

        config.write()

    mystation = dict(location = config['Station']['location'].strip(),
                    latitude = config['Station']['latitude'].strip(),
                    longitude = config['Station']['longitude'].strip(),
                    altitude = config['Station']['altitude'].split(',')[0].strip(),
                    altitude_unit = config['Station']['altitude'].split(',')[1].strip(),
                    station_type = config['Station']['station_type'],
                    rain_year_start = config['Station']['rain_year_start'],
                    week_start = config['Station']['week_start'] 
                    )

    reports = utilities.getReports()
    return render_template('menu/config/station.html', **mystation, **reports)

# Logging Section
@bp.route('/configuration/c_logging', methods=['POST','GET'])
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
    reports = utilities.getReports()
    
    return render_template('menu/config/logging.html', **mylogging, **reports, stdprint = stdprint)

# DerivedValues Section
@bp.route('/configuration/c_derivedvalues', methods=['POST','GET'])
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

    reports = utilities.getReports()
    myderivedvalues = dict(config['StdWXCalculate']['Calculations'])
    return render_template('menu/config/derivedvalues.html', **myderivedvalues, **reports)

# MQTTSubscribeService
@bp.route('/configuration/c_mqttsubscribeservice', methods=['POST','GET'])
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
    reports = utilities.getReports()
    return render_template('menu/config/mqttsubscribeservice.html', 
        **mymqttsubscribeservice, **reports)

# NWS
@bp.route('/configuration/c_nws', methods=['POST','GET'])
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
    reports = utilities.getReports()
    
    return render_template('menu/config/nws.html', **mynws, **reports)