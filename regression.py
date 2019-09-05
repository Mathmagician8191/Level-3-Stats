import csv
import numpy as np

file = open("data.csv")

raw_data = csv.reader(file, delimiter=",")

x = []
y = []

header = True #whether or not the data has a header row put True or False
zeroes = 10**-13 #what to set a zero to (to stop divide by zero)

expl = 0 #explanatory variable index
resp = 1 #response variable index

for item in raw_data:
    if not(header):
        if item[expl] == 0:
            x.append(zeroes)
        else: x.append(float(item[expl]))
        if item[resp] == 0:
            y.append(zeroes)
        else: y.append(float(item[resp]))
    else: header = False

def linear(x,y):
    """
    returns m, c, r_2 such that y = m*x + c
    """
    x_mean = np.mean(x)
    
    y_mean = np.mean(y)
    
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
        ss_reg += (y[index]-(m*x[index])-c)**2
    r_2 = 1-(ss_reg/ss_tot)
    
    return m,c,r_2

def gradient(x,y):
    """
    returns m such that y=m*x
    """
    return np.mean(np.divide(x,y))

def polynomial(x,y,order):
    """
    returns beta, ar_2 such that y = sum(beta[n]*x^n)
    """
    n = len(x)
    
    array = []
    for item in x:
        line = []
        for value in range(order+1):
            line.append(item**value)
        array.append(line)
    matrix = np.array(array)
    beta = np.linalg.inv(matrix.T@matrix)@matrix.T@np.array(y)
    
    y_mean = np.mean(y)
    
    sse = 0
    for index in range(n):
        x_i = x[index]
        value = 0
        for index2 in range(len(beta)):
            value += beta[index2]*x_i**index2
        sse += (y[index] - value)**2
    sst = 0
    for item in y:
        sst += (item - y_mean)**2
    ar_2 = 1- ((sse/sst)*(n-1)/(n-order-1))
    
    return beta, ar_2

def exponential(x,y):
    """
    returns a, b such that y = a*e^(b*x)
    """
    y_log = np.log(y)
    m, c, r_2 = linear(x,y_log)
    
    return np.exp(c), m, r_2

def log(x,y):
    """
    returns m, c such that y = m*ln(x) + c
    """
    x_log = np.log(x)
    m, c, r_2 = linear(x_log,y)

    return m, c, r_2

def power(x,y):
    """
    returns m, b such that y = b*x^m
    """
    x_log = np.log(x)
    y_log = np.log(y)
    
    m, c, r_2 = linear(x_log,y_log)
    
    return m, np.exp(c), r_2

def best_polynomial(x,y):
    """
    Finds the polynomial with best adjusted r squared
    """
    ar_2 = -0.001
    r_2 = 0
    beta = [0]
    order = 0
    while r_2 > ar_2:
        ar_2 = r_2
        poly = beta
        order += 1
        beta, r_2 = polynomial(x,y,order)
    return poly, ar_2
