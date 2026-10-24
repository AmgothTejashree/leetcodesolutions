class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        digit=0
        rev=0
        x=num
        rever=0
        digi=0
        while num>0:
            digit=num%10
            num=num//10
            rev=rev*10+digit
        while rev>0:
            digi=rev%10
            rev=rev//10
            rever=rever*10+digi
        if x==rever:
            return True
        return False
        
