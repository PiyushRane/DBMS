Install "expect" in your system to run the expect script that i have used.

Remove all the databases from dbs directory
Run the command below and it will do every thing needed to produce time per query per database:-
"bash run.sh"
It will take 1-2 mins to run

I have used expect script to import the data to sqlite database and to run the queries.
The “run.sh” script first import the data using "import.sh" file and then run "time.sh" to get the time in file "time.txt" and the output of queries in folder "query".
After getting the time, run "clean.py" to get the time for each database in different file
having 4 lines representing time of 4 queries and each line have 7 time data separated by ‘,’ stored in folder "time". 

