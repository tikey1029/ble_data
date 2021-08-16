import csv

with open('06170947', "r") as f:
    datas = f.readline()
    qwq = datas.replace('22 02', 'EF FE').replace('22 01', 'FE EF').replace('22 00', '22')
    a = qwq.split(' ')

eeg1 = {}
times1 = 0

for i in range(0, len(a)):
    if a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '01':
        if a[i+16] == '06':
            for j in range(0, 20, 2):
                eeg1[times1*10+j/2] = str(int(a[i+18+j+1] + a[i+18+j], 16))
            times1 += 1

def WriteCsv(file_name, datalist):
    with open(file_name, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in datalist:
            writer.writerow([datalist[row]])

WriteCsv('eeg1_data.csv', eeg1)
