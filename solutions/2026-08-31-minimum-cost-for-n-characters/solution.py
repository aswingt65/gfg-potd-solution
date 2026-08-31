from array import array


def minimum_cost(n: int, insert_cost: int, delete_cost: int, copy_cost: int) -> int:
    """Return the minimum cost to display exactly n characters."""
    if n <= 0:
        return 0

    # dp[length] is the minimum cost to obtain exactly `length` characters.
    dp = array("Q", [0])

    for length in range(1, n + 1):
        best = dp[length - 1] + insert_cost

        if length % 2 == 0:
            best = min(best, dp[length // 2] + copy_cost)
        elif length > 1:
            # Copy (length + 1) // 2 characters, then delete one character.
            best = min(best, dp[(length + 1) // 2] + copy_cost + delete_cost)

        dp.append(best)

    return dp[n]


class Solution:
    def minimumCost(self, n: int, i: int, d: int, c: int) -> int:
        return minimum_cost(n, i, d, c)

    # Alias included for platforms that use this common method name.
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        return minimum_cost(n, i, d, c)