# routes/maintenence.py

from flask import Flask, render_template, request
from configobj import ConfigObj
import subprocess as sp


from flask import Blueprint

# my utilities
from utils import utilities


bp = Blueprint('maintenance', __name__)


############################################################
# Maintenance Section
# Service Section
@bp.route('/configuration/m_service', methods=['POST','GET'])
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
    reports = utilities.getReports()

    return render_template('menu/maintenance/service.html', **myret, **reports)

# Set Defaults Section
@bp.route('/configuration/m_setdefaults', methods=['POST','GET'])
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
    reports = utilities.getReports()

    return render_template('menu/maintenance/setdefaults.html', **mydefaults, **reports)

# Run Reports
@bp.route('/configuration/m_runreports', methods=['POST','GET'])
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
        # ret = sp.run(command, capture_output=True, shell=True, executable='/bin/bash')
        sp.Popen(command, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, executable='/bin/bash')


    myreports = dict(all = all, seasons = seasons, nws = nws, smartphone = smartphone, neowxmaterial = neowxmaterial, belchertown = belchertown)
    reports = utilities.getReports()

    return render_template('menu/maintenance/runreports.html', **myreports, **reports)

@bp.route('/configuration/m_resetdefaults', methods=['POST','GET'])
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
    reports = utilities.getReports()

    return render_template('menu/maintenance/resetdefaults.html', **mydefaults, **reports)
