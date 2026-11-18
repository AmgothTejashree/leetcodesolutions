class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr=[]
        for i in range(0,len(order)):
            if order[i] in friends:
                arr.append(order[i])
        return arr
