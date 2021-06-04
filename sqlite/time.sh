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

set q1 "SELECT * FROM A WHERE A1 <= 50;\n"
set q2 "SELECT * FROM B ORDER BY B3;\n"
set q3 "SELECT AVG(sum) FROM (SELECT COUNT(B1) AS sum FROM B GROUP BY B2);\n"
set q4 "SELECT B1,B2,B3,A2 FROM B JOIN A ON A.A1 = B.B2;\n"

spawn mkdir -p query
spawn mkdir -p "time"
spawn sqlite3
expect "sqlite> "
send ".timer ON\n"
expect "sqlite> "

#query 1
for { set j 0 }  { $j < 7 }  { incr j } {
    for { set i 0 }  { $i < 9 }  { incr i } {
        send ".output ./query/$dbs($i)query_1.txt\n"
        exec sleep 0.001
        expect "sqlite> "
        send ".open ./dbs/$dbs($i)\n"
        exec sleep 0.001
        expect "sqlite> "
        send $q1
        exec sleep 0.001
        expect "sqlite> "
    }
}

#query 2
for { set j 0 }  { $j < 7 }  { incr j } {
    for { set i 0 }  { $i < 9 }  { incr i } {
        send ".output ./query/$dbs($i)query_2.txt\n"
        exec sleep 0.001
        expect "sqlite> "
        send ".open ./dbs/$dbs($i)\n"
        exec sleep 0.001
        expect "sqlite> "
        send $q2
        exec sleep 0.001
        expect "sqlite> "
    }
}

#query 3
for { set j 0 }  { $j < 7 }  { incr j } {
    for { set i 0 }  { $i < 9 }  { incr i } {
        send ".output ./query/$dbs($i)query_3.txt\n"
        exec sleep 0.001
        expect "sqlite> "
        send ".open ./dbs/$dbs($i)\n"
        exec sleep 0.001
        expect "sqlite> "
        send $q3
        exec sleep 0.001
        expect "sqlite> "
    }
}

#query 4
for { set j 0 }  { $j < 7 }  { incr j } {
    for { set i 0 }  { $i < 9 }  { incr i } {
        send ".output ./query/$dbs($i)query_4.txt\n"
        exec sleep 0.001
        expect "sqlite> "
        send ".open ./dbs/$dbs($i)\n"
        exec sleep 0.001
        expect "sqlite> "
        send $q4
        exec sleep 0.001
        expect "sqlite> "
    }
}
send ".quit\n"

interact