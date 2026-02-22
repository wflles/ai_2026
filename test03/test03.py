import csv
import matplotlib.pyplot as plt
import numpy as np

living_obj = ["cherry", "tree", "banana", "lemon"]

nonliving_obj = ["envelope", "golfclub", "pencil", "wineglass"]

csv_stored = []
living_objects = []
nonliving_obects = []

def find_living_obj(obj):
    lvn_obj = []
    for i in range(56):
        row = []
        row = obj[i]
        temp = []
        for i in row:
               temp.append(i)
        lvn_obj.append(temp)
 
    return lvn_obj

def find_nonliving_obj(obj):
    lvn_obj = []
    for i in range(56):
        row = []
        row = obj[i + 56]
        temp = []
        for i in row:
               temp.append(i)
        lvn_obj.append(temp)
 
    return lvn_obj

def isolate_feature_by_index(index, obj):
    ret = []
    for row in obj:
        ret.append(row[index + 1])
    return ret


with open("../../40437373_features.csv", mode ='r')as file:
          csvFile = csv.reader(file)
          for row in csvFile:
              tmp = []
              for num in row:
                      tmp.append(num)
              csv_stored.append(tmp)


#histogram variables
living_objects = find_living_obj(csv_stored)
nonliving_objects = find_nonliving_obj(csv_stored)

colors = ['red', 'tan', 'lime']
names = ['living', 'non-living', 'all']

#nr_pix 
val = []

val.append(isolate_feature_by_index(1, living_objects))
val.append(isolate_feature_by_index(1, nonliving_objects))
val.append(isolate_feature_by_index(1, csv_stored))

plt.hist(val, bins = 8, density=True, histtype='bar', color=colors, label=names)
plt.legend(prop={'size': 10})
plt.tick_params(axis='x', labelrotation=90) 
plt.show()


