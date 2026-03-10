import csv
from pickle import OBJ
from matplotlib.pylab import f
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import statistics
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import r2_score
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

def show_clusters(living_objects, non_living_objects):
    val = []

    colors = ['red', 'tan']
    names = ['living', 'non-living']

    fig, axes = plt.subplots(nrows=1, ncols=1)
    val.append(isolate_feature_by_index(16, living_objects))
    val.append(isolate_feature_by_index(16, non_living_objects))

    axes.hist(val, bins = 20, density=True, histtype='bar', color=colors, label=names)
    axes.legend(prop={'size': 10})
    axes.xaxis.set_major_locator(MaxNLocator(nbins=20))
    axes.tick_params(axis='x', labelrotation=90) 
    axes.set_title("Clusters")


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

    ax0.hist(val, bins = 10, density=True, histtype='bar', color=colors, label=names)
    ax0.legend(prop={'size': 10})
    ax0.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax0.tick_params(axis='x', labelrotation=90) 
    ax0.set_title("Connected areas")

    val = []

    val.append(isolate_feature_by_index(14, living_objects))
    val.append(isolate_feature_by_index(14, nonliving_objects))

    ax1.hist(val, bins = 10, density=True, histtype='bar', color=colors, label=names)
    ax1.legend(prop={'size': 10})
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax1.tick_params(axis='x', labelrotation=90) 
    ax1.set_title("Eyes")

    val = []

    val.append(isolate_feature_by_index(15, living_objects))
    val.append(isolate_feature_by_index(15, nonliving_objects))

    ax2.hist(val, bins = 10, density=True, histtype='bar', color=colors, label=names)
    ax2.legend(prop={'size': 10})
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax2.tick_params(axis='x', labelrotation=90) 
    ax2.set_title("Hollowness")

def get_all_means(objects):
    val = []
    for row in objects:
        val.append(mean(row))
    return val

def get_all_range(objects):
    val = []
    for row in objects:
        val.append(rnge(row))
    return val

def get_all_median(objects):
    val = []
    for row in objects:
        val.append(median(row))
    return val

def get_all_mode(objects):
    val = []
    for row in objects:
        val.append(mode(row))
    return val

def calculate_measures(type, objRef, object):
    if(all_equal_zero(object)):
        print(f"OBJECT: {objRef} all return 0 -- cannot calculate measures\n")
    else:
        mean = 0
        median = 0
        rnge = 0
        mode = 0

        # mean
        for i in object:
            mean = mean + i
        mean = mean / len(object)

        #median
        median = statistics.median(object)

        #range
        min_val = 0
        max_val = 0
        for i in object:
            if(min_val > i):
                min_val = i
            if(max_val < i):
                max_val = i
        rnge = max_val - min_val

        #mode
        mode = statistics.mode(object)

        #print out 
        print(f"OBJECT({type}): {objRef}")
        print(f"MEAN: {mean}")
        print(f"MODE: {mode}")
        print(f"RANGE: {rnge}")
        print(f"MEDIAN: {median}\n")

def median(object):
    if(all_equal_zero(object)):
        print("cannot calculate")
        return 0
    else:
        median = statistics.median(object)
        return median

def mode(object):
    if(all_equal_zero(object)):
        print("cannot calculate")
        return 0
    else:
          mode = statistics.mode(object)
          return mode

def rnge(object):
    if(all_equal_zero(object)):
        print("cannot calculate")
        return 0
    else:
        min_val = 0
        max_val = 0
        for i in object:
                if(min_val > i):
                    min_val = i
                if(max_val < i):
                    max_val = i
        rnge = min_val - max_val
        return rnge;

def mean(object):
    if(all_equal_zero(object)):
        print("cannot calculate")
        return 0
    else:
        for i in object:
                mean = mean + i
        mean = mean / len(object)
        return mean

def all_equal_zero(object):
    for i in object:
        if(i > 0):
            return False
    return True

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

def task_3_2(csv_stored):
    variance = calculate_variance(isolate_feature_by_index(1, csv_stored))
    mean = calculate_mean(isolate_feature_by_index(1, csv_stored))

    sigma = np.sqrt(variance)
    x = np.linspace(mean - 3*sigma, mean + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mean, sigma))

def task_3_3(csv_stored):
    percentile = stats.norm.ppf(0.95, calculate_mean(isolate_feature_by_index(1, csv_stored)), calculate_variance(isolate_feature_by_index(1, csv_stored)))
    print(f"TASK 3.3: {percentile}")

def t_test(num, object1, object2):
    if(all_equal_zero(object1) | (all_equal_zero(object2))):
         print(f"OBJECT{num} has no data\n")
    else:
        log_data1 = np.log1p(object1)
        log_data2 = np.log1p(object2)

        t_stat, p_value = stats.ttest_ind(log_data1, log_data2)

        r_t_stat = round(t_stat, 3)
        r_p_value = round(p_value, 3)

        print(f"LIVING AGAISNT NONLIVING\nREF{num} has:")
        print(f"T: {r_t_stat}")
        print(f"P: {r_p_value}")

        if(r_p_value >= 0.05):
            print(f"NULL HYPOTHESIS PROVEN IN REF{num}\n")
        else:
            print(f"FAIL TO REJECT NULL HYPOTHESIS IN REF{num}\n")


def task_3_4(csv_stored, living_objects, nonliving_objects):

    #barcharts for normal values
    show_black_px_per_rows(living_objects, nonliving_objects)
    show_black_px_per_col(living_objects, nonliving_objects)
    show_hollow_eyes_con_areas(living_objects, nonliving_objects)
    show_clusters(living_objects, nonliving_objects)

    # #print out written version of staistical values
    len_b = 16
    for j in range(len_b):
            calculate_measures("living", j + 1, isolate_feature_by_index(j + 1, living_objects))
            calculate_measures("non-living", j + 1, isolate_feature_by_index(j + 1, nonliving_objects)) 

    #t-tests
    len_b = 16
    for j in range(len_b):
                t_test(j+1, isolate_feature_by_index(j + 1, living_objects), isolate_feature_by_index(j + 1, nonliving_objects)) 

def y_intercept(slope, intercept, x):
  return slope * x + intercept
                
def calculate_line_correlation(type, num1, num2, obj1, obj2):
    if(num1 == num2):
        print(f"SKIP (EXPERIMENT {num1} == {num2})\n")
        return 0, 0
    else:
        slope, intercept, r_value, p_value, std_err = stats.linregress(obj1,obj2)
        r_squared = r_value**2
    
        print(f"EXPERIMENT ({type}) {num1} + {num2}:")
        print(f"R_VALUE: {r_value}")
        print(f"R2_VALUE: {r_squared}")
        print(f"P_VALUE: {round(p_value, 2)}\n")

        model = list(map(lambda x: plot_y(x, slope, intercept), obj1))

        plt.scatter(obj1, obj2, color = 'blue')
        plt.xlabel(num1)
        plt.ylabel(num2)
        plt.title(f"Graph: {type} ( {num1}|{num2} )")
        plt.plot(obj1, model)
        plt.show()
        return r_value, r_squared

def plot_y(obj, slope, intercept):
    return slope * obj + intercept

def task_3_5(living_objects, nonliving_objects):
    #1, 8, 9, 10, 15
    val = [1, 8, 9, 10, 15]
    #[0] = val, [1] = x, [2] = y
    highest_r = [0, 0, 0]
    highest_r_squared = [0, 0, 0]

    #living objects
    for i in val:
        for j in val:
            temp_0, temp_1 = calculate_line_correlation("living", i, j, isolate_feature_by_index(i, living_objects), isolate_feature_by_index(j, living_objects))
            if(temp_0 > highest_r):
                highest_r[0] = temp_0
                highest_r[1] = i
                highest_r[2] = j
            if(temp_0 > highest_r_squared):
                highest_r_squared[0] = temp_1
                highest_r_squared[1] = i
                highest_r_squared[2] = j

    print(f"HIGHEST (living) R EXPERIMENT{highest_r[1]}{highest_r[2]}:")
    print(f"R: {highest_r[0]}\n")

    print(f"HIGHEST (living) R2 EXPERIMENT{highest_r_squared[1]}{highest_r_squared[2]}:")
    print(f"R: {highest_r_squared[0]}\n")

    #nonliving objects
    for i in val:
        for j in val:
            temp_0, temp_1 = calculate_line_correlation("non-living", i, j, isolate_feature_by_index(i, nonliving_objects), isolate_feature_by_index(j, nonliving_objects))
            if(temp_0 > highest_r):
                highest_r[0] = temp_0
                highest_r[1] = i
                highest_r[2] = j
            if(temp_0 > highest_r_squared):
                highest_r_squared[0] = temp_1
                highest_r_squared[1] = i
                highest_r_squared[2] = j

    print(f"HIGHEST (living) R EXPERIMENT{highest_r[1]}{highest_r[2]}:")
    print(f"R: {highest_r[0]}\n")

    print(f"HIGHEST (living) R2 EXPERIMENT{highest_r_squared[1]}{highest_r_squared[2]}:")
    print(f"R: {highest_r_squared[0]}\n")


with open("../../40437373_features.csv", mode ='r')as file:
          csvFile = csv.reader(file)
          for row in csvFile:
              tmp = []
              for num in row:
                      tmp.append(num)
              csv_stored.append(tmp)


living_objects = find_living_obj(csv_stored)
nonliving_objects = find_nonliving_obj(csv_stored)

#task 3.1
task_3_1(living_objects, nonliving_objects, csv_stored)

# #task 3.2
# task_3_2(csv_stored)

# #task 3.3.
# task_3_3(csv_stored)

# # task 3_4
# task_3_4(csv_stored, living_objects, nonliving_objects)

# # task 3_5
# task_3_5(living_objects, nonliving_objects)


plt.show();


# mymodel = list(map(myfunc, x))
# print(r)
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

