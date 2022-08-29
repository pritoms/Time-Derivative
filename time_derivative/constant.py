#!/usr/bin/env python3

import json
import os

PATH = os.path.abspath(os.curdir)
OUTPUT_FORMAT = 'text'
COLOR = True
HEADING = True
DECORATION = True

JSON_FILE = 'time_derivatives.json'
CONFIG_FILE = '.time_derivative_config'

DEFAULT_CONFIG = {
    'format': OUTPUT_FORMAT,
    'color': COLOR,
    'heading': HEADING,
    'decoration': DECORATION
}

DEFAULT_CONFIG_STRING = json.dumps(DEFAULT_CONFIG)
