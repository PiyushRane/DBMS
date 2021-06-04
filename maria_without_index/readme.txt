Install "expect" in your system to run the the expect script that I have used.

Run the command below and it will do every thing needed to produce time per query per database:-
"bash run.sh"
It can take 3-4 hours to run

I have used expect script to import the data to MariaDB database and bash script to run the queries. The “run.sh” script first import the data using "expect import.sh" and then run "bash time.sh" to get the time in 4 files naming "t1.txt" for query 1, "t2.txt" for query 2 and so on.
After getting the time, run "clean.py" to get the time for each database in different file having 4 lines representing time of 4 queries and each line have 7 time data separated by ‘,’ stored in folder "time". 


