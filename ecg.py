import csv

with open('ppp', "r") as f:
    datas = f.readline()
    qwq = datas.replace('22 02', 'EF FE').replace('22 01', 'FE EF').replace('22 00', '22')
    a = qwq.split(' ')

ecg = {}
mecg = {}
times = 0

for i in range(0, len(a)):
    if a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '00':
        if a[i+16] == '01':
            for j in range(0, 100, 2):
                if a[i+21+j+1] == '00':
                    ecg[times*50+j/2] = str(int(a[i+21+j], 16))
                if a[i+21+j+1] == 'FF':
                    ecg[times*50+j/2] = '-' + str(int('FF',16) - int(a[i+21+j], 16))
            times += 1

def WriteCsv(file_name, datalist):
    with open(file_name, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in datalist:
            writer.writerow([datalist[row]])

WriteCsv('ecg_data.csv', ecg)

# print(ecg)
# print(len(ecg))