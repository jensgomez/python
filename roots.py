# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:47:56 2016

@author: Jens
"""

from scipy import optimize
class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 
    
    def f(self,x):
        return self.a*(x**2) + self.b*(x) + self.c
    
    def table(self,l,r,n):
        dx = (r-l)/n
        for i in range(0,n):
            x = l + dx*i
            print("f({}) = {}".format(x, self.f(x)))
    
    def roots(self,l,r):
        return optimize.brentq(self.f,l,r)
        

q1 = quadratic(1,1,-5)
x = 3
print("f({}) = {}".format(x,q1.f(x)))

a = 0
b = 4
n = 10
q1.table(a,b,n)
print(" " )
print("The root between {} and {} is: {} ".format(a,b,q1.roots(a,b)))
