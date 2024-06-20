'''9
Created on Mar 9, 2019

@author: jgomezm
'''

# /usr/local/bin/python3 -m pip install numpy 
# python -m pip install numpy
# python -m pip install matplotlib

import numpy as np

#Custom
from graph import draw
from hanoi import towersOfHanoi
from timeit import default_timer as timer


''' Funcion para resolver la torre de Hanoi 
'''
'''
def TowersOfHanoi(numberOfDisks, src=1, dest=3, tmp=2):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks-1, src = src, dest = tmp, tmp = dest)
        print ("Move disk %d from peg %d to peg %d" % (numberOfDisks, src, dest))
        TowersOfHanoi(numberOfDisks-1, src = tmp, dest = dest, tmp = src)
'''

MAX_NRO = 20#24
x = np.arange(MAX_NRO)
y = np.arange(MAX_NRO, dtype='float')


for i in range(MAX_NRO):
    start = timer()
    x[i] = i
    towersOfHanoi(_nro_disks=i)
    end = timer()
    delay = end - start
    y[i] = delay
    print(x[i])
    print(y[i])
    print("----------------------")


draw(x,y,"g","Hanoi vs Processing Time", "Nunber Disks","Time(s)")


#TowersOfHanoi(numberOfDisks=3)

'''
Move disk 1 from peg 1 to peg 3
Move disk 2 from peg 1 to peg 2
Move disk 1 from peg 3 to peg 2
Move disk 3 from peg 1 to peg 3
Move disk 1 from peg 2 to peg 1
Move disk 2 from peg 2 to peg 3
Move disk 1 from peg 1 to peg 3
'''