class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 1
        n = len(A)
        A.sort()
        while i < n and j < n:
            if (i!=j and A[j] - A[i] == B):
                return 1
            elif A[j]-A[i] < B:
                j += 1
            else :
                i += 1
        return 0