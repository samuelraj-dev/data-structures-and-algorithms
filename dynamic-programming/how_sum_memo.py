## RULE 1: CAN USE AN ELEMENT MULTIPLE TIMES
## RULE 2: WHOLE NUMBERS only

## m - target sum [max height of tree possible (eg: 1+1+1+....+1)]
## n - nums.length

## brute force
## time complexity O(n*m^2) [one of the m of m^2 for copying list]
## space complexity O(m^2)

def how_sum(targetSum, nums, memo={}):
    # base case
    if targetSum == 0: return []
    if targetSum < 0: return None

    if (targetSum in memo): return memo[targetSum]

    for num in nums:
        rem = targetSum - num
        result = how_sum(rem, nums, memo)

        if (result is not None):
            memo[targetSum] = [ *result, num ]
            return memo[targetSum]
    
    memo[targetSum] = None
    return memo[targetSum]

print(how_sum(7, [2,6,3]))
print(how_sum(300, [14,7]))