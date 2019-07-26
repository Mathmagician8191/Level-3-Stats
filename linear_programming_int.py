import math
import operator
from itertools import combinations
from linear_programming_config import *

#boundaries to check in
lower_x = -100
upper_x = 100
lower_y = -100
upper_y = 100

comparisons = {"<" : operator.lt,
               "<=" : operator.le,
               ">" : operator.gt,
               ">=" : operator.ge}

#determines if x, y is in the feasible region
def feasible(x,y):
    for item in constraints:
        if not comparisons[item[3]](item[0] * x + item[1] * y, item[2]): return False
    return True #if no inequations fail

max = -math.inf #so the first feasible intersection will always be greater than this
max_type = "No Solution"
min = math.inf #so the first feasible intersection will be less than this
min_type = "No Solution"

for x in range(lower_x, upper_x):
    for y in range(lower_y, upper_y):
        if feasible(x,y): #if the intersection point is valid
            value = (function[0]*x)+(function[1]*y) #value of the objective function at the point
            
            if value > max:
                max_type = "Single solution"
                max_x = x
                max_y = y
                max = value
            
            elif value == max: #handling multiple solutions
                if max_type == "Single solution": #set up list
                    max_type = "Multiple solutions"
                    max_x = [max_x, x]
                    max_y = [max_y, y]
                elif max_type == "Multiple solutions": #append to list
                    max_x.append(x)
                    max_y.append(y)
            
            if value < min:
                min_x = x
                min_y = y
                min = value
            
            elif value == min:
                if min_type == "Single solution": #set up list
                    min_type == "Multiple solutions"
                    min_x = [min_x, x]
                    min_y = [min_y, y]
                elif min_type == "Multiple solutions": #append to list
                    min_x.append(x)
                    min_y.append(y)

#outputting solutions
if max_type == "No solution":
    print("Nothing lies in the feasible region")
elif max_type == "Multiple solutions":
    points = ""
    for x in range(len(max_x)): #loop through all points
        points += "(" + str(max_x[x]) + ", " + str(max_y[x]) + "), " #turn co-ordinates to string
    print(str(max) + " at " + points[:-2])
else: print(str(max) + " at (" + str(max_x) + ", " + str(max_y) + ")")

if min_type == "No solution":
    pass
elif min_type == "Multiple solutions":
    points = ""
    for x in range(len(min_x)): #loop through all points
        points += "(" + str(min_x[x]) + ", " + str(min_y[x]) + ")," #turn co-ordinates to string
    print(str(min) + " at " + points)
else: print(str(min) + " at (" + str(min_x) + ", " + str(min_y) + ")")
