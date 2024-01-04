class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subseq(nums, k):
            stack = []
            for i, num in enumerate(nums):
                while stack and len(nums) - i + len(stack) > k and stack[-1] < num:
                    stack.pop()
                if len(stack) < k:
                    stack.append(num)
            return stack
        
        def merge(nums1, nums2):
            merged = []
            i, j = 0, 0
            while i < len(nums1) or j < len(nums2):
                if i >= len(nums1):
                    merged.append(nums2[j])
                    j += 1
                elif j >= len(nums2):
                    merged.append(nums1[i])
                    i += 1
                elif nums1[i:] > nums2[j:]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            return merged
        
        ans = []
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            j = k - i
            subseq1 = get_max_subseq(nums1, i)
            subseq2 = get_max_subseq(nums2, j)
            merged = merge(subseq1, subseq2)
            ans = max(ans, merged)
        return ans