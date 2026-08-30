# Marks from Ranks

[← Back to solution index](../../README.md)

## Problem

Marks are represented by sorted, non-overlapping, inclusive intervals `l[i]` to `r[i]`.

- `l[i]` and `r[i]` are the first and last valid marks in the i-th interval.
- A mark's rank is its 1-indexed position among every valid mark in increasing order.

For every value in `rank[]`, return the matching mark.

### Examples

```text
Input:  l = [1, 6, 14], r = [3, 9, 15], rank = [2, 5, 8]
Output: [2, 7, 14]

Input:  l = [5, 10], r = [7, 12], rank = [1, 4, 6]
Output: [5, 10, 12]
```

### Constraints

- `1 <= l.size(), r.size(), rank.size() <= 10^5`
- `1 <= l[i], r[i], rank[i] <= 10^5`
- Intervals are sorted and do not overlap.
- Each queried rank is valid.

## Approach

Build a prefix-count array where `prefix[i]` is the total number of valid marks through interval `i`.

For a query rank `k`, binary-search for the first interval whose prefix count is at least `k`. The number of marks before that interval gives the zero-based offset of the answer within the interval.

- Time complexity: `O(n + q log n)`
- Auxiliary space: `O(n)` (not counting the returned answer)

## Python solution

```python
from bisect import bisect_left


class Solution:
    def getMarks(self, l, r, rank):
        prefix = []
        total = 0

        for start, end in zip(l, r):
            total += end - start + 1
            prefix.append(total)

        answer = []
        for k in rank:
            interval = bisect_left(prefix, k)
            marks_before = prefix[interval - 1] if interval else 0
            answer.append(l[interval] + (k - marks_before - 1))

        return answer
```
