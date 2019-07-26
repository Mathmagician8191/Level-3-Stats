# Regression

A file data.csv is needed with a column for x coordinates and one for y. The first column becomes the variable *x* and the second one becomes *y*.

*linear(x,y)* does linear regression on *x* and *y*. It returns *m* and *c* such that *mx+c* is the best linear match for the data.

*polynomial(x,y,order)* matches *x* and *y* to a polynomial of degree *order*. it returns a list, of which the value of a given index *n* (python list are 0-indexed) is the coefficient of the *x<sup>n</sup>* term

Both functions also give an R<sup>2</sup> value.
