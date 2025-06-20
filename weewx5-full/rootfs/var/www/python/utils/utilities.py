from flask import Flask
from configobj import ConfigObj
from flask import Blueprint



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
