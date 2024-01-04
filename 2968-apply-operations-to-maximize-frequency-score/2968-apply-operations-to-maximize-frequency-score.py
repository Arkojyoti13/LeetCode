class Solution:
    def findme(self, l, r, nums, prefix):
        mid = (r + l) // 2
        first = prefix[mid]

        if l > 0:
            first -= prefix[l - 1]

        ans = (nums[mid] * (mid - l + 1)) - first
        second = prefix[r] - prefix[mid]
        ans += second - (nums[mid] * (r - mid))
        return ans

    def maxFrequencyScore(self, nums, k):
        nums.sort()
        n = len(nums)
        prefix = [0] * n

        for i in range(n):
            prefix[i] = nums[i] if i == 0 else nums[i] + prefix[i - 1]

        maxi = 0
        for i in range(n):
            low = i
            high = n - 1
            ans = -1

            while low <= high:
                mid = low + (high - low) // 2
                if self.findme(i, mid, nums, prefix) <= k:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if ans != -1:
                maxi = max(maxi, ans - i + 1)
        return maxi