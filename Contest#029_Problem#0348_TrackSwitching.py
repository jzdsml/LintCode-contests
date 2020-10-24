class Solution:
    """
    @param obstacles: the tracks which obstacles are settled on.
    @return: return the minimum times to switch the track.
    """
    def trackSwitching(self, obstacles):
        # f[i]: min number of track switching when ending in track i, where i = 1, 2, 3.
        f = [None, math.inf, 0, math.inf]
        for o in obstacles:
            f = [None, min(f[1], f[2] + 1, f[3] + 1), min(f[1] + 1, f[2], f[3] + 1), min(f[1] + 1, f[2] + 1, f[3])]
            f[o] = math.inf # Update the initial state of next round. Track o is blocked for next round.
        return min(f[1:])
