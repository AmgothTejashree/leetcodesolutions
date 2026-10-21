class Solution:
    def hammingWeight(self, n: int) -> int:
        m=n
        rev=0
        count=0
        bit=0
        while n>0:
            bit=n%2
            n=n//2
            rev=rev*10+bit
        while rev>0:
            digit=rev%10
            if digit==1:
                count+=1
            rev//=10
        return count
        
