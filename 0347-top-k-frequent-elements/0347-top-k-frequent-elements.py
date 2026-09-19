class Solution(object):
    def topKFrequent(self, nums, k):
        dict={}
        dict1={}
        arr=[]
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for _ in range(k):
            max=0
            n=0
            for x in dict:
                if dict[x]>max:
                    max=dict[x]
                    n=x
            arr.append(n)
            del dict[n]
        return arr