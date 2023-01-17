class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
        n = len(A)
        max_len = 0
        max_start = -1
        start = 0
        end = 0
        zeroes = 0
        while end < n:
            if A[end] == 0:
                zeroes += 1
            while zeroes > B:
                if A[start] == 0:
                    zeroes -= 1
                start += 1
            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_start = start
            end += 1
        return [i for i in range(max_start, max_start + max_len)]