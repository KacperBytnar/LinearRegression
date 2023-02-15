
import numpy
import pandas 
import matplotlib.pyplot as plt


print("Assignment 2")
list1 = [1, 2, 5]
list2 = [2, 4, 6]
xy = []
for num1, num2 in zip(list1, list2):
   xy.append(num1*num2)
print(xy)


print("Assignment 3")
def xySum_Prod(list1,list2):
    result=0
    for num1, num2 in zip(list1, list2):
       ##result = result + (num1*num2)
       result += (num1*num2)
    return result

print(xySum_Prod(list1, list2));
     


print("Assignment 4")
def find_a(x,y):
    n = len(x)
    xSum = sum(x)
    ySum = sum(y)
    xySum = xySum_Prod(x,y)
    x2Sum = xySum_Prod(x,x)
    a = ((ySum * x2Sum) - (xSum*xySum))/(n*x2Sum - xSum*xSum)
    return a
a = find_a(list1,list2)
print(f"a: {a}")



print("Assignment 5")
def find_b(x,y):
    n = len(x)
    xSum = sum(x)
    ySum = sum(y)
    xySum = xySum_Prod(x,y)
    x2Sum = xySum_Prod(x,x)
    b = (n*xySum - xSum*ySum)/(n*x2Sum - xSum**2)
    return b
b = find_b(list1,list2)
print(f"b: {b}")


print("Assignment 6")
#Cost per click of individual keywords
x = [2.3, 2.1, 2.5, 4.5, 5.9, 4.1, 8.9]
#Total amount of clicks per day
y = [89.0, 63.0, 71.0, 70.0, 80.0, 89.0, 150.0]\
    
a = find_a(x,y)
b = find_b(x,y)
print(f"a: {a}")
print(f"b: {b}")



print("Assignment 7")

plt.axis([0, 10, 0, 200])
plt.scatter(x, y)
test_line = [(b*item + a) for item in [0, 10]]
plt.plot([0, 10], test_line)
     