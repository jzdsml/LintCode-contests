class Solution:
    """
    @param song: an array represent song'time
    @param M: an integer represent sont time limit
    @return: return the longest time for song
    """
    def LongestSongTime(self, song, M):
        # 越长的歌越往后放，只要最后一首的开始时间<M即可
        # 问题转化为求前N-1首歌在前M-1时间中能达到的最晚开始时间dp[M-1]，再加上最长的歌时长，即为答案
        song.sort()
        N = len(song)
        dp = [0] * M
        for i in range(N-1):
            for j in range(M-1, song[i]-1, -1):
                dp[j] = max(dp[j], dp[j-song[i]] + song[i])
                
        return dp[-1] + song[-1]
