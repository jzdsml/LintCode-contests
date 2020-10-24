class Solution:
    """
    @param a: first sequence
    @param b: second sequence
    @return: return ans
    """
    def Intersection(self, a, b):
        i, j, N1, N2 = 0, 0, len(a), len(b)
        ans= []
        while (i < N1 and j < N2):
            if (a[i][1] >= b[j][0] and a[i][1] <= b[j][1]) or (b[j][1] >= a[i][0] and b[j][1] <= a[i][1]):
                ans.append([i, j])
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1
        return ans
