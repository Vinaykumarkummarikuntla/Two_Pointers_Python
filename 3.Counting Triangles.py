class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        n = len(A)
        result = 0
        if n < 3:
            return 0
        for i in range(n-1,1,-1):
            a = 0
            b = i-1
            while a<b:
                if A[a]+A[b] > A[i]:
                    result += (b-a)% (10**9+7)
                    print(result)
                    b -= 1
                else:
                    a += 1 
        return result%(10**9+7)