class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table=[]
        count=0
        _max=0
        for i in range(len(s)):
            
            if s[i] not in table:
                table.append(s[i])
                
            else:
                if _max<=len(table):
                    _max=len(table)
                    
                table=table[table.index(s[i])+1:]
                table.append(s[i])
                
        if _max<len(table):
            _max=len(table)
        return _max
