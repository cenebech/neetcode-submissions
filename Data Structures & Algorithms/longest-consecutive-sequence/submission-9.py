class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        count = 1
        best = 1
        print(nums)
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if abs(nums[i + 1] - nums[i]) == 1:
                count += 1
                best = max(count, best)
            else:
                count = 1
        
        return best
