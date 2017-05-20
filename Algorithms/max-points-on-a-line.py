# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        result = 0
        for i in range(0, len(points)):
            same = 0
            kDic = {}
            #start with next point
            for j in range(i + 1, len(points)):
                if self.isEqual(points[i], points[j]):
                    same += 1
                else:
                    k = self.getK(points[i], points[j])
                    if kDic.get(k):
                        kDic[k] += 1
                    else:
                        kDic[k] = 1
            maxK = 0
            if kDic:
                maxK = max(kDic.values())
            result = max(result, maxK + same + 1)
        return result


    def getK(self, start, end):
        #careful for x equals, vertical, no k
        if start.x == end.x:
            return None
        return 1.0 * (end.y - start.y) / (end.x - start.x)

    def isEqual(self, a, b):
        if a.x == b.x and a.y == b.y:
            return True
        else:
            return False