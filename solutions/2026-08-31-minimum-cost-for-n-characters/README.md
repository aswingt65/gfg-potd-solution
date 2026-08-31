# Minimum Cost for n Characters

## Problem

Minimum Cost for n Characters
Difficulty: MediumAccuracy: 49.82%Submissions: 11K+Points: 4
Given four integers n, i, d, and c, where:

i is the cost of inserting a single character,
d is the cost of deleting the last character,
c is the cost of copying the entire current string and pasting it immediately (thereby doubling its length).
Find the minimum cost required to obtain exactly n characters on the screen. Initially, the screen is empty.

Examples:

Input: n = 9, i = 1, d = 2, c = 1
Output: 5
Explanation: Perform the following operations:
Insert (1 character)
Insert (2 characters)
Copy-paste (4 characters)
Copy-paste (8 characters)
Insert (9 characters)
Total cost = 1 + 1 + 1 + 1 + 1 = 5.
Input: n = 9, i = 10, d = 1, c = 1
Output: 17
Explanation: Perform the following operations:
Insert (1 character)
Copy-paste (2 characters)
Copy-paste (4 characters)
Delete (3 characters)
Copy-paste (6 characters)
Delete (5 characters)
Copy-paste (10 characters)
Delete (9 characters)
Total cost = 10 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 17.
Since insertion is expensive, it is cheaper to use copy-paste operations and adjust the length using deletions.
Constraints:

1 ≤ n ≤ 10^6
1 ≤ i, d, c ≤ 100

## Approach

Dynamic programming computes the cheapest way to reach every length up to n. For an even length, the final step can be an insertion or a copy from half the length. For an odd length, it can be an insertion or a copy to one character too many followed by one deletion.

## Complexity

Time: O(n). Space: O(n), stored compactly in a standard-library unsigned-integer array.

## Verification evidence

- Generated tests: 3
- Docker test result: passed
- Independent review: The DP recurrence is correct for insertions, doubling copies, and overshoot-then-delete paths. Costs and storage fit the constraints, and tests cover the key cases.
