#!/usr/bin/env python
# coding=utf-8 

import yaml
import logging

# Open the YAML file
try:
    with open('/config/config.yaml', 'r') as file:
        # Load the content into a dictionary
        config = yaml.safe_load(file)
except FileNotFoundError:
    logger.warning("/config/config.yaml not found.  Reverting to defaults")
    with open('/root/config.yaml', 'r') as file:
        # Load the content into a dictionary
        config = yaml.safe_load(file)

#
discovery = config['discovery']
ids = config['discovery']['ids']

