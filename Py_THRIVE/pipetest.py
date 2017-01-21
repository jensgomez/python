# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:52:47 2017

@author: danieljc
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:08:12 2017

@author: Jens
"""

import scipy as sp

class primary(object):
    def __init__(self,corbyp,gpmt,na,nin,non,p,qt,tin,tsbyp,ttb,title):
        self.corbyp = corbyp
        self.gpmt = gpmt
        self.na = na
        self.nin = nin
        self.non = non
        self.p = p
        self.qt = qt
        self.tin = tin
        self.tsbyp = tsbyp
        self.ttb = ttb
        self.title = title
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
