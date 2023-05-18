class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 1
        curr_max_index = nums[0]
        next_max_index = nums[0]
        
        for i in range(1, n):
            if i > curr_max_index:
                jumps += 1
                curr_max_index = next_max_index
            
            next_max_index = max(next_max_index, i + nums[i])
        
        return jumps
