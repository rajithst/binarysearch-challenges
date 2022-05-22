class Solution:
    def solve(self, n):
        memo = {}

        def rec(steps):
            if steps == 0:
                return 1
            if steps == 1:
                return 1
            if steps == 2:
                return 2
            if steps in memo:
                return memo[steps]
            memo[steps] = rec(steps - 1) + rec(steps - 2)
            return memo[steps]

        return rec(n) % (10 ** 9 + 7)
