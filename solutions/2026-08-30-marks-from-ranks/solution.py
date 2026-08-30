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
