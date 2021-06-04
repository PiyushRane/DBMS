#!/bin/bash

expect import.sh
expect time.sh > time.txt
python3 clean.py