class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
                
        m, n = len(A), len(B)
        A[:] = A + [0] * n
        # l = m + n
        position = m + n - 1
        p1, p2 = m-1, n-1
        while p1 >= 0 and p2 >= 0:
            if A[p1] > B[p2]:
                A[position] = A[p1]
                p1 -= 1
            else:
                A[position] = B[p2]
                p2 -= 1
            position -= 1
            
        while p1 >= 0:
            A[position] = A[p1]
            p1 -= 1
            position -= 1
        
        while p2 >= 0:
            A[position] = B[p2]
            p2 -= 1
            position -= 1
                