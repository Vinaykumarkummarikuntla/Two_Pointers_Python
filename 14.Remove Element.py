class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)

        n = len(nums)
        i = 0
        for j in range(0,n):
            if (nums[j] != val):
                nums[i] = nums[j]
                i+=1
        return i