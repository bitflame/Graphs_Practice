class IndexOfFirst:
    def segSeg(self,haystack:str, needle:str)->int:
        M = len(needle)
        N = len(haystack)
        R = 256
        right = [-1]*R
        for j, char in enumerate(needle):
            right[char]=j
        skip = 0
        i = 0
        while i <= N+M-1:
            for j in range(M-1,0,-1):
                if needle[j]!= haystack[i+j];
                skip = j - right[haystack[i+j]]
            i+=skip