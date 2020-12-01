import os
import numpy as np
def E_step():
    pass
def M_step():
    pass
def main(iters):
    i=0
    dif=0.01
    while i<iters:
        E_step()
        M_step()
if __name__=='__main__':
    main()