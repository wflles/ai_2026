import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from scipy import stats

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
        ret.append(float(row[index + 1]))

    ret.sort()

    return ret


def calculate_mean(data):
    sum = 0
    length = len(data)
    for i in data:
        sum = sum + int(i)
    return sum / length

def calculate_variance(data):
    mean = calculate_mean(data)
    sum = 0
    length = len(data) - 1
    for i in data:
        sum = (int(i) - mean)**2
    return sum / length

def show_black_px_per_rows(living_objects, nonliving_objects):
    colors = ['red', 'tan']
    names = ['living', 'non-living']
    fig, axes = plt.subplots(nrows=1, ncols=3)

    ax0 = axes[0]
    ax1 = axes[1]
    ax2 = axes[2]

    #nr_pix_w_1 
    val = []

    val.append(isolate_feature_by_index(2, living_objects))
    val.append(isolate_feature_by_index(2, nonliving_objects))

    ax0.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax0.legend(prop={'size': 10})
    ax0.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax0.tick_params(axis='x', labelrotation=90) 
    ax0.set_title("One black pixel per row")

    #nr_pix_w_2

    val = []

    val.append(isolate_feature_by_index(4, living_objects))
    val.append(isolate_feature_by_index(4, nonliving_objects))

    ax1.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax1.legend(prop={'size': 10})
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax1.tick_params(axis='x', labelrotation=90) 
    ax1.set_title("Two black pixel per row")

    #nr_pix_w_ 3
    val = []

    val.append(isolate_feature_by_index(6, living_objects))
    val.append(isolate_feature_by_index(6, nonliving_objects))

    ax2.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax2.legend(prop={'size': 10})
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax2.tick_params(axis='x', labelrotation=90) 
    ax2.set_title("Three or more black pixel per row")

    plt.show()

def show_black_px_per_col(living_objects, non_living_objects):
    colors = ['red', 'tan']
    names = ['living', 'non-living']

    fig, axes = plt.subplots(nrows=1, ncols=3)

    ax0 = axes[0]
    ax1 = axes[1]
    ax2 = axes[2]

    #nr_pix_w_1 
    val = []

    val.append(isolate_feature_by_index(3, living_objects))
    val.append(isolate_feature_by_index(3, nonliving_objects))

    ax0.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax0.legend(prop={'size': 10})
    ax0.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax0.tick_params(axis='x', labelrotation=90) 
    ax0.set_title("One black pixel per col")

    val = []

    val.append(isolate_feature_by_index(5, living_objects))
    val.append(isolate_feature_by_index(5, nonliving_objects))

    ax1.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax1.legend(prop={'size': 10})
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax1.tick_params(axis='x', labelrotation=90) 
    ax1.set_title("Two black pixel per col")

    #nr_pix_w_ 3
    val = []

    val.append(isolate_feature_by_index(7, living_objects))
    val.append(isolate_feature_by_index(7, nonliving_objects))

    ax2.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    ax2.legend(prop={'size': 10})
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax2.tick_params(axis='x', labelrotation=90) 
    ax2.set_title("Three or more black pixel per col")

    plt.show()

def show_hollow_eyes_con_areas(living_objects, non_living_objects):
    val = []

    colors = ['red', 'tan']
    names = ['living', 'non-living']

    fig, axes = plt.subplots(nrows=1, ncols=3)

    ax0 = axes[0]
    ax1 = axes[1]
    ax2 = axes[2]

    #nr_pix_w_1 
    val = []

    val.append(isolate_feature_by_index(13, living_objects))
    val.append(isolate_feature_by_index(13, nonliving_objects))

    ax0.hist(val, bins = 4, density=True, histtype='bar', color=colors, label=names)
    ax0.legend(prop={'size': 10})
    ax0.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax0.tick_params(axis='x', labelrotation=90) 
    ax0.set_title("Connected areas")

    val = []

    val.append(isolate_feature_by_index(14, living_objects))
    val.append(isolate_feature_by_index(14, nonliving_objects))

    ax1.hist(val, bins = 4, density=True, histtype='bar', color=colors, label=names)
    ax1.legend(prop={'size': 10})
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax1.tick_params(axis='x', labelrotation=90) 
    ax1.set_title("Eyes")

    val = []

    val.append(isolate_feature_by_index(15, living_objects))
    val.append(isolate_feature_by_index(15, nonliving_objects))

    ax2.hist(val, bins = 4, density=True, histtype='bar', color=colors, label=names)
    ax2.legend(prop={'size': 10})
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax2.tick_params(axis='x', labelrotation=90) 
    ax2.set_title("Hollowness")

    plt.show()

def task_3_1(living_objects, nonliving_objects, csv_stored):

    colors = ['red', 'tan', 'lime']
    names = ['living', 'non-living', 'all']

    #nr_pix 
    val = []

    val.append(isolate_feature_by_index(1, living_objects))
    val.append(isolate_feature_by_index(1, nonliving_objects))
    val.append(isolate_feature_by_index(1, csv_stored))

    plt.figure()
    plt.hist(val, bins = 8, density=True, histtype='bar', color=colors, label=names)
    plt.legend(prop={'size': 10})
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=50))
    plt.tick_params(axis='x', labelrotation=90) 

    #height
    val = []

    val.append(isolate_feature_by_index(8, living_objects))
    val.append(isolate_feature_by_index(8, nonliving_objects))
    val.append(isolate_feature_by_index(8, csv_stored))

    plt.figure()
    plt.hist(val, bins = 8, density=True, histtype='bar', color=colors, label=names)
    plt.legend(prop={'size': 10})
    plt.tick_params(axis='x', labelrotation=90) 

    #width

    val = []

    val.append(isolate_feature_by_index(9, living_objects))
    val.append(isolate_feature_by_index(9, nonliving_objects))
    val.append(isolate_feature_by_index(9, csv_stored))

    plt.figure()
    plt.hist(val, bins = 8, density=True, histtype='bar', color=colors, label=names)
    plt.legend(prop={'size': 10})
    plt.tick_params(axis='x', labelrotation=90) 

    #aspect ratio

    val = []

    val.append(isolate_feature_by_index(10, living_objects))
    val.append(isolate_feature_by_index(10, nonliving_objects))
    val.append(isolate_feature_by_index(10, csv_stored))

    plt.figure()
    plt.hist(val, bins = 8, density=True, histtype='bar', color=colors, label=names)
    plt.legend(prop={'size': 10})
    plt.tick_params(axis='x', labelrotation=90) 
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=20))
    plt.show()

def task_3_2(csv_stored):
    variance = calculate_variance(isolate_feature_by_index(1, csv_stored))
    mean = calculate_mean(isolate_feature_by_index(1, csv_stored))

    sigma = np.sqrt(variance)
    x = np.linspace(mean - 3*sigma, mean + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mean, sigma))
    plt.show()

def task_3_3(csv_stored):
    percentile = stats.norm.ppf(0.95, calculate_mean(isolate_feature_by_index(1, csv_stored)), calculate_variance(isolate_feature_by_index(1, csv_stored)))
    print(f"TASK 3.3: {percentile}")

def task_3_4(csv_stored, living_objects, nonliving_objects):

    #barcharts for pix
    show_black_px_per_rows(living_objects, nonliving_objects)
    show_black_px_per_rows(living_objects, nonliving_objects)
    show_hollow_eyes_con_areas(living_objects, nonliving_objects)

def myfunc(x):
  return slope * x + intercept

with open("../../40437373_features.csv", mode ='r')as file:
          csvFile = csv.reader(file)
          for row in csvFile:
              tmp = []
              for num in row:
                      tmp.append(num)
              csv_stored.append(tmp)


living_objects = find_living_obj(csv_stored)
nonliving_objects = find_nonliving_obj(csv_stored)

##task 3.1
# task_3_1(living_objects, nonliving_objects, csv_stored)

# #task 3.2
# task_3_2(csv_stored)

# #task 3.3.
# task_3_3(csv_stored)

#task 3.4(living_objects, nonliving_objects)

len = 14
for i in range(len):
    for j in range(len):
        x = isolate_feature_by_index(i, nonliving_objects)
        y = isolate_feature_by_index(j, nonliving_objects)
        if(x == y):
            break
        try:
            slope, intercept, r, p, std_err = stats.linregress(x, y)
        except:
            print("unable to calculate: " + str(i) + " + " + str(j))
            break
        print("r value of {" + str(i + 1) + "-" + str(j + 1) + "} = " + str(r))
        





# mymodel = list(map(myfunc, x))
# print(r)
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

