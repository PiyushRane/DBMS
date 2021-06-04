#!/usr/bin/expect

set dbs(0) "db1" 
set dbs(1) "db2" 
set dbs(2) "db3" 
set dbs(3) "db4" 
set dbs(4) "db5" 
set dbs(5) "db6" 
set dbs(6) "db7" 
set dbs(7) "db8" 
set dbs(8) "db9"

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

spawn mkdir -p dbs
spawn sqlite3

expect "sqlite> "
send ".mode csv\n"
expect "sqlite> "

############### it will show error for 1st row in each file as "INSERT failed: datatype mismatch" ############
###############  due to headers in the file but it will insert all the other rows ############################
for { set i 0 }  { $i < 9 }  { incr i } {
        send ".open ./dbs/$dbs($i)\n"
        exec sleep 0.0005
        expect "sqlite> "
        send "CREATE TABLE A (A1 INTEGER, A2 VARCHAR, PRIMARY KEY(A1));\n"
        exec sleep 0.0005
        expect "sqlite> "
        send ".import ../data/$A($i).csv A \n"
        exec sleep 0.0005
        expect "sqlite> "
        send "CREATE TABLE B ( B1 INTEGER, B2 INTEGER, B3 VARCHAR, PRIMARY KEY(B1), FOREIGN KEY(B2) REFERENCES A (A1) );\n"
        exec sleep 0.0005
        expect "sqlite> "
        send ".import ../data/$B($i).csv B \n"
        exec sleep 0.0005
        expect "sqlite> "
    }
send ".quit\n"

interact