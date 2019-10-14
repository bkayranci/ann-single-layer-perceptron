# turkalp burak kayrancioglu - 150101011

import matplotlib.pyplot as plt
import numpy as np
import random

dataset_file = 'dataset.csv'
loop_timeout = 0.05 # yavaslatmak icin degeri buyutun, grafigin yenileme dongusunun suresi

# yol agirliklari
w = [0, 0]

# esik degeri
threshold = 0

# bias
bias = 1

# ogrenme orani
learning_rate = 1

# maksimum iterasyon
max_iterations = 100

# verileri oku
import csv
data = []
data_dictionary = {}
with open(dataset_file, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(list([float(i) for i in row.values()]))
        data_dictionary['{},{}'.format(row.get('x'), row.get('y'))] = row.get('z')

y = 0

color = ""

answer = ""

def get_points_of_color(data, label):
    x_coords = [float(point.split(",")[0]) for point in data.keys() if data[point] == label]
    y_coords = [float(point.split(",")[1]) for point in data.keys() if data[point] == label]
    return x_coords, y_coords

# mathplotlib ile ilgili bisey
plt.ion()

for k in range(1, max_iterations):
    hits = 0
    print("\n========================= ADIM: "+str(k)+" ========================= ")

    for i in range(0,len(data)):
        sum = 0

        # agirliklar toplami
        for j in range(0,len(data[i])-1):
            sum += data[i][j] * w[j]

        # bias ekle
        output = bias + sum

        if output > threshold:
            y = 1
        else:
            y = -1     

        if y == data[i][2]:
            hits += 1
            answer = "dogru"
        else:
            for j in range (0,len(w)):             
                w[j] = w[j] + (learning_rate * data[i][2] * data[i][j])
            bias = bias + learning_rate * data[i][2]
            answer = "hata - agirlik hesapla: "+str(w)

        # sonuc yaz
        if y == 1:
            print("\n"+answer)
        elif y == -1:
            print("\n"+answer)

        plt.clf() # temizle
        plt.title('adim %s\n' % (str(k)))
        plt.grid(False)
        plt.xlim(-1,1)
        plt.ylim(-1,1)

        xA = 1
        xB = -1

        if w[1] != 0:
            yA = (- w[0] * xA - bias) / w[1]
            yB = (- w[0] * xB - bias) / w[1]
        else:
            xA = - bias / w[0]
            xB = - bias / w[0]

            yA = 1
            yB = -1

        plt.plot([0.77, -0.55], [-1, 1], color='k', linestyle='-', linewidth=1)
        plt.plot([xA, xB], [yA, yB], color='g', linestyle='-', linewidth=2)

        
        x_coords, y_coords = get_points_of_color(data_dictionary, '-1')
        plt.plot(x_coords, y_coords, 'bo')

        x_coords, y_coords = get_points_of_color(data_dictionary, '1')
        plt.plot(x_coords, y_coords, 'ro')

        if answer == 'dogru':
            # dogru
            plt.plot(data[i][0], data[i][1], 'go', markersize=15, alpha=.5)
        else:
            # hatali
            plt.plot(data[i][0], data[i][1], 'mo', markersize=30, alpha=.5)
        plt.show()

        # bekle
        plt.pause(loop_timeout)

    if hits == len(data):
        print("\n===============================================================")
        print("\n"+str(k)+" adimda ogrenildi!")
        break
