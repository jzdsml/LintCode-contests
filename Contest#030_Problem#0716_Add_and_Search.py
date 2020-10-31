class Solution:
    """
    @param inputs: an integer array
    @param tests: an integer array
    @return: return true if sum of two values in inputs are in tests.
    """
    def addAndSearch(self, inputs, tests):
        set_tests = set(tests)
        N = len(inputs)
        for i in range(N-1):
            for j in range(i+1, N):
                if inputs[i] + inputs[j] in set_tests:
                    return True
        return False
