# Home Assistant Add-on: WeeWX-HA

_WeeWX addon to read weather sensors._

## About
You can use this add-on to install WeeWX, an open-source a free, open source, software program, written in Python, which interacts with your weather station to produce graphs, reports, and HTML pages. It can optionally publish to weather sites or web servers. It uses modern software concepts, making it simple, robust, and easy to extend. For more information, please see [weewx].

I wanted to leverage my current Home Assistant instance to run WeeWX.  Currently I use the RTL-SDR library to read data directly from my weather sensor as the HA hardware resides in an incovenient location to connect to the console via USB.  As a bonus, if you don't have a sensor, grab the data from your neighbor's :).

## Included in the container:
- WeeWX: [weewx]
- RTL-SDR
- RTL-433
- Eclipse Paho™ MQTT Python Client: [pahoo.mqtt.python] 
- Matthew Wall's WeeWX MQTT extension: [weewx-mqtt] 
- Matthew Wall's SDR driver: [weewx-sdr] 
- John Kline's WeeWX NWS: [weewx-nws]

## Skins included:
- NeoWX-Material: [NeoWX-Material]
- Steel Series Weather Gaugues: [Steel Series Weather Gaugues]
- Amphibian: [Amphibian]
- Belchertown: [Belchertown]

[weewx]: https://www.weewx.com/
[pahoo.mqtt.python]: https://github.com/eclipse/paho.mqtt.python
[weewx-mqtt]:https://github.com/matthewwall/weewx-mqtt
[weewx-sdr]: https://github.com/matthewwall/weewx-sdr
[weewx-nws]:https://github.com/chaunceygardiner/weewx-nws
[NeoWX-Material]: https://neoground.com/projects/neowx-material
[Steel Series Weather Gaugues]: https://github.com/weewx/weewx/wiki/steelseries
[Amphibian]: https://github.com/weewx/weewx/wiki/amphibian
[Belchertown]: https://github.com/poblabs/weewx-belchertown

## Installation
- Repository not yet created

## Configuration
You must edit the config file /config/weewx/weewx.conf in the root of your Home Assistant configuration directory.  Refer to the weewx configuration guide.
### Files
Persistent files are located at /config/weewx of the Home Assistant directory
- Config file - weewx.conf
- Log file - weewx.log
- WeeWX SQLite database - weewx.sdb
- WeeWX-NWS database - nws.sdb
- skins/
  Directory of current skins.  Modifications made to the files here are used by the addon after restart. Deleting any file/directory forces the addon to use the default
- index.html
  User modifications are used by the skin after restart.  Deleting forces the default


## Logs 
 Logs are sent to /config/weewx/logs/weewx.log

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

