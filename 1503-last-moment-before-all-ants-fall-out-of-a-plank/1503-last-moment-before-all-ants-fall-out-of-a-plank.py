class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # getMaxLeft() gets the maximum index of ants moving to left
        maxLeft = max(left, default=0)
        
        # getMinRight() gets the minimum index of ants moving to right
        # we subtract it from n to get the distance from the right edge
        minRight = n - min(right, default=n)
        
        # the maximum of these two values will be our result
        return max(maxLeft, minRight)