## RULE 1: CAN USE AN ELEMENT MULTIPLE TIMES
## RULE 2: WHOLE NUMBERS only

## m - target sum [max height of tree possible (eg: 1+1+1+....+1)]
## n - nums.length

## brute force
## time complexity O(n^m)
## space complexity O(m)

def canSum(targetSum, nums):
    # base case
    if (targetSum == 0): return True
    if (targetSum < 0): return False

    for num in nums:
        rem = targetSum - num
        if (canSum(rem, nums) == True): return True

    return False

print(canSum(8, [2,6,3]))
print(canSum(300, [14,7]))