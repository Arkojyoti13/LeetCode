from collections import defaultdict
import math

class Solution:
    def minOperations(self, v):
        m = defaultdict(int)
        n = len(v)
        
        for i in v:
            m[i] += 1
        
        c = 0
        
        for key, count in m.items():
            if count == 1:
                return -1
            c += math.ceil(count / 3.0)
        
        return c