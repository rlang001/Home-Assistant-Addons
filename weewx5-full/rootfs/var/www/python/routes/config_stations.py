# routes/config_stations.py

from flask import Flask, render_template, request
from configobj import ConfigObj

from flask import Blueprint

# my utilities
from utils import utilities

bp = Blueprint('config_stations', __name__)


###########################################################
# Config/stations/Simulator
@bp.route('/configuration/s_simulator', methods=['POST','GET'])
def s_simulator():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Simulator section
    if 'Simulator' not in config.keys():
        config = ConfigObj('/config/stations/simulator.conf', list_values=False)

    if request.method == 'POST':
        config['Simulator']['loop_interval'] = request.form.get('loop_interval')
        config['Simulator']['mode'] = request.form.get('mode')
        if request.form.get('start'):
            config['Simulator']['start'] = request.form.get('start')

        config.write()

    mysimulator = dict((config['Simulator']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/simulator.html', **mysimulator, **reports)

@bp.route('/configuration/s_acurite', methods=['POST','GET'])
def s_acurite():
    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is an acurite section
    if 'AcuRite' not in config.keys():
        config = ConfigObj('/config/stations/acurite.conf', list_values=False)

    if request.method == 'POST':
        config['AcuRite']['use_contants'] = request.form.get('use_contants')
        config['AcuRite']['model'] = request.form.get('model')

        config.write()

    myacurite = dict((config['AcuRite']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/acurite.html', **myacurite, **reports)

@bp.route('/configuration/s_cc3000', methods=['POST','GET'])
def s_cc3000():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a cc3000 section
    if 'CC3000' not in config.keys():
        config = ConfigObj('/config/stations/cc3000.conf', list_values=False)


    if request.method == 'POST':
        config['CC3000']['model'] = request.form.get('model')
        config['CC3000']['port'] = request.form.get('port')
        config['CC3000']['debug_serial'] = request.form.get('debug_serial')
        config['CC3000']['debug_openclose'] = request.form.get('debug_openclose')
        config['CC3000']['debug_checksum'] = request.form.get('debug_checksum')
        config['CC3000']['logger_threshold'] = request.form.get('logger_threshold')
        config['CC3000']['max_tries'] = request.form.get('max_tries')
        config['CC3000']['polling_interval'] = request.form.get('polling_interval')
        config['CC3000']['use_station_time'] = request.form.get('use_station_time')

        config.write()

    mycc3000 = dict((config['CC3000']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/cc3000.html', **mycc3000, **reports)

@bp.route('/configuration/s_fineoffsetusb', methods=['POST','GET'])
def s_fineoffsetusb():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a FineOffsetUSB section
    if 'FineOffsetUSB' not in config.keys():
        config = ConfigObj('/config/stations/fineoffsetusb.conf', list_values=False)

    if request.method == 'POST':
        config['FineOffsetUSB']['model'] = request.form.get('model')
        config['FineOffsetUSB']['polling_mode'] = request.form.get('polling_mode')
        config['FineOffsetUSB']['polling_interval'] = request.form.get('polling_interval')
        config['FineOffsetUSB']['data_format'] = request.form.get('data_format')

        config.write()

    myfineoffsetusb = dict((config['FineOffsetUSB']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/fineoffsetusb.html', **myfineoffsetusb, **reports)

@bp.route('/configuration/s_te923', methods=['POST','GET'])
def s_te923():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a TE923 section
    if 'TE923' not in config.keys():
        config = ConfigObj('/config/stations/te923.conf', list_values=False)

    if request.method == 'POST':
        config['TE923']['model'] = request.form.get('model')
        config.write()

    myte923= dict((config['TE923']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/te923.html', **myte923, **reports)

@bp.route('/configuration/s_ultimeter', methods=['POST','GET'])
def s_ultimeter():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'Ultimeter' not in config.keys():
        config = ConfigObj('/config/stations/ultimeter.conf', list_values=False)

    if request.method == 'POST':
        config['Ultimeter']['port'] = request.form.get('port')
        config['Ultimeter']['model'] = request.form.get('model')
        config.write()

    myultimeter= dict((config['Ultimeter']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/ultimeter.html', **myultimeter, **reports)

@bp.route('/configuration/s_vantage', methods=['POST','GET'])
def s_vantage():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'Vantage' not in config.keys():
        config = ConfigObj('/config/stations/vantage.conf', list_values=False)

    if request.method == 'POST':
        config['Vantage']['type'] = request.form.get('type')
        config['Vantage']['port'] = request.form.get('port')
        config['Vantage']['host'] = request.form.get('host')
        config['Vantage']['baudrate'] = request.form.get('baudrate')
        config['Vantage']['tcp_port'] = request.form.get('tcp_port')
        config['Vantage']['tcp_send_delay'] = request.form.get('tcp_send_delay')
        config['Vantage']['loop_request'] = request.form.get('loop_request')
        config['Vantage']['iss_id'] = request.form.get('iss_id')
        config['Vantage']['timeout'] = request.form.get('timeout')
        config['Vantage']['wait_before_retry'] = request.form.get('wait_before_retry')
        config['Vantage']['max_tries'] = request.form.get('max_tries')
        config.write()

    myvantage= dict((config['Vantage']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/vantage.html', **myvantage, **reports)

@bp.route('/configuration/s_wmr100', methods=['POST','GET'])
def s_wmr100():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WMR100' not in config.keys():
        config = ConfigObj('/config/stations/wmr100.conf', list_values=False)

    if request.method == 'POST':
        config['WMR100']['model'] = request.form.get('model')
        config.write()

    mywmr100= dict((config['WMR100']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/wmr100.html', **mywmr100, **reports)

@bp.route('/configuration/s_wmr300', methods=['POST','GET'])
def s_wmr300():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WMR300' not in config.keys():
        config = ConfigObj('/config/stations/wmr300.conf', list_values=False)

    if request.method == 'POST':
        config['WMR300']['model'] = request.form.get('model')
        config.write()

    mywmr300= dict((config['WMR300']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/wmr300.html', **mywmr300, **reports)

@bp.route('/configuration/s_wmr9x8', methods=['POST','GET'])
def s_wmr9x8():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WMR9x8' not in config.keys():
        config = ConfigObj('/config/stations/wmr9x8.conf', list_values=False)

    if request.method == 'POST':
        config['WMR9x8']['type'] = request.form.get('type')
        config['WMR9x8']['port'] = request.form.get('port')
        config['WMR9x8']['model'] = request.form.get('model')
        config.write()

    mywmr9x8 = dict((config['WMR9x8']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/wmr9x8.html', **mywmr9x8, **reports)

@bp.route('/configuration/s_ws1', methods=['POST','GET'])
def s_ws1():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WS1' not in config.keys():
        config = ConfigObj('/config/stations/ws1.conf', list_values=False)

    if request.method == 'POST':
        config['WS1']['mode'] = request.form.get('mode')
        config['WS1']['port'] = request.form.get('port')
        config['WS1']['polling_interval'] = request.form.get('polling_interval')        
        config.write()

    myws1 = dict((config['WS1']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/ws1.html', **myws1, **reports)

@bp.route('/configuration/s_ws23xx', methods=['POST','GET'])
def s_ws23xx():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WS23xx' not in config.keys():
        config = ConfigObj('/config/stations/ws23xx.conf', list_values=False)

    if request.method == 'POST':
        config['WS23xx']['port'] = request.form.get('port')
        config['WS23xx']['model'] = request.form.get('model')        
        config['WS23xx']['polling_interval'] = request.form.get('polling_interval')        
        config.write()

    myws23xx = dict((config['WS23xx']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/ws23xx.html', **myws23xx, **reports)

    
@bp.route('/configuration/s_ws28xx', methods=['POST','GET'])
def s_ws28xx():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'WS28xx' not in config.keys():
        config = ConfigObj('/config/stations/ws28xx.conf', list_values=False)

    if request.method == 'POST':
        config['WS28xx']['model'] = request.form.get('model')        
        config['WS28xx']['transceiver_frequency'] = request.form.get('transceiver_frequency')        
        config.write()

    myws28xx = dict((config['WS28xx']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/ws28xx.html', **myws28xx, **reports)

@bp.route('/configuration/s_sdr', methods=['POST','GET'])
def s_sdr():

    # Read the file
    config = ConfigObj('/config/weewx.conf', list_values=False)

    # check if there is a Ultimeter section
    if 'SDR' not in config.keys():
        config = ConfigObj('/config/stations/sdr.conf', list_values=False)

    if request.method == 'POST':
        config['SDR']['model'] = request.form.get('model')        
        config['SDR']['transceiver_frequency'] = request.form.get('transceiver_frequency')        

        config.write()

    mysdr = dict((config['SDR']))

    reports = utilities.getReports()
    return render_template('menu/config/stations/sdr.html', **mysdr, **reports)