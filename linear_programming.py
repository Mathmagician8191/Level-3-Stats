import math
from itertools import combinations
from linear_programming_config import *

comparisons = {"<" : [False, False],
               "<=" : [False, True],
               ">" : [True, False],
               ">=" : [True, True]}

#determines if x, y is in the feasible region
def feasible(x,y):
    for item in constraints:
        greater, equal = comparisons[item[3]]
        value = (item[0]*x)+(item[1]*y) #value of LHS of inequation
        if value == item[2]:
            if equal: #if equal LHS and RHS is ok
                continue #skip the constraint because it passes
            else: return 2 #on boundary produces no solution if max/min, unique return value to identify
        elif (value > item[2]) ^ greater: #XOR to compare whether the LHS is more than the RHS and whether that is ok
            return 0 #wrong side of inequation
    return 1 #if no inequations fail

max = -math.inf #so the first feasible intersection will always be greater than this
max_type = "No Solution"
min = math.inf #so the first feasible intersection will be less than this
min_type = "No Solution"

for i, j in combinations(constraints, 2): #loops through all unique combinations
    a = i[0]
    b = i[1]
    c = j[0]
    d = j[1]
    e = i[2]
    f = j[2]
    if a*d != b*c: #otherwise line gradient is identical, either identical lines or parallel lines
        #intersection points are the only candidate max/min options for linear programming
        x = ((d*e)-(b*f))/((a*d)-(b*c)) #intersection x coordinate
        y = ((a*f)-(c*e))/((a*d)-(b*c)) #intersection y coordinate
        
        result = feasible(x,y)
        if result > 0: #if the intersection point is valid
            value = (function[0]*x)+(function[1]*y) #value of the objective function at the point
            
            if value > max:
                if result == 2: #if the result is on the boundary, meaning no solution
                    max_type = "No maximum"
                else:
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
                else:
                    max_type = "Single solution" #no maximum previously, single solution only
                    max_x = x
                    max_y = y
            
            if value < min:
                if result == 2: #if the result is on the boundary, meaning no solution
                    min_x = "No minimum"
                    min_y = "No minimum"
                else:
                    min_x = x
                    min_y = y
                min = value
            
            elif value == min:
                if min_type == "Single solution": #set up list
                    min_type = "Multiple solutions"
                    min_x = [min_x, x]
                    min_y = [min_y, y]
                elif min_type == "Multiple solutions": #append to list
                    min_x.append(x)
                    min_y.append(y)
                else:
                    min_type = "Single solution" #no minimum previously, single solution only
                    min_x = x
                    min_y = y

#outputting solutions
if max_type == "No solution":
    print("Nothing lies in the feasible region")
elif max_type == "No maximum":
    print("There is no maximum, the maximum would lie on an invalid boundary")
elif max_type == "Multiple solutions":
    print("Multiple solutions of: " + str(max))
    points = "On the line between: "
    for x in range(len(max_x)):
        points += "(" + str(max_x[x]) + ", " + str(max_y[x]) + ") and "
    print(points[:-5])
else: print(str(max) + " at (" + str(max_x) + ", " + str(max_y) + ")")

if min_type == "No solution":
    pass
elif min_type == "No minimum":
    print("There is no minimum, the minimum would lie on an invalid boundary")
elif min_type == "Multiple solutions":
    print("Multiple solutions of: " + str(min))
    for x in range(len(min_x)):
        print("(" + str(min_x[x]) + ", " + str(min_y[x]) + ")")
else: print(str(min) + " at (" + str(min_x) + ", " + str(min_y) + ")")
