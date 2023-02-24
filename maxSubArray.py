class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum+n, n)
            maxSub = max(maxSub, curSum)

        return maxSub