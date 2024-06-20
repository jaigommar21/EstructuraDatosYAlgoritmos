def generate_binary_strings(n, arr, i):
    if i == n:
        print('-'.join(arr))
        return
    
    # First assign "0" at ith position and try for all other permutations for remaining positions
    arr[i] = "0"
    generate_binary_strings(n, arr, i + 1)

    # Then assign "1" at ith position and try for all other permutations for remaining positions
    arr[i] = "1"
    generate_binary_strings(n, arr, i + 1)

def generate_all_binary_strings(n):
    arr = [None] * n
    print(arr)
    generate_binary_strings(n, arr, 0)

# Example for 3-bit binary strings
generate_all_binary_strings(4)
