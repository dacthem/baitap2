import math


def myformat(x):
    return ('%.3f' % x).rstrip('0').rstrip('.')

print("Enter x = 0.5 thoa man dieu kien tat ca")
x=float(input("Enter x="))

def solution_1(x):
    mu=2;
    eps = 0.0001
    first = 1
    second = first+(x/math.factorial(1))
    while(abs(first-second) > eps) :
        first=second
        second=first+(x**mu/math.factorial(mu))
        mu=mu+1
    return first
print("solution 1 : ",solution_1(x))
print("result 1 : ",math.e**x)