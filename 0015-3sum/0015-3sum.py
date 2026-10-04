class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i=0
        j=0
        k=0
        res=set()
        while i<=len(nums)-1:
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]<-nums[i]:
                    j+=1
                    continue
                if nums[j]+nums[k]>-nums[i]:
                    k-=1
                    continue
                if nums[j]+nums[k]==-nums[i]:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
            i+=1
        return [list(x) for x in res]