# routes/config_restful.py

from flask import Flask, render_template, request
from configobj import ConfigObj

from flask import Blueprint

# my utilities
from utils import utilities

bp = Blueprint('config_restful', __name__)

############################################################
# Restful/stationregistry
@bp.route('/configuration/c_stationregistry', methods=['POST','GET'])
def c_stationregistry():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)
    if request.method == 'POST':
        # Station registry
        config['StdRESTful']['StationRegistry']['register_this_station'] = request.form.get('register_this_station')

        config.write()

    mystationregistry = dict(register_this_station = config['StdRESTful']['StationRegistry']['register_this_station'].lower())
    reports = utilities.getReports()

    return render_template('menu/config/restful/stationregistry.html', **mystationregistry, **reports)

# Restful/AWEKAS
@bp.route('/configuration/c_awekas', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/awekas.html', **myawekas, **reports)

# Restful/CWOP
@bp.route('/configuration/c_cwop', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/cwop.html', **mycwop, **reports)

# Restful/PWSWeather
@bp.route('/configuration/c_pwsweather', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/pwsweather.html', **mypwsweather, **reports)

# Restful/WOW
@bp.route('/configuration/c_wow', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/wow.html', **mywow, **reports)

# Restful/Wunderground
@bp.route('/configuration/c_wunderground', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/wunderground.html', **mywunderground, **reports)

# Restful/MQTT
@bp.route('/configuration/c_mqtt', methods=['POST','GET'])
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

    reports = utilities.getReports()

    return render_template('menu/config/restful/mqtt.html', **mymqtt, **reports)
