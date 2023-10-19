class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0

        # important: add 0 at the begining and in the end
        # won't change if the first and last plot can plant flower
        flowerbed = [0] + flowerbed + [0]

        # scan each plot, check if it can plant flower
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1:i+2] == [0,0,0]:
                count += 1
                flowerbed[i] = 1
            if count >= n:
                return True    

        return False