'''
Created on Mar 5, 2019

@author: jgomezm
'''
import sys

from graph  import draw
from factorial import factorial
from timeit import default_timer as timer

# Cantidad maxima de recursion definido para 128

MAX_NRO = 15 # 15
times = dict() 
#sys.setrecursionlimit(1027)
sys.setrecursionlimit(pow(2,MAX_NRO+1)+3)

print("-"*80)
for i in range(MAX_NRO) :
    index = pow(2,i)
    start = timer() 
    fact = factorial(index)
    end = timer()
    delay = end - start
    times[index] = delay
    #print("2^{} = {} , delay = {}, fact={}" \
    #        .format(i,order[i],times[i], fact))
    print(f"2^{i:02d} = {index:4d} , delay = {times[index]}")
    print("-"*80)

# Show graph 
draw(times.keys(),times.values(),'g','Factorial vs Processing Time', 'Number', 'Time(s)')
