class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        arr=[]
        leng=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i]+1==nums[i+1]:
                leng+=1
            else:
                arr.append(leng)
                leng=1
        arr.append(leng)
        return max(arr)
