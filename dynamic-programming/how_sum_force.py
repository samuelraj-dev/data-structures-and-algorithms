## RULE 1: CAN USE AN ELEMENT MULTIPLE TIMES
## RULE 2: WHOLE NUMBERS only

## m - target sum [max height of tree possible (eg: 1+1+1+....+1)]
## n - nums.length

## brute force
## time complexity O(n^m * m) [m multiplied for copying list]
## space complexity O(m)

def how_sum(targetSum, nums):
    # base case
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in nums:
        rem = targetSum - num
        result = how_sum(rem, nums)

        if (result is not None): return [ *result, num ]
    
    return None

print(how_sum(7, [2,6,3]))
print(how_sum(300, [14,7]))