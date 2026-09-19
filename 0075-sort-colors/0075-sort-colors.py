class Solution(object):
    def sortColors(self, nums):
        dict={}
        p=0
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in range(3):
            n = dict.get(j, 0)
            while n!=0:
                nums[p]=j
                p+=1
                n-=1
        return nums