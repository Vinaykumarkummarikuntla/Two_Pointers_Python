class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        ans = 0
        p1, p2, p3 = 0, 0, 0
        while p1 < len(A) and p2 < len(B) and p3 < len(C):
            ans = min(ans, max(abs(A[p1] - B[p2]), max(abs(B[p2] - C[p3]), abs(C[p3] - A[p1]))))
            if A[p1] <= B[p2] and A[p1] <= C[p3]:
                p1 += 1
            elif B[p2] <= A[p1] and B[p2] <= C[p3]:
                p2 += 1
            else:
                p3 += 1
        return ans