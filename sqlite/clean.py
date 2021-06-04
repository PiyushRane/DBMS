import re

file = open("time.txt")
data = file.read()
clean = re.findall(".*Run.*",data)
# clean = re.findall("([0-9]*\.[0-9]+)",data)

final = []
for a in clean :
    num = re.findall("([0-9]*\.[0-9]+)",a)
    final.append(num)
# print(data)
# print(clean)
# print(final)
# print(len(final))

f1 = open("./time/db1time.csv", "w")
f2 = open("./time/db2time.csv", "w")
f3 = open("./time/db3time.csv", "w")
f4 = open("./time/db4time.csv", "w")
f5 = open("./time/db5time.csv", "w")
f6 = open("./time/db6time.csv", "w")
f7 = open("./time/db7time.csv", "w")
f8 = open("./time/db8time.csv", "w")
f9 = open("./time/db9time.csv", "w")

f = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']

for k in range(4):
    for j in range(7):
        
        f1.write('%.6f' % (float(final[k*63+j*9+0][1])+float(final[k*63+j*9+0][2])))
        if(j is not 6):f1.write(',')

        f2.write('%.6f' % (float(final[k*63+j*9+1][1])+float(final[k*63+j*9+1][2])))
        if(j is not 6):f2.write(',')

        f3.write('%.6f' % (float(final[k*63+j*9+2][1])+float(final[k*63+j*9+2][2])))
        if(j is not 6):f3.write(',')

        f4.write('%.6f' % (float(final[k*63+j*9+3][1])+float(final[k*63+j*9+3][2])))
        if(j is not 6):f4.write(',')

        f5.write('%.6f' % (float(final[k*63+j*9+4][1])+float(final[k*63+j*9+4][2])))
        if(j is not 6):f5.write(',')

        f6.write('%.6f' % (float(final[k*63+j*9+5][1])+float(final[k*63+j*9+5][2])))
        if(j is not 6):f6.write(',')

        f7.write('%.6f' % (float(final[k*63+j*9+6][1])+float(final[k*63+j*9+6][2])))
        if(j is not 6):f7.write(',')

        f8.write('%.6f' % (float(final[k*63+j*9+7][1])+float(final[k*63+j*9+7][2])))
        if(j is not 6):f8.write(',')
        
        f9.write('%.6f' % (float(final[k*63+j*9+8][1])+float(final[k*63+j*9+8][2])))
        if(j is not 6):f9.write(',')
    f1.write('\n')
    f2.write('\n')
    f3.write('\n')
    f4.write('\n')
    f5.write('\n')
    f6.write('\n')
    f7.write('\n')
    f8.write('\n')
    f9.write('\n')

# file = open("clean.csv","w")
# for time in final:
#     file.write(time[0])
#     file.write(',')
#     file.write(time[1])
#     file.write(',')
#     file.write(time[2])
#     file.write('\n')
# file.close()