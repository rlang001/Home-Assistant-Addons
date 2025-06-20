#!/bin/bash



source ~/weewx-venv/bin/activate
python3

from configobj import ConfigObj


config = ConfigObj('/config/weewx.conf', list_values=False)
if 'AcuRite' not in config.keys():
    config = ConfigObj('/config/stations/acurite.conf', list_values=False)

station_type = config['Station']['station_type']

filename = '/config/stations/' + station_type.lower() + ".conf"

station = ConfigObj(filename, list_values=False)

station_data = config[station_type]
station[station_type] = station_data
station.write()





