#!/bin/bash

dbs=( db1 db2 db3 db4 db5 db6 db7 db8 db9 )
A=( A_100 A_100 A_100 A_1000 A_1000 A_1000 A_10000 A_10000 A_10000 )
B=(B_100_3_0 B_100_5_0 B_100_10_0 B_1000_5_0 B_1000_10_1 B_1000_50_1 B_10000_5_0 B_10000_50_1 B_10000_500_1)

for i in {0..8};do 
    mongoimport --type csv -d ${dbs[i]} -c A --headerline --drop ../data/${A[i]}.csv
    mongoimport --type csv -d ${dbs[i]} -c B --headerline --drop ../data/${B[i]}.csv
done


# mongoimport --type csv -d academic -c student --headerline --drop students-header.csv