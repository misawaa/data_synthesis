class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        
        # Iterate through each interval in intervals
        for interval in intervals:
            
            # If newInterval overlaps with interval, merge them
            if not inserted and newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            
            # If newInterval comes before interval, insert it and mark as inserted
            elif not inserted and newInterval[1] < interval[0]:
                result.append(newInterval)
                result.append(interval)
                inserted = True
            
            # If interval comes before newInterval, add it to the result
            else:
                result.append(interval)
        
        # If newInterval hasn't been inserted yet, add it to the end
        if not inserted:
            result.append(newInterval)
        
        return result
