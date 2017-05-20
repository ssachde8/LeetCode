class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 pointer approach
        # one pointer at beginig, one at end
        # the further the 2 lines are, greater the area
        # time O(n) single pass
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area