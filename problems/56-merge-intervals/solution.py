class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # O(nlogn)
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        # O(n)
        for (start, end) in intervals[1:]:
            last = output[-1]
            last_end = last[1]

            if start <= last_end:
                last[1] = max(last_end, end)
            else:
                output.append([start, end])

        return output
