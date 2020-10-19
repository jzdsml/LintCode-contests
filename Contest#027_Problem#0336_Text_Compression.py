class Solution:
    """
    @param lines: the text to compress.
    @return: return the text after compression.
    """
    def textCompression(self, lines):
        # 哈希表以及对单词的编号
        table = {}
        word_id = 0
        result = []
        
        for line in lines:
            s = ''
            new_line = ''
            
            for c in line:
                # 如果是英文字符，先加到字符串上
                if c.isalpha():
                    s += c
                    continue

                # 访问到非英文字符时，s 为空的话跳过
                if s == '':
                    new_line += c
                    continue

                # 判断单词是否在哈希表内，进行压缩
                if s in table:
                    new_line += str(table[s])
                else:
                    word_id += 1
                    table[s] = word_id
                    new_line += s
                s = ''
                new_line += c
                
            # 行末的字符串也要处理
            if s:
                if s in table:
                    new_line += str(table[s])
                else:
                    word_id += 1
                    table[s] = word_id
                    new_line += s
            
            result.append(new_line)
        
        return result
