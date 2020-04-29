import scipy.io as scio
import os
import time

dataFile = r'D:\Code\Python\data\BITVehicle_Dataset\VehicleInfo.mat'
target_path = r'D:\Code\Python\data\BITVehicle_Dataset\txt_with_name'

if not os.path.exists(target_path):
    os.mkdir(target_path)

data = scio.loadmat(dataFile)
for i in data['VehicleInfo']:
    time.sleep(0.001)
    txt_file = i[0][0][0].split('.')[0] + '.txt'
    # os.mknod("txt_1/" + txt_file)
    file = os.path.join(target_path, txt_file)

    fp = open(file, 'w')
    #
    # a = i[0]
    # b = i[0][4]
    # c = i[0][4][0]
    # d = i[0][4][0][0]
    #
    # print(a)

    if int(i[0][4][0][0]) == 1:
        line = str(i[0][3][0][0][0][0][0]) + ' ' + str(i[0][3][0][0][1][0][0]) + ' ' + str(
            i[0][3][0][0][2][0][0]) + ' ' + str(i[0][3][0][0][3][0][0]) + ' ' + str(i[0][3][0][0][4][0])
        fp.write(line)
        fp.close()
    elif int(i[0][4][0][0]) == 2:
        line = str(i[0][3][0][0][0][0][0]) + ' ' + str(i[0][3][0][0][1][0][0]) + ' ' + str(
            i[0][3][0][0][2][0][0]) + ' ' + str(i[0][3][0][0][3][0][0]) + ' ' + str(i[0][3][0][0][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][1][0][0][0]) + ' ' + str(i[0][3][0][1][1][0][0]) + ' ' + str(
            i[0][3][0][1][2][0][0]) + ' ' + str(i[0][3][0][1][3][0][0]) + ' ' + str(i[0][3][0][1][4][0])
        fp.write(line)
        fp.close()
    elif int(i[0][4][0][0]) == 3:
        line = str(i[0][3][0][0][0][0][0]) + ' ' + str(i[0][3][0][0][1][0][0]) + ' ' + str(
            i[0][3][0][0][2][0][0]) + ' ' + str(i[0][3][0][0][3][0][0]) + ' ' + str(i[0][3][0][0][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][1][0][0][0]) + ' ' + str(i[0][3][0][1][1][0][0]) + ' ' + str(
            i[0][3][0][1][2][0][0]) + ' ' + str(i[0][3][0][1][3][0][0]) + ' ' + str(i[0][3][0][1][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][2][0][0][0]) + ' ' + str(i[0][3][0][2][1][0][0]) + ' ' + str(
            i[0][3][0][2][2][0][0]) + ' ' + str(i[0][3][0][2][3][0][0]) + ' ' + str(i[0][3][0][2][4][0])
        fp.write(line)
        fp.close()
    elif int(i[0][4][0][0]) == 4:
        line = str(i[0][3][0][0][0][0][0]) + ' ' + str(i[0][3][0][0][1][0][0]) + ' ' + str(
            i[0][3][0][0][2][0][0]) + ' ' + str(i[0][3][0][0][3][0][0]) + ' ' + str(i[0][3][0][0][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][1][0][0][0]) + ' ' + str(i[0][3][0][1][1][0][0]) + ' ' + str(
            i[0][3][0][1][2][0][0]) + ' ' + str(i[0][3][0][1][3][0][0]) + ' ' + str(i[0][3][0][1][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][2][0][0][0]) + ' ' + str(i[0][3][0][2][1][0][0]) + ' ' + str(
            i[0][3][0][2][2][0][0]) + ' ' + str(i[0][3][0][2][3][0][0]) + ' ' + str(i[0][3][0][2][4][0]) + '\n'
        fp.write(line)
        line = str(i[0][3][0][3][0][0][0]) + ' ' + str(i[0][3][0][3][1][0][0]) + ' ' + str(
            i[0][3][0][3][2][0][0]) + ' ' + str(i[0][3][0][3][3][0][0]) + ' ' + str(i[0][3][0][3][4][0]) + '\n'
        fp.write(line)
        fp.close()
    else:
        print(i[0][0][0])
