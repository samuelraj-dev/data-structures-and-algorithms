### ALLOWED MOVES - RIGHT, DOWN only

## brute force
## time complexity - O(2^(x+y))
## space complexity - O(x+y)

def gridTraveler(x, y):
    # base case
    if (x == 1 and y == 1): return 1
    if (x == 0 or y == 0): return 0

    return gridTraveler(x-1, y) + gridTraveler(x, y-1)

print(gridTraveler(20, 20))