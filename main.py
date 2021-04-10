import numpy as np

flowdata = np.genfromtxt('TP_Link_Plug_flowstats.csv', dtype='int64', delimiter=',')

attacks = np.genfromtxt('TP_Link_Plug.csv', dtype="int64", delimiter=',')
attack_num = len(attacks)

thou = 1000
length = len(flowdata)
print(length)
print(attack_num)

labels = np.empty((length, 2), dtype='int', order='C')


def add_me(stat, id):
    ind = id - 1
    labels[ind, 0] = id
    labels[ind, 1] = stat


def check_time(num):
    for j in range(attack_num):
        start_time = attacks[j, 0] * thou
        end_time = attacks[j, 1] * thou
        if start_time <= num <= end_time:
            return 1
    return 0


for i in range(length):
    status = check_time(flowdata[i, 1])
    add_me(status, flowdata[i, 0])


np.savetxt("tp_link_plug_labels.txt", labels, fmt='%d', delimiter="\t")
