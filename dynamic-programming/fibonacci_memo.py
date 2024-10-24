## memoization (dp)
## time complexity - O(n)
## space complexity - O(n)

def fibMemo(n, memo={}):
    # base case
    if n <= 2: return 1

    if n in memo: return memo[n]

    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

print(fibMemo(1000))