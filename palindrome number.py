class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        digit=0
        y=x
        while x>0:
            digit=x%10
            x=x//10
            rev=rev*10+digit
        if y==rev:
            return True
        else:
             return False
        
