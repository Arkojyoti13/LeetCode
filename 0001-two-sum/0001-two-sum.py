class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        s = []
        
        for i in range(l-1):
            for j in range(i+1,l):
                if(nums[i]+nums[j]==target):
                    s.append(i)
                    s.append(j)
        return s