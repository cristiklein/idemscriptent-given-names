#!/bin/bash

# Bail out on any error
set -e

coverage run *_test.py
coverage report --show-missing
