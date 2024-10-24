## brute force
## time complexity - O(2^n)
## space complexity - O(n)

def fib(n):
    # base case
    if (n <= 2): return 1
    
    return fib(n-1) + fib(n-2)

print(fib(50))