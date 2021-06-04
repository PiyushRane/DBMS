#!/bin/bash

dbs=( db1 db2 db3 db4 db5 db6 db7 db8 db9 )

q1="SELECT * FROM A WHERE A1 <= 50;\n"
q2="SELECT * FROM B ORDER BY B3;\n"
q3="SELECT AVG(sum) FROM (SELECT COUNT(B1) AS sum FROM B GROUP BY B2) AS new;\n"
q4="SELECT B1,B2,B3,A2 FROM B JOIN A ON A.A1 = B.B2;\n"

# delete the t1.txt t2.txt t3.txt t4.txt file otherwise it wil append to previous output
rm t?.txt

# create time folder to store time systematically
mkdir -p "time"

# query 1
for j in {0..6}; do
    for i in {0..8}; do
        mysql --user=admin --password=password -vvv -e "RESET QUERY CACHE; SET PROFILING = 1; $q1 SHOW PROFILES;" ${dbs[i]} | grep "FROM" >> "t1.txt"
    done
done

# query 2
for j in {0..6}; do
    for i in {0..8}; do
        mysql --user=admin --password=password -vvv -e "RESET QUERY CACHE; SET PROFILING = 1; $q2 SHOW PROFILES;" ${dbs[i]} | grep "FROM" >> "t2.txt"
    done
done

# query 3
for j in {0..6}; do
    for i in {0..8}; do
        mysql --user=admin --password=password -vvv -e "RESET QUERY CACHE; SET PROFILING = 1; $q3 SHOW PROFILES;" ${dbs[i]} | grep "FROM" >> "t3.txt"
    done
done

# query 4
for j in {0..6}; do
    for i in {0..8}; do
        mysql --user=admin --password=password -vvv -e "RESET QUERY CACHE; SET PROFILING = 1; $q4 SHOW PROFILES;" ${dbs[i]} | grep "FROM" >> "t4.txt"
    done
done