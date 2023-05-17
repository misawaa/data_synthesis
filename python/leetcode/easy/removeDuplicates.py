class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        
        # duyet nums
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:

                nums[count] = nums[i]

                count += 1
        return count
