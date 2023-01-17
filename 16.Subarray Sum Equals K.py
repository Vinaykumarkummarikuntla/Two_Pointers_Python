class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        curr_sum = 0
        sum_count = {0: 1}
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_count:
                count += sum_count[curr_sum - k]
            if curr_sum not in sum_count:
                sum_count[curr_sum] = 0
            sum_count[curr_sum] += 1
        return count