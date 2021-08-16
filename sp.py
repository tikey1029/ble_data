import csv

with open('spo2_5min', "r") as f:
    datas = f.readline()
    qwq = datas.replace('22 02', 'EF FE').replace('22 01', 'FE EF').replace('22 00', '22')
    a = qwq.split(' ')

spo2 = {}
times = 0

for i in range(0, len(a)):
    if a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '01':
        if a[i+126] == '0B':
            for j in range(0, 24):
                spo2[j+times*24] = a[i+128+j]
            times += 1

for tt in range(0, 24):
    print(spo2[tt])
# print(len(spo2))

# def WriteCsv(file_name, datalist):
#     with open(file_name, 'a+', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         for row in datalist:
#             writer.writerow([datalist[row]])
#
# WriteCsv('red_ired_data_5min.csv', spo2)

with open('red_ired_5min.txt', 'a+') as f:
    for lens in range(0, len(spo2)):
        f.write(spo2[lens])
        f.write('\n')