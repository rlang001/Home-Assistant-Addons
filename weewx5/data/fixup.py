#!/usr/bin/python3
#
# Fix up some weewx.conf file entries
#


import fileinput
from configobj import ConfigObj
from os import system


# Open some config files
config = ConfigObj('/root/weewx-data/weewx.conf', list_values=False, interpolation=False)
wdc = ConfigObj('/root/weewx-data/skins/weewx-wdc/skin.conf', list_values=False, interpolation=False)
neowx = ConfigObj('/root/weewx-data/neowx-material.conf', list_values=False, interpolation=False)
logging = ConfigObj('/root/weewx-data/logging.conf', list_values=False, interpolation=False)
jas = ConfigObj('/root/weewx-data/jas.conf', list_values=False, interpolation=False)
simulator = ConfigObj('/root/weewx-data/stations/simulator.conf', list_values=False, interpolation=False)

# Merge some into weewx.conf
config.merge(neowx)
config.merge(logging)
config.merge(jas)
config.merge(simulator)

# Fix the user root
config['USER_ROOT'] = "/config/bin/user"


# Point to html  directory
config['StdReport']['HTML_ROOT'] = "/var/www/html"

# Fix skin stuff
config['StdReport']['SKIN_ROOT'] = "/config/skins"

config['StdReport']['enable'] = "false"

config['StdReport']['SeasonsReport']['HTML_ROOT'] = "/var/www/html/seasons"
config['StdReport']['SeasonsReport']['enable'] = "false"

config['StdReport']['SmartphoneReport']['HTML_ROOT'] = "/var/www/html/smartphone"
config['StdReport']['SmartphoneReport']['enable'] = "false"

config['StdReport']['MobileReport']['HTML_ROOT'] = "/var/www/html/mobile"
config['StdReport']['MobileReport']['enable'] = "false"

config['StdReport']['NWSReport']['HTML_ROOT'] = "/var/www/html/nws"
config['StdReport']['NWSReport']['enable'] = "false"

config['StdReport']['Belchertown']['HTML_ROOT'] = "/var/www/html/belchertown"
config['StdReport']['Belchertown']['enable'] = "false"

config['StdReport']['amphibian']['HTML_ROOT'] = "/var/www/html/amphibian"
config['StdReport']['amphibian']['enable'] = "false"

config['StdReport']['WdcReport']['HTML_ROOT'] = "/var/www/html"
config['StdReport']['WdcReport']['enable'] = "true"

config['StdReport']['simple']['HTML_ROOT'] = "/var/www/html/simple"
config['StdReport']['simple']['enable'] = "false"

config['StdReport']['Me.teo']['HTML_ROOT'] = "/var/www/html/meteo"
config['StdReport']['Me.teo']['HTML_SUBDIR'] = "meteo"
config['StdReport']['Me.teo']['enable'] = "false"

# config['StdReport']['forecast']['HTML_ROOT'] = "/var/www/html/forecast"

#config['StdReport']['Bootstrap']['HTML_ROOT'] = "/var/www/html/bootstrap"
#config['StdReport']['Bootstrap']['enable'] = "false"
#config['StdReport']['Bootstrap']['lang'] = "en"


#config['StdReport']['OBWX']['HTML_ROOT'] = "/var/www/html/obwx"
#config['StdReport']['OBWX']['enable'] = "false"

#config['StdReport']['Me.teo']['HTML_ROOT'] = "/var/www/html/meteo"
#config['StdReport']['Me.teo']['enable'] = "false"

#config['StdReport']['AllTimeSeasons']['enable'] = "false"
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



######################################################################################################
# Database location fixups

config['Databases']['archive_sqlite']['database_name'] = "dbs/weewx.sdb"
config['Databases']['archive_mysql']['database_name'] = "dbs/weewx"
config['Databases']['nws_sqlite']['database_name'] = "dbs/nws.sdb"
config['Databases']['cmon_sqlite']['database_name'] = "dbs/cmon.sdb"
config['Databases']['forecast_sqlite']['database_name'] = "dbs/forecast.sdb"


config.write()

######################################################################################################
# Simple skin fixes to work withg Python3

for line in fileinput.input("/root/weewx-data/skins/simple/index.html.tmpl", inplace=True):
    # inside this loop the STDOUT will be redirected to the file
    print(line.replace("trend.windSpeed.formatted", "trend.windSpeed.raw"), end="")

######################################################################################################
# NeoXW-material fixes
for line in fileinput.input("/root/weewx-data/skins/neowx-material/head.inc", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/header.inc", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/header.inc", inplace=True):
    print(line.replace("is '", "== '"), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/footer.inc", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/index.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/month.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/week.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/year.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/month-%Y-%m.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/year-%Y.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

for line in fileinput.input("/root/weewx-data/skins/neowx-material/yesterday.html.tmpl", inplace=True):
    print(line.replace("is not \"\"", "!= \"\""), end="")

######################################################################################################
# Extensions.py
for line in fileinput.input("/root/weewx-data/bin/user/extensions.py", inplace=True):
    print(line.replace("import locale", "import locale\nimport weewx.units\n"), end="")

system("cat /root/weewx-data/extensions.py >> /root/weewx-data/bin/user/extensions.py")