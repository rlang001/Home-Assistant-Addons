#!/bin/sh
export PYTHONPATH="/root/shinysdr"
exec python -m shinysdr.main "$@"
