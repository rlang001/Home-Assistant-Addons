# Home Assistant Add-On: shinySDR.  The software component of a software-defined radio receiver. When combined with suitable hardware devices such as the RTL-SDR, HackRF, or USRP, it can be used to listen to or display data from a variety of radio transmissions.

## Features and applications

This Add-On is based on https://shinysdr.switchb.org

I just added a few sprinkles to make it work with Home Assistant.

### Remote operation:
The receiver can be listened to and remotely controlled over a LAN or the Internet; the user interface works the same everywhere.

Requires network capacity of 3 Mb/s or greater, depending on settings. Google Chrome (excluding Chrome for iOS) is recommended. Phone/tablet compatible.

Internet access is not required for local or LAN operation.

### Receive audio transmissions and broadcasts:
ShinySDR supports all standard analog modes — AM, FM (narrowband and broadcast), SSB, CW. You can monitor multiple frequencies at once, limited only by hardware bandwidth, and use stereo panning for easier listening.

Receive and decode telemetry data: ShinySDR can decode and display ADS-B, APRS, WSPR, and the telemetry formats supported by rtl_433. When position information is available, it is displayed on a map with animated extrapolated positions.

Telemetry support requires installation of additional (open source) software as described in the installation instructions.

### Frequency database:
Jump to favorite stations; catalog signals you hear; import published tables of band, channel, and station info. Stations with known coordinates can be displayed on the map.

### Persistent waterfall display:
You can zoom, pan, and retune without losing any of the displayed history, whereas many other programs will discard anything which is temporarily offscreen, or the whole thing if the window is resized. If you zoom in to get a look at one signal, you can zoom out again.

## Supported modes
- Analog audio: AM, FM narrowband, FM broadcast, SSB, CW.
- Digital audio: All those supported by gr-dsd.
- Text: RTTY, PSK31.
- Telemetry: APRS, Mode S/ADS-B, WSPR, all those supported by rtl_433.


## Installation

- If not already done, add the Add-on repostitory ((https://github.com/rlang001/Home-Assistant-Addons))

## TODO

- Checkout https://github.com/wiedehopf/tar1090
- Use prebuild docker images. Tried whole evening but multi-arch is a pain in that case.