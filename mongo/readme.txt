Install mongoDB in linux system and start the mongod process by "sudo systemctl start mongod"

Run the command below and it will do everything needed to produce time per query per database:-
"bash run.sh"
It can take 2-3 minutes to run

I have used a bash script to import the data to MongoDB database and java script to run the queries. The “run.sh” script first import the data using "bash import.sh" and then run "mongo s1.js | grep "millis" | tee t1.txt" and so on to get the time in 4 files naming "t1.txt" for query 1, "t2.txt" for query 2 and so on. After getting the time, run "clean.py" to get the time for each database in a different file having 4 lines representing time of 4 queries and each line have 7 time data separated by ‘,’ stored in folder "time". 

