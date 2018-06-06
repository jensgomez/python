from scipy import log10, sqrt
from scipy.optimize import newton


def ColebrookWhite( f0, eps, dh, re, v ):
    """
    Creating a function to solve for the friction factor using
    the Colebrook - White equation:
    1/sqrt(f) = -2*log10( e/(3.7*dH) + 2.51/(Re*sqrt(f)) )

    """
    
    echo = 1
    if echo == 1:
        print("ECHO ENABLED ... INPUTS INTO FUNCTION LISTED BELOW:  ")
        print(" VELOCITY             = ", v)
        print(" ROUGHNESS            = ", eps)
        print(" HYDRAULIC DIAMETER   = ", dh)
        print(" REYNOLDS NUMBER      = ", re)
        print(" INITIAL GUESS OF F   = ", f0)
        print(" ")
    
    fric = 1/sqrt(f0) + 2*log10(eps/(3.7*dh) + 2.51/(re*sqrt(f0)))
    
    return fric
    
    
    
f0 = 0.001   
re = 1e6
dh = 4
eps = 2.5e-4
v = 10

f = newton( func=ColebrookWhite, x0 = f0, args=( eps, dh, re, v) )

print(f)
    
    
    
    
    
