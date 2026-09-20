class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[]
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for k in dict:
            if dict[k]>n/3:
                res.append(k)
        return res