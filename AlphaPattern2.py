n = 4  # number of rows

for i in range(1, n + 1):
    
    # Print leading spaces
    for space in range(n - i):
        print(" ", end=" ")
    
    # Print letters
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()
