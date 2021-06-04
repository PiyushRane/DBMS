#!/bin/bash

mkdir -p "time"
bash import.sh
mongo s1.js | grep "millis" | tee t1.txt
mongo s2.js | grep "millis" | tee t2.txt
mongo s3.js | grep "millis" | tee t3.txt
mongo s4.js | grep "millis" | tee t4.txt
python3 clean.py