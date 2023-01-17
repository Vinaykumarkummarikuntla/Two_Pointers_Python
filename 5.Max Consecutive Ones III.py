class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        flip = 0
        n = len(nums)
        result = 0

        for i in range(n):
            if nums[i] == 0:
                flip += 1

            while flip > k:
                if nums[j] == 0:
                    flip -=1
                j +=1
            result = max(result,i-j+1)
        return result