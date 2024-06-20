
'''
Created on Mar 12, 2024
@author: jgomezm
@version: 1.0
'''
    
# Factorial function
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n*factorial(n-1)

# Using
if __name__ == "__main__":
    print(factorial(9))

