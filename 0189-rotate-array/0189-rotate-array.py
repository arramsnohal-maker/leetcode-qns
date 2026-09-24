class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums.reverse()
        k=k%len(nums)
        i=0
        j=k-1
        temp=0
        while(i<=j):
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp
            i+=1
            j-=1
        i=k
        j=len(nums)-1
        while(i<=j):
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp
            i+=1
            j-=1