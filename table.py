import pandas as pd
import csv
import matplotlib as plot

############################# sqlite #################################################
s = []
for i in range(1,10):
    with open("./sqlite/time/db" + str(i) + "time.csv") as f:
        data = csv.reader(f,quoting = csv.QUOTE_NONNUMERIC)
        for row in data:
            s.append(row)
filter = []
for row in s:
    row.sort()
    filter.append(row[1:-1])            # drop the min and maximum and take only 5 values for avg and std

avg = []
dev = []
for row in filter:
    avg.append(pd.Series(row).mean())
    dev.append(pd.Series(row).std())

# print(len(avg))
# print(len(dev))

adf1 = pd.DataFrame({
    'db1' : avg[:4],
    'db2' : avg[4:8],
    'db3' : avg[8:12],
    'db4' : avg[12:16],
    'db5' : avg[16:20],
    'db6' : avg[20:24],
    'db7' : avg[24:28],
    'db8' : avg[28:32],
    'db9' : avg[32:]
},
    index = ["query1", "query2", "query3", "query4"])

sdf1 = pd.DataFrame({
    'db1' : dev[:4],
    'db2' : dev[4:8],
    'db3' : dev[8:12],
    'db4' : dev[12:16],
    'db5' : dev[16:20],
    'db6' : dev[20:24],
    'db7' : dev[24:28],
    'db8' : dev[28:32],
    'db9' : dev[32:]
},
    index = ["query1", "query2", "query3", "query4"])

sqldf1 = pd.DataFrame({
    'db1' : avg[0],
    'db2' : avg[4],
    'db3' : avg[8],
    'db4' : avg[12],
    'db5' : avg[16],
    'db6' : avg[20],
    'db7' : avg[24],
    'db8' : avg[28],
    'db9' : avg[32]
},index=['Sqlite'])
sqldf2 = pd.DataFrame({
    'db1' : avg[1],
    'db2' : avg[5],
    'db3' : avg[9],
    'db4' : avg[13],
    'db5' : avg[17],
    'db6' : avg[21],
    'db7' : avg[25],
    'db8' : avg[29],
    'db9' : avg[33]
},index=['Sqlite'])
sqldf3 = pd.DataFrame({
    'db1' : avg[2],
    'db2' : avg[6],
    'db3' : avg[10],
    'db4' : avg[14],
    'db5' : avg[18],
    'db6' : avg[22],
    'db7' : avg[26],
    'db8' : avg[30],
    'db9' : avg[34]
},index=['Sqlite'])
sqldf4 = pd.DataFrame({
    'db1' : avg[3],
    'db2' : avg[4],
    'db3' : avg[11],
    'db4' : avg[15],
    'db5' : avg[19],
    'db6' : avg[23],
    'db7' : avg[27],
    'db8' : avg[31],
    'db9' : avg[35]
},index=['Sqlite'])

# print(adf1)
# print(sdf1)

############################################# maria (index) #######################################3
s = []
for i in range(1,10):
    with open("./maria_with_index/time/db" + str(i) + "time.csv") as f:
        data = csv.reader(f,quoting = csv.QUOTE_NONNUMERIC)
        for row in data:
            s.append(row)
filter = []
for row in s:
    row.sort()
    filter.append(row[1:-1])

# print(pd.Series(filter[0]).mean())

avg = []
dev = []
for row in filter:
    avg.append(pd.Series(row).mean())
    dev.append(pd.Series(row).std())

# print(len(avg))
# print(len(dev))

adf2 = pd.DataFrame({
    'db1' : avg[:4],
    'db2' : avg[4:8],
    'db3' : avg[8:12],
    'db4' : avg[12:16],
    'db5' : avg[16:20],
    'db6' : avg[20:24],
    'db7' : avg[24:28],
    'db8' : avg[28:32],
    'db9' : avg[32:]
},
    index = ["query1", "query2", "query3", "query4"])

sdf2 = pd.DataFrame({
    'db1' : dev[:4],
    'db2' : dev[4:8],
    'db3' : dev[8:12],
    'db4' : dev[12:16],
    'db5' : dev[16:20],
    'db6' : dev[20:24],
    'db7' : dev[24:28],
    'db8' : dev[28:32],
    'db9' : dev[32:]
},
    index = ["query1", "query2", "query3", "query4"])

mariadf1 = pd.DataFrame({
    'db1' : avg[0],
    'db2' : avg[4],
    'db3' : avg[8],
    'db4' : avg[12],
    'db5' : avg[16],
    'db6' : avg[20],
    'db7' : avg[24],
    'db8' : avg[28],
    'db9' : avg[32]
},index=['Maria (index)'])
mariadf2 = pd.DataFrame({
    'db1' : avg[1],
    'db2' : avg[5],
    'db3' : avg[9],
    'db4' : avg[13],
    'db5' : avg[17],
    'db6' : avg[21],
    'db7' : avg[25],
    'db8' : avg[29],
    'db9' : avg[33]
},index=['Maria (index)'])
mariadf3 = pd.DataFrame({
    'db1' : avg[2],
    'db2' : avg[6],
    'db3' : avg[10],
    'db4' : avg[14],
    'db5' : avg[18],
    'db6' : avg[22],
    'db7' : avg[26],
    'db8' : avg[30],
    'db9' : avg[34]
},index=['Maria (index)'])
mariadf4 = pd.DataFrame({
    'db1' : avg[3],
    'db2' : avg[4],
    'db3' : avg[11],
    'db4' : avg[15],
    'db5' : avg[19],
    'db6' : avg[23],
    'db7' : avg[27],
    'db8' : avg[31],
    'db9' : avg[35]
},index=['Maria (index)'])

# print(adf2)
# print(sdf2)

############################################## maria(no idx) ##################################################
s = []
for i in range(1,10):
    with open("./maria_without_index/time/db" + str(i) + "time.csv") as f:
        data = csv.reader(f,quoting = csv.QUOTE_NONNUMERIC)
        for row in data:
            s.append(row)
filter = []
for row in s:
    row.sort()
    filter.append(row[1:-1])

# print(pd.Series(filter[0]).mean())

avg = []
dev = []
for row in filter:
    avg.append(pd.Series(row).mean())
    dev.append(pd.Series(row).std())

# print(len(avg))
# print(len(dev))

adf3 = pd.DataFrame({
    'db1' : avg[:4],
    'db2' : avg[4:8],
    'db3' : avg[8:12],
    'db4' : avg[12:16],
    'db5' : avg[16:20],
    'db6' : avg[20:24],
    'db7' : avg[24:28],
    'db8' : avg[28:32],
    'db9' : avg[32:]
},
    index = ["query1", "query2", "query3", "query4"])

sdf3 = pd.DataFrame({
    'db1' : dev[:4],
    'db2' : dev[4:8],
    'db3' : dev[8:12],
    'db4' : dev[12:16],
    'db5' : dev[16:20],
    'db6' : dev[20:24],
    'db7' : dev[24:28],
    'db8' : dev[28:32],
    'db9' : dev[32:]
},
    index = ["query1", "query2", "query3", "query4"])

maria_nodf1 = pd.DataFrame({
    'db1' : avg[0],
    'db2' : avg[4],
    'db3' : avg[8],
    'db4' : avg[12],
    'db5' : avg[16],
    'db6' : avg[20],
    'db7' : avg[24],
    'db8' : avg[28],
    'db9' : avg[32]
},index=['Maria (no idx)'])
maria_nodf2 = pd.DataFrame({
    'db1' : avg[1],
    'db2' : avg[5],
    'db3' : avg[9],
    'db4' : avg[13],
    'db5' : avg[17],
    'db6' : avg[21],
    'db7' : avg[25],
    'db8' : avg[29],
    'db9' : avg[33]
},index=['Maria (no idx)'])
maria_nodf3 = pd.DataFrame({
    'db1' : avg[2],
    'db2' : avg[6],
    'db3' : avg[10],
    'db4' : avg[14],
    'db5' : avg[18],
    'db6' : avg[22],
    'db7' : avg[26],
    'db8' : avg[30],
    'db9' : avg[34]
},index=['Maria (no idx)'])
maria_nodf4 = pd.DataFrame({
    'db1' : avg[3],
    'db2' : avg[4],
    'db3' : avg[11],
    'db4' : avg[15],
    'db5' : avg[19],
    'db6' : avg[23],
    'db7' : avg[27],
    'db8' : avg[31],
    'db9' : avg[35]
},index=['Maria (no idx)'])

# print(adf3)
# print(sdf3)

################################################# mongo ###################################################
s = []
for i in range(1,10):
    with open("./mongo/time/db" + str(i) + "time.csv") as f:
        data = csv.reader(f,quoting = csv.QUOTE_NONNUMERIC)
        for row in data:
            s.append(row)
filter = []
for row in s:
    row.sort()
    filter.append(row[1:-1])

# print(pd.Series(filter[0]).mean())

avg = []
dev = []
for row in filter:
    avg.append(pd.Series(row).mean())
    dev.append(pd.Series(row).std())

# print(len(avg))
# print(len(dev))

adf4 = pd.DataFrame({
    'db1' : avg[:4],
    'db2' : avg[4:8],
    'db3' : avg[8:12],
    'db4' : avg[12:16],
    'db5' : avg[16:20],
    'db6' : avg[20:24],
    'db7' : avg[24:28],
    'db8' : avg[28:32],
    'db9' : avg[32:]
},
    index = ["query1", "query2", "query3", "query4"])

sdf4 = pd.DataFrame({
    'db1' : dev[:4],
    'db2' : dev[4:8],
    'db3' : dev[8:12],
    'db4' : dev[12:16],
    'db5' : dev[16:20],
    'db6' : dev[20:24],
    'db7' : dev[24:28],
    'db8' : dev[28:32],
    'db9' : dev[32:]
},
    index = ["query1", "query2", "query3", "query4"])

mdf1 = pd.DataFrame({
    'db1' : avg[0],
    'db2' : avg[4],
    'db3' : avg[8],
    'db4' : avg[12],
    'db5' : avg[16],
    'db6' : avg[20],
    'db7' : avg[24],
    'db8' : avg[28],
    'db9' : avg[32]
},index=['MongoDB'])
mdf2 = pd.DataFrame({
    'db1' : avg[1],
    'db2' : avg[5],
    'db3' : avg[9],
    'db4' : avg[13],
    'db5' : avg[17],
    'db6' : avg[21],
    'db7' : avg[25],
    'db8' : avg[29],
    'db9' : avg[33]
},index=['MongoDB'])
mdf3 = pd.DataFrame({
    'db1' : avg[2],
    'db2' : avg[6],
    'db3' : avg[10],
    'db4' : avg[14],
    'db5' : avg[18],
    'db6' : avg[22],
    'db7' : avg[26],
    'db8' : avg[30],
    'db9' : avg[34]
},index=['MongoDB'])
mdf4 = pd.DataFrame({
    'db1' : avg[3],
    'db2' : avg[4],
    'db3' : avg[11],
    'db4' : avg[15],
    'db5' : avg[19],
    'db6' : avg[23],
    'db7' : avg[27],
    'db8' : avg[31],
    'db9' : avg[35]
},index=['MongoDB'])

# print(adf4)
# print(sdf4)

############################## Tables as html and csv ###################################################

adf = pd.concat([adf1, adf2, adf3, adf4], keys = ['Sqlite', 'Maria(index)', 'Maria(no index)', 'MongoDB'])
sdf = pd.concat([sdf1, sdf2, sdf3, sdf4], keys = ['Sqlite', 'Maria(index)', 'Maria(no index)', 'MongoDB'])
print("Average Table")
print(adf)
print("\nStd Table")
print(sdf)

adf.to_html('avg.html')
sdf.to_html('std.html')

adf.to_csv('avg.csv')
sdf.to_csv('std.csv')

############################## Plots ############################################################

q1df = pd.concat([sqldf1,mariadf1,maria_nodf1,mdf1])
q2df = pd.concat([sqldf2,mariadf2,maria_nodf2,mdf2])
q3df = pd.concat([sqldf3,mariadf3,maria_nodf3,mdf3])
q4df = pd.concat([sqldf4,mariadf4,maria_nodf4,mdf4])

# print(q1df)
# print(q2df)
# print(q3df)
# print(q4df)

adf1.T.plot()
plot.pyplot.title("Time vs Database of Sqlite")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/sqlite.png')

adf2.T.plot()
plot.pyplot.title("Time vs Database of Maria (index)")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/maria_idx.png')

adf3.T.plot()
plot.pyplot.title("Time vs Database of Maria (no idx)")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/maria_noidx.png')

adf4.T.plot()
plot.pyplot.title("Time vs Database of MongoDB")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/mongo.png')

q1df.T.plot()
plot.pyplot.title("Time vs Database System for Query 1")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/q1.png')

q2df.T.plot()
plot.pyplot.title("Time vs Database System for Query 2")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/q2.png')

q3df.T.plot()
plot.pyplot.title("Time vs Database System for Query 3")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/q3.png')

q4df.T.plot()
plot.pyplot.title("Time vs Database System for Query 4")
plot.pyplot.ylabel("Time (s)")
plot.pyplot.savefig('./plots/q4.png')

# plot.pyplot.show()