from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        if len(points) < 2:
            return 1

        lines = defaultdict(set)
        for i, (x0, y0) in enumerate(points, start=0):
            for j, (x1, y1) in enumerate(points[i + 1:], start=i + 1):
                line = self.find_line(x0, y0, x1, y1)
                lines[line].add(i)
                lines[line].add(j)

        return max((len(pts) for pts in lines.values()))

    def find_line(self, x0, y0, x1, y1) -> tuple[int, int | None]:
        """

        :param x0:
        :param y0:
        :param x1:
        :param y1:
        :return: (slope, intercept)
        """
        if y0 == y1:
            return 0, y0
        if x0 == x1:
            return x0, None

        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0

        return slope, intercept
