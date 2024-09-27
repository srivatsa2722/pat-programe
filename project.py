def triangle_pattern(n):
    for i in range(1, n+1):
        # Print leading spaces for alignment
        print(' ' * (n - i), end='')
        # Print the stars
        print('*' * (2*i - 1))

# Test the function with 5 rows
n = 5
triangle_pattern(n)