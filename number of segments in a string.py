class Solution:
    def countSegments(self, s: str) -> int:
        arr=[]
        for word in s.split():
            arr.append(word)
            
        return len(arr)


        
