# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:08:12 2017

@author: Jens
"""

import scipy as sp

class primary(object):
    def __init__(self,gpmt,tin,p,qt):
        self.gpmt = gpmt
        self.tin = tin
        self.qt = qt
        self.p = p
        self.dens = 0.02711 # Needs to call density from a steam table
        self.w = sp.zeros(len(self.gpmt))
        
        for i in range(0,len(self.gpmt)):
            self.w[i] = self.dens*self.gpmt[i]*60/7.48
        
        
        
    def echo(self):
        print("THERMAL DESIGN FLOW    (TDF) = {} [gpm]".format(self.gpmt[0]))
        print("BEST ESTIMATE FLOW     (BEF) = {} [gpm]".format(self.gpmt[1]))
        print("MECHANICAL DESIGN FLOW (MDF) = {} [gpm]".format(self.gpmt[2]))
        print("HOT PUMP OVERSPEED     (HPO) = {} [gpm]".format(self.gpmt[3]))
        print("COLD FULL FLOW         (CFF) = {} [gpm]".format(self.gpmt[4]))
           
        

# ----------------------- NEEDS WORK BELOW ----------------------- #

class inletnozzles(primary):
    def __init__(self,dia,l,gpmt):
        # NEED TO FIGURE OUT HOW TO CALL PRIMARY CLASS INTO THIS AS INPUT
        
    # ONCE GPMT GETS SENT INTO INLET NOZZLES MAKE SURE THESE WORKS
    def echo(self):
        print("THERMAL DESIGN FLOW    (TDF) = {} [gpm]".format(self.gpmt[0]))
        print("BEST ESTIMATE FLOW     (BEF) = {} [gpm]".format(self.gpmt[1]))
        print("MECHANICAL DESIGN FLOW (MDF) = {} [gpm]".format(self.gpmt[2]))
        print("HOT PUMP OVERSPEED     (HPO) = {} [gpm]".format(self.gpmt[3]))
        print("COLD FULL FLOW         (CFF) = {} [gpm]".format(self.gpmt[4]))        


a = [1,2,3,4,5]

p = primary(a,513.4,2250.0,3014)
