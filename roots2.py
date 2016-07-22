# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:25:51 2016

@author: Jens
"""

import scipy as sp
import matplotlib.pyplot as plt

class extrema:
    def __init__(self,f,a,b):
        self.f = f
        self.a = a
        self.b = b
        
    def roots(self):
        root = sp.optimize.brentq(self.f,self.a,self.b,args=(), xtol=1e-12, rtol=4.4408920985006262e-16, maxiter=100, full_output=True, disp=True)
        n = 100
        x = sp.linspace(self.a,self.b,n)
        func = sp.zeros(n)
        for i in range(0,n):
            func[i] = self.f(x[i])

        plt.plot(root[0],0, 'ro')
        plt.axhline(y=0)
        plt.plot(x,func)
        print("root between x1 = {0:8.5f} and x2 = {1:8.5f} is at x = {2:8.5f}".format(self.a,self.b,root[0]))
        return root


def f1(x):
    return sp.cos(x)
    
    
def f2(x):
    return sp.sin(x)*sp.log(x)
    
    

# minmax1 = extrema(f1,2*sp.pi,3*sp.pi)
# r1 = minmax1.roots()


minmax2 = extrema(f2,2,4)
r2 = minmax2.roots()
