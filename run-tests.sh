#!/bin/bash

# Bail out on any error
set -e

coverage erase
for FILE in *_test.py; do
	coverage run --append $FILE
done
coverage report --show-missing
