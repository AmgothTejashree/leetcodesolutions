class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a=set()
        for i in range(0,len(s)):
            if s[i] not in a:
                a.add(s[i])
            else:
                return s[i]
        
