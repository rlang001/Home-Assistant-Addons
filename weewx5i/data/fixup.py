#!/usr/bin/python3
#
from configobj import ConfigObj

config = ConfigObj('/root/weewx-data/weewx.conf', list_values=False, interpolation=False)
wdc = ConfigObj('/root/weewx-data/skins/weewx-wdc/skin.conf', list_values=False, interpolation=False)


neowx = ConfigObj('/root/weewx-data/neowx-material.conf', list_values=False, interpolation=False)
logging = ConfigObj('/root/weewx-data/logging.conf', list_values=False, interpolation=False)
jas = ConfigObj('/root/weewx-data/jas.conf', list_values=False, interpolation=False)

config.merge(neowx)
config.merge(logging)
config.merge(jas)

config['StdReport']['SKIN_ROOT'] = "/config/skins"

config['StdReport']['HTML_ROOT'] = "/var/www/html/standard"
# config['StdReport']['enable'] = "false"

config['StdReport']['SeasonsReport']['HTML_ROOT'] = "/var/www/html/seasons"
config['StdReport']['SeasonsReport']['enable'] = "true"

config['StdReport']['SmartphoneReport']['HTML_ROOT'] = "/var/www/html/smartphone"
config['StdReport']['SmartphoneReport']['enable'] = "true"

config['StdReport']['MobileReport']['HTML_ROOT'] = "/var/www/html/mobile"
config['StdReport']['MobileReport']['enable'] = "true"

config['StdReport']['NWSReport']['HTML_ROOT'] = "/var/www/html/nws"
config['StdReport']['NWSReport']['enable'] = "true"

config['StdReport']['Belchertown']['HTML_ROOT'] = "/var/www/html/belchertown"
config['StdReport']['Belchertown']['enable'] = "true"

config['StdReport']['amphibian']['HTML_ROOT'] = "/var/www/html/amphibian"
config['StdReport']['amphibian']['enable'] = "true"

config['StdReport']['WdcReport']['HTML_ROOT'] = "/var/www/html/wdc"
config['StdReport']['WdcReport']['enable'] = "true"

config['StdReport']['simple']['HTML_ROOT'] = "/var/www/html/simple"
config['StdReport']['simple']['enable'] = "true"

config['StdReport']['SteelSeries']['HTML_ROOT'] = "/var/www/html/ss"
config['StdReport']['SteelSeries']['enable'] = "true"

# config['StdReport']['forecast']['HTML_ROOT'] = "/var/www/html/forecast"

#config['StdReport']['Bootstrap']['HTML_ROOT'] = "/var/www/html/bootstrap"
#config['StdReport']['Bootstrap']['enable'] = "true"
#config['StdReport']['Bootstrap']['lang'] = "en"


#config['StdReport']['OBWX']['HTML_ROOT'] = "/var/www/html/obwx"
#config['StdReport']['OBWX']['enable'] = "true"

#config['StdReport']['Me.teo']['HTML_ROOT'] = "/var/www/html/meteo"
#config['StdReport']['Me.teo']['enable'] = "true"

#config['StdReport']['AllTimeSeasons']['enable'] = "true"
#config['StdReport']['AllTimeSeasons']['HTML_ROOT'] = "/var/www/html/alltimeseasons"


config['StdRESTful']['MQTT']['enable'] = "false"
config['StdRESTful']['MQTT']['server_url'] = ""
config['StdRESTful']['MQTT']['topic'] = "weather"
config['StdRESTful']['MQTT']['binding'] = "loop"
config['StdRESTful']['MQTT']['unit_system'] = "US"
config['StdRESTful']['MQTT']['aggregation'] = "individual"

config.merge(neowx)
config.merge(logging)

config['StdReport']['NeoWX-Material']['HTML_ROOT'] = "/var/www/html/neowxmaterial"
config['StdReport']['NeoWX-Material']['enable'] = "true"


config['DatabaseTypes']['SQLite']['SQLITE_ROOT'] = "/config"

# Get the report services
# Change the report_services = weewx.engine.StdPrint, weewx.engine.StdReport
reportServices = config['Engine']['Services']['report_services']
stdPrint = "weewx.engine.StdPrint"

if stdPrint in reportServices:
    s = reportServices.replace(stdPrint, "").strip(",")
    config['Engine']['Services']['report_services'] = s

# Fix the WDC html location
wdc['Extras']['base_path'] = "/wdc/"
wdc.write()

config.write()