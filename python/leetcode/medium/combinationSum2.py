class Solution:
    # idk
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_sum, chosen):
            if curr_sum == target:
                result.append(list(chosen))
                return
            
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                chosen.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i], chosen)
                chosen.pop()
        
        result = []
        candidates.sort()
        backtrack(0, 0, [])
        return result
