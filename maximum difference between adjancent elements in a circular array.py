class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff=[]
        for i in range(0,len(nums)):
            diff.append(abs(nums[i]-nums[(i+1)%len(nums)]))
        return max(diff)
        
