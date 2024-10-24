### ALLOWED MOVES - RIGHT, DOWN only

## memoization (dp)
## time complexity - O(x*y)
## space complexity - O(x+y)

def gridTravelerMemo(x, y, memo={}):
    # base case
    if (x == 1 and y == 1): return 1
    if (x == 0 or y == 0): return 0

    if (x,y) in memo: return memo[(x,y)]
    if (y,x) in memo: return memo[(y,x)]    

    memo[(x,y)] = gridTravelerMemo(x-1, y) + gridTravelerMemo(x, y-1)
    return memo[(x,y)]

print(gridTravelerMemo(20, 20))