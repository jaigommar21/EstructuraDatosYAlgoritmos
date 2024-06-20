
'''
Created on Mar 12, 2024
@author: jgomezm
'''
# generate_binary_strings Function
def generate_binary_strings(n, result=''):    
    
    # Base case
    if len(result) == n:
        print(result)
        return
    
    # Append '0' to the string and recurse
    generate_binary_strings(n, result + '0')
    
    # Append '1' to the string and recurse
    generate_binary_strings(n, result + '1')

if __name__ == "__main__":
    n = 8 # number of bits
    generate_binary_strings(n)



