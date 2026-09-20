class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r=int(c**0.5)
        l=0
        while l<=r:
            summ=((l*l)+(r*r))
            if summ==c:
                return True
            if summ<c:
                l+=1
            if summ>c:
                r-=1
        return False