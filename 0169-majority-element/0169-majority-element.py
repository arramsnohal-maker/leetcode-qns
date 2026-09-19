class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        max=0
        n=0
        for j in dict:
            if dict[j]>max:
                max=dict[j]
                n=j
        return n