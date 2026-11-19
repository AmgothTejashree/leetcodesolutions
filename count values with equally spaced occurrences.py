class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count=0
        for i in set(nums):
            a=[]
            for j in range(len(nums)):
                if nums[j]==i:
                    a.append(j)
            if len(a)==3:
                if a[1]-a[0]==a[2]-a[1]:
                    count+=1
        return count


        
