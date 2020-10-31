class Solution:
    """
    @param lunch: an array that contains each lunch food's calories and value
    @param dinner: an array that contains each dinner food's calories and value
    @param T: the minest limit value
    @return: return the min calories
    """
    def getMinCalories(self, lunch, dinner, T):
        import bisect
        ans = math.inf
        N1, N2 = len(lunch), len(dinner)
        for i in range(N1):
            if lunch[i][1] >= T:
                ans = min(ans, lunch[i][0])
        for i in range(N2):
            if dinner[i][1] >= T:
                ans = min(ans, dinner[i][0])
                
        lunch.sort(key=lambda x: x[1])
        min_cal = [math.inf] * N1
        min_cal[N1-1] = lunch[N1-1][0]
        for i in range(N1-2, -1, -1):
            min_cal[i] = min(min_cal[i+1], lunch[i][0])
        deli = [item[1] for item in lunch]

        for i in range(N2):
            idx = bisect.bisect_left(deli, T-dinner[i][1], lo=0, hi=len(deli))
            if 0 <= idx < len(deli):
                ans = min(ans, dinner[i][0] + min_cal[idx])
        return ans if ans < math.inf else -1
