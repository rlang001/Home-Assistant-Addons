#
#    Copyright (c) 2009-2020 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your rights.
#
"""The extended wview schema."""

# =============================================================================
# This is a list containing the default schema of the archive database.  It is
# only used for initialization --- afterwards, the schema is obtained
# dynamically from the database.  Although a type may be listed here, it may
# not necessarily be supported by your weather station hardware.
# =============================================================================
# NB: This schema is specified using the WeeWX V4 "new-style" schema.
# =============================================================================
table = [('dateTime',             'INTEGER NOT NULL UNIQUE PRIMARY KEY'),
         ('usUnits',              'INTEGER NOT NULL'),
         ('interval',             'INTEGER NOT NULL'),
         ('altimeter',            'REAL'),
         ('appTemp',              'REAL'),
         ('appTemp1',             'REAL'),
         ('barometer',            'REAL'),
         ('batteryStatus1',       'REAL'),
         ('batteryStatus2',       'REAL'),
         ('batteryStatus3',       'REAL'),
         ('batteryStatus4',       'REAL'),
         ('batteryStatus5',       'REAL'),
         ('batteryStatus6',       'REAL'),
         ('batteryStatus7',       'REAL'),
         ('batteryStatus8',       'REAL'),
         ('batteryStatus9',       'REAL'),
         ('batteryStatus10',       'REAL'),
         ('batteryStatus11',       'REAL'),
         ('batteryStatus12',       'REAL'),
         ('cloudbase',            'REAL'),
         ('co',                   'REAL'),
         ('co2',                  'REAL'),
         ('consBatteryVoltage',   'REAL'),
         ('dewpoint',             'REAL'),
         ('dewpoint1',            'REAL'),
         ('ET',                   'REAL'),
         ('extraHumid1',          'REAL'),
         ('extraHumid2',          'REAL'),
         ('extraHumid3',          'REAL'),
         ('extraHumid4',          'REAL'),
         ('extraHumid5',          'REAL'),
         ('extraHumid6',          'REAL'),
         ('extraHumid7',          'REAL'),
         ('extraHumid8',          'REAL'),
         ('extraTemp1',           'REAL'),
         ('extraTemp2',           'REAL'),
         ('extraTemp3',           'REAL'),
         ('extraTemp4',           'REAL'),
         ('extraTemp5',           'REAL'),
         ('extraTemp6',           'REAL'),
         ('extraTemp7',           'REAL'),
         ('extraTemp8',           'REAL'),
         ('forecast',             'REAL'),
         ('hail',                 'REAL'),
         ('hailBatteryStatus',    'REAL'),
         ('hailRate',             'REAL'),
         ('heatindex',            'REAL'),
         ('heatindex1',           'REAL'),
         ('heatingTemp',          'REAL'),
         ('heatingVoltage',       'REAL'),
         ('humidex',              'REAL'),
         ('humidex1',             'REAL'),
         ('inDewpoint',           'REAL'),
         ('inHumidity',           'REAL'),
         ('inTemp',               'REAL'),
         ('inTempBatteryStatus',  'REAL'),
         ('leafTemp1',            'REAL'),
         ('leafTemp2',            'REAL'),
         ('leafWet1',             'REAL'),
         ('leafWet2',             'REAL'),
         ('lightning_distance',        'REAL'),
         ('lightning_disturber_count', 'REAL'),
         ('lightning_energy',          'REAL'),
         ('lightning_noise_count',     'REAL'),
         ('lightning_strike_count',    'REAL'),
         ('luminosity',           'REAL'),
         ('maxSolarRad',          'REAL'),
         ('nh3',                  'REAL'),
         ('no2',                  'REAL'),
         ('noise',                'REAL'),
         ('o3',                   'REAL'),
         ('outHumidity',          'REAL'),
         ('outTemp',              'REAL'),
         ('outTempBatteryStatus', 'REAL'),
         ('pb',                   'REAL'),
         ('pm10_0',               'REAL'),
         ('pm1_0',                'REAL'),
         ('pm2_5',                'REAL'),
         ('pressure',             'REAL'),
         ('radiation',            'REAL'),
         ('rain',                 'REAL'),
         ('rainBatteryStatus',    'REAL'),
         ('rainRate',             'REAL'),
         ('referenceVoltage',     'REAL'),
         ('rxCheckPercent',       'REAL'),
         ('signal1',              'REAL'),
         ('signal2',              'REAL'),
         ('signal3',              'REAL'),
         ('signal4',              'REAL'),
         ('signal5',              'REAL'),
         ('signal6',              'REAL'),
         ('signal7',              'REAL'),
         ('signal8',              'REAL'),
         ('snow',                 'REAL'),
         ('snowBatteryStatus',    'REAL'),
         ('snowDepth',            'REAL'),
         ('snowMoisture',         'REAL'),
         ('snowRate',             'REAL'),
         ('so2',                  'REAL'),
         ('soilMoist1',           'REAL'),
         ('soilMoist2',           'REAL'),
         ('soilMoist3',           'REAL'),
         ('soilMoist4',           'REAL'),
         ('soilMoist5',           'REAL'),
         ('soilMoist6',           'REAL'),
         ('soilMoist7',           'REAL'),
         ('soilMoist8',           'REAL'),
         ('soilTemp1',            'REAL'),
         ('soilTemp2',            'REAL'),
         ('soilTemp3',            'REAL'),
         ('soilTemp4',            'REAL'),
         ('soilTemp5',            'REAL'),
         ('soilTemp6',            'REAL'),
         ('soilTemp7',            'REAL'),
         ('soilTemp8',            'REAL'),
         ('supplyVoltage',        'REAL'),
         ('txBatteryStatus',      'REAL'),
         ('UV',                   'REAL'),
         ('uvBatteryStatus',      'REAL'),
         ('windBatteryStatus',    'REAL'),
         ('windchill',            'REAL'),
         ('windDir',              'REAL'),
         ('windGust',             'REAL'),
         ('windGustDir',          'REAL'),
         ('windrun',              'REAL'),
         ('windSpeed',            'REAL'),
         ]

day_summaries = [(e[0], 'scalar') for e in table
                 if e[0] not in ('dateTime', 'usUnits', 'interval')] + [('wind', 'VECTOR')]

schema = {
    'table': table,
    'day_summaries' : day_summaries
}