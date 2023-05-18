class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # move the positive integer to its corresponding index
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # if all positive integers from 1 to n are present, return n+1
        return n + 1
