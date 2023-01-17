class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        N = len(nums)
        print(N)
        print(N-1)

        i = pairs = 0
        j = 1

        while j < N:
            if j < N - 1 and nums[j] == nums[j + 1]:
                j += 1

            elif nums[j] == nums[i] + k:
                pairs += 1
                i += 1
                j += 1

            elif nums[j] > nums[i] + k:
                i += 1

            elif nums[j] < nums[i] + k:
                j += 1

            j = max(j, i + 1)

        return pairs