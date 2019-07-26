function = [15, 20] #objective function, [a,b] means ax+by

#constraints are of form [a,b,c,d]
#d is the comparison operator
#ax+by=c (replace = with comparison operator)
constraints = [[1, 0, 0, ">="],
               [0, 1, 5, ">="],
               [0, 1, 20, "<="],
               [3, 4, 115, "<="],
               [1, 2, 50, "<="]]
