import csv
import numpy as np

file = open("data.csv")

raw_data = csv.reader(file, delimiter=",")

x = []
y = []

for item in raw_data:
    x.append(item[0])
    y.append(item[1])

def linear(x,y):
    """
    returns m, c, r_2 such that y = m*x + c
    """
    x_mean = 0
    for item in x:
        x_mean += item
    x_mean /= len(x)
    
    y_mean = 0
    for item in y:
        y_mean += item
    y_mean /= len(y)
    
    m_num = 0
    for index in range(len(x)):
        m_num += (x[index]-x_mean)*(y[index]-y_mean)
    
    m_den = 0
    for item in x:
        m_den += (item-x_mean)**2
    
    m = m_num/m_den
    c = y_mean - (m*x_mean)
    
    ss_reg = 0
    ss_tot = 0
    for index in range(len(x)):
        ss_tot += (y[index]-y_mean)**2
        ss_reg += (y[index]-(m*x[index])-b)**2
    r_2 = 1-(ss_reg/ss_tot)
    
    return m,c,r_2

def polynomial(x,y,order):
    """
    returns beta, r_2 such that y = sum(beta[n]*x^n)
    """
    array = []
    for item in x:
        line = []
        for value in range(order+1):
            line.append(item**value)
        array.append(line)
    matrix = np.array(array)
    beta = np.linalg.inv(matrix.T@matrix)@matrix.T@np.array(y)
    
    y_mean = 0
    for item in y:
        y_mean += item
    y_mean /= len(y)
    
    sse = 0
    for index in range(len(x)):
        x_i = x[index]
        value = 0
        for index2 in range(len(beta)):
            value += beta[index2]*x_i**index2
        sse += (y[index] - value)**2
    sst = 0
    for item in y:
        sst += (item - y_mean)**2
    r_2 = 1 - (sse/sst)
    
    return beta, r_2

def exponential(x,y):
    """
    returns a, b such that y = a*e^(b*x)
    """
    y_log = []
    for item in y:
        y_log.append(np.log(item))
    m, c, r_2 = linear(x,y_log)
    
    return exp(c), m, r_2
