import numpy as np
class Sort():

    def bubble_sort(self, nums):
        n = len(nums)
        while n > 0:
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            n -= 1
        return nums

    def selection_sort(self, nums):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums


baobao=Sort()
nums=np.random.randint(0,50,size=10)
print(nums)
print(baobao.bubble_sort(nums))
print((baobao.selection_sort(nums)))

