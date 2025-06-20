# routes/config_reprots.py

from flask import Flask, render_template, request
from configobj import ConfigObj

from flask import Blueprint

# my utilities
from utils import utilities

bp = Blueprint('config_reports', __name__)

############################################################
# Reports Section
@bp.route('/configuration/c_stdreports', methods=['POST','GET'])
def c_stdreports():

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
@bp.route('/configuration/c_ftp', methods=['POST','GET'])
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
    reports = utilities.getReports()

    return render_template('menu/config/reports/ftp.html', **myftp, **reports)

############################################################
# reports/Rsync Section
@bp.route('/configuration/c_rsync', methods=['POST','GET'])
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
    reports = utilities.getReports()

    return render_template('menu/config/reports/rsync.html', **myrsync, **reports)
