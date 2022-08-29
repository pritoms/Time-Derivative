#!/bin/bash

set -e

time_derivatives.py time_derivatives.json /tmp/test/
time_derivatives.py time_derivatives.json /tmp/test/
time_derivative.py time_derivatives.json
time_derivative.py --format html time_derivatives.json > test.html
