class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res=[]
        p=0
        i=len(numbers)-1
        while i!=0:
            left=numbers[p]
            right=numbers[i]
            if left+right==target:
                res.append(p+1)
                res.append(i+1)
                return res
            if left+right<target:
                p+=1
            else:
                i-=1