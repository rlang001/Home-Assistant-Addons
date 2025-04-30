#!/usr/bin/python3
#
from configparser import ConfigParser

def application(environ, start_response):
    
    # instantiate
    config = ConfigParser(allow_unnamed_section=True)

    # Read the file
    config.read('/config/weewx.conf')


    config['Station']['location']


    # parse existing file
    #station = config.get('Station')

    #latitude = config.getfloat('Station', 'latitude')
    #longitude = config.getfloat('Station', 'longitude')

    status = '200 OK'
    html_header = ''

    html_header = '<!DOCTYPE html>\n' \
           '<html lang="en">\n' \
           '<head>\n' \
           '  <title>WeeWX Station Config</title>\n' \
           '  <meta charset="utf-8">\n' \
           '  <meta name="viewport" content="width=device-width, initial-scale=1">\n' \
           '  <link rel="stylesheet" href="css/default.css">\n' \
           '  <link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">\n' \
           '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n' \
           '</head>\n'

    html_body = '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'WSGI Test Page\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n' \
           '<body>\n' \
           '  <div class="w3-container">\n' \
           '    <form class="w3-container">\n' \
           '      <label>First Name</label>\n' \
           '      <input class="w3-input" type="text">\n' \
           '      <label>Last Name</label>\n' \
           '      <input class="w3-input" type="text">\n' \
           '    </form>\n' \
           '  </div>\n' \
           '</body>\n' \
           '</html>'.encode("utf-8")

    html = html_head + html_body

    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

