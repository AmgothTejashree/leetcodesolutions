class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        digit=0
        n=x
        x=abs(x)
        while x!=0:
            digit=x%10
            x=x//10
            rev=rev*10+digit
        if n<0:
            rev=-rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev

        
