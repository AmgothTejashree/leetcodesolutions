class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        sett=set()
        ans=0
        for num in nums:
            if num in sett:
                ans^=num
            else:
                sett.add(num)
        return ans
        
