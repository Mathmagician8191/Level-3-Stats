from math import sqrt
from random import choice, choices, sample
from bootstrap_data import *

def stats(data):
    length = len(data)
    if length == 0:
        return "Invalid data"
    
    mean = 0
    for item in data:
        mean += item
    mean /= length
    
    variance = 0
    for item in data:
        variance += (mean-item)**2
    stdev = sqrt(variance)

    data.sort()
    
    halves = length//2
    quartiles = length//4
    mod = length % 4
    if mod == 0:
        median = (data[halves] + data[halves - 1])/2
        lower = (data[quartiles] + data[quartiles-1])/2
        upper = (data[halves+quartiles] + data[halves+quartiles-1])/2
    elif mod == 1:
        median = data[halves]
        lower = (data[quartiles-1]+3*data[quartiles])/4
        upper = (3*data[halves+quartiles]+data[halves+quartiles+1])/4
    elif mod == 2:
        median = (data[halves] + data[halves - 1])/2
        lower = data[quartiles]
        upper = data[halves+quartiles]
    else:
        median = data[halves]
        lower = (3*data[quartiles]+data[quartiles+1])/4
        upper = (data[halves+quartiles]+3*data[halves+quartiles+1])/4
    return mean, median, lower, upper

def bootstrap(data, samples=1000, percentile=95):
    mean = []
    median = []
    lower = []
    upper = []
    for _ in range(samples):
        sample = sample_data(data, len(data), True)
        s_mean, s_median, s_lower, s_upper = stats(sample)
        mean.append(s_mean)
        median.append(s_median)
        lower.append(s_lower)
        upper.append(s_upper)
    mean.sort()
    median.sort()
    lower.sort()
    upper.sort()
    gap = -int(-samples * (100-percentile)/200)
    for item in mean, median, lower, upper:
        print("Range: " + str(item[gap]) + " to " + str(item[len(item)-1-gap]))

def sample_data(data, size=20, replacement=False):
    if replacement:
        result = choices(data, k=size)
    else: result = sample(data, k=size)
    return result

for dataset in dataset1, dataset2:
    print(stats(dataset))
    bootstrap(dataset, iterations)
