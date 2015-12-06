#!/bin/bash

# Bail out on any error
set -e

coverage run WikipediaKnowledgeBase.py
coverage report
