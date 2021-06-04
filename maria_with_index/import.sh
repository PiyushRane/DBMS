#!/usr/bin/expect

set dbs(0) "dbidx1" 
set dbs(1) "dbidx2" 
set dbs(2) "dbidx3" 
set dbs(3) "dbidx4" 
set dbs(4) "dbidx5" 
set dbs(5) "dbidx6" 
set dbs(6) "dbidx7" 
set dbs(7) "dbidx8" 
set dbs(8) "dbidx9"

set A(0) "A_100"
set A(1) "A_100"
set A(2) "A_100"
set A(3) "A_1000"
set A(4) "A_1000"
set A(5) "A_1000"
set A(6) "A_10000"
set A(7) "A_10000"
set A(8) "A_10000"

set B(0) "B_100_3_0"
set B(1) "B_100_5_0"
set B(2) "B_100_10_0"
set B(3) "B_1000_5_0"
set B(4) "B_1000_10_1"
set B(5) "B_1000_50_1"
set B(6) "B_10000_5_0"
set B(7) "B_10000_50_1"
set B(8) "B_10000_500_1"

spawn mysql --user=admin --password=password
expect "*>"

# drop if already present 
for { set i 0 }  { $i < 9 }  { incr i } {
        send "DROP DATABASE $dbs($i);\n"
        exec sleep 0.0005
        expect "*>"
    }
for { set i 0 }  { $i < 9 }  { incr i } {
        send "CREATE DATABASE IF NOT EXISTS $dbs($i);\n"
        exec sleep 0.0005
        expect "*>"
        send "USE $dbs($i);\n"
        exec sleep 0.0005
        expect "*>"
        send "CREATE TABLE A (A1 INTEGER, A2 VARCHAR(128), PRIMARY KEY(A1));\n"
        exec sleep 0.0005
        expect "*>"
        send "LOAD DATA LOCAL INFILE '../data/$A($i).csv' INTO TABLE A FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n\' IGNORE 1 ROWS (A1,A2);\n"
        exec sleep 0.0005
        expect "*>"
        send "CREATE TABLE B ( B1 INTEGER, B2 INTEGER, B3 VARCHAR(128), PRIMARY KEY(B1), FOREIGN KEY(B2) REFERENCES A (A1), INDEX idx (B3) );\n"
        exec sleep 0.0005
        expect "*>"
        send "LOAD DATA LOCAL INFILE '../data/$B($i).csv' INTO TABLE B FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n\' IGNORE 1 ROWS (B1,B2,B3);\n"
        exec sleep 0.0005
        expect "*>"
    }
send "exit\n"

interact