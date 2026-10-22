class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        digit=0
        for i in range(0,len(nums)):
            sums=0
            x=nums[i]
            while x>0:
                digit=x%10
                x=x//10
                sums+=digit
            if i==sums:
                return i
        return -1
        
