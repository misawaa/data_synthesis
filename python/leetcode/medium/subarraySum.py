class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        sum_counts = {0: 1} # initialize with 0 sum seen once
        for num in nums:
            running_sum += num
            count += sum_counts.get(running_sum - k, 0)
            sum_counts[running_sum] = sum_counts.get(running_sum, 0) + 1
        return count