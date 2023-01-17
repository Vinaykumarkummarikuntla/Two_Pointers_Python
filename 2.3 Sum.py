class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        
        for i in range(0,len(nums)):
            j = i+1
            k = n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0 :
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif nums[j]+nums[k]+nums[i] < 0:
                    j += 1
                else:
                    k -=1
        return ans