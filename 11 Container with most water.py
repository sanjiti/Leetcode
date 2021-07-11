class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2= len(height)-1
        maxarea = 0
        while p1<p2:
            maxarea = max(maxarea, ((p2-p1)*min(height[p1], height[p2])))
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return maxarea