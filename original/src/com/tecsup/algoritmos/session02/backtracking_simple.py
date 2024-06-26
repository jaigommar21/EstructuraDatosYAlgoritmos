'''
Created on Mar 10, 2019
@author: jgomezm
'''
# bitStrings Function
def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    return [ digit + bitstring 
             for digit in bitStrings(1)
                 for bitstring in bitStrings(n-1)]

if __name__ == "__main__":
    # Excuting            
    print(bitStrings(3))