class Solution:
    """
    @param text: the text to print
    @param width: the width of the window
    @return: return the result of pretty print.
    """
    def prettyPrint(self, text, width):
        res = ['*' * (width + 2)]
        for line in text:
            cur = ''
            for word in line:
                if len(cur) + len(word) > width:
                    cur += ' ' * (width - len(cur) + 1)
                    cur += '*'
                    res.append(cur)
                    cur = ''
                if cur == '':
                    cur += '*'
                else:
                    cur += ' '
                cur += word
            if cur:
                cur += ' ' * (width - len(cur) + 1)
                cur += '*'
                res.append(cur)
        res.append('*' * (width + 2))
        return res
