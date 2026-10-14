class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sums=0
        while(n>0):
            digit=n%10
            n=n//10
            sums+=digit
            product*=digit
            difference=product-sums
        return difference

        

        
