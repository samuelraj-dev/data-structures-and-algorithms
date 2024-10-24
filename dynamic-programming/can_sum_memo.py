## RULE 1: CAN USE AN ELEMENT MULTIPLE TIMES
## RULE 2: WHOLE NUMBERS only

## m - target sum [max height of tree possible (eg: 1+1+1+....+1)]
## n - nums.length

## brute force
## time complexity O(n*m)
## space complexity O(m)

def canSum(targetSum, nums, memo={}):
    # base case
    if (targetSum == 0): return True
    if (targetSum < 0): return False

    if (targetSum in memo): return memo[targetSum]

    for num in nums:
        rem = targetSum - num
        if (canSum(rem, nums, memo) == True):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return memo[targetSum]

print(canSum(8, [2,6,3]))
print(canSum(300, [14,7]))
# print(canSum(170141183460469231731687303715884105727, [7]))