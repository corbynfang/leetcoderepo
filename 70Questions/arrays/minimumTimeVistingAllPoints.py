# Problem: form a list of points, calculate the main distance between first and last points
# Soultion: If the next node is -10x and -5y away its going to be 10 turns because you can only make 1x at a time and the difference in y is made up by diagonials moves during the process of overcoming the difference of x. Time: O(N) Space: O(1)

def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    res = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        res += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    return res
