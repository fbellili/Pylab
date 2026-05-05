"""
Program: Lab 15 
Author: Farouk Bellili
Purpose: Use matplotlib and the math library to plot the Sinc function,
         sin(x)/x
Starter Code: N/A
Date: 2026-05-05
"""
 
import matplotlib.pyplot as plt
import math
 
x = []
y = []
 
for i in range(1, 3151):
    x_val = i / 10.0
 
    # sin(x)/x is undefined at x=0, so we use 1.
    if x_val == 0:
        y_val = 1.0
    else:
        y_val = math.sin(x_val) / x_val
 
    x.append(x_val)
    y.append(y_val)
 
plt.plot(x, y)
plt.title("Sinc Function: sin(x) / x")
plt.xlabel("x")
plt.ylabel("sin(x) / x")
 
plt.savefig("sinc_plot.png")
plt.show()
 
