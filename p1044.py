class Solution:
    def longestDupSubstring(self, S: str) -> str:
        p = 31
        mod = 10 ** 9 + 7

        def check(length):
            seen = defaultdict(list)
            hash_value = 0
            for i in range(length):
                hash_value *= p
                hash_value += (ord(S[i])-ord('a')+1)
                hash_value %= mod
            seen[hash_value].append((0, length))
            idx = length
            while idx < len(S):
                hash_value -= pow(p, length-1, mod) * (ord(S[idx-length])-ord('a')+1)
                hash_value *= p
                hash_value += (ord(S[idx])-ord('a')+1)
                hash_value %= mod
                for pair in seen[hash_value]:
                    if S[pair[0]:pair[1]] == S[idx-length+1:idx+1]:
                        return (pair[0], pair[1])
                seen[hash_value].append((idx-length+1, idx+1))
                idx += 1
            return None

        lo = 0
        hi = len(S)
        mid = (lo+hi)//2
        ans = None

        while lo != mid:
            tmp = check(mid)
            if tmp is not None:
                lo = mid
                ans = tmp
            else:
                hi = mid
            mid = (lo+hi)//2

        return S[ans[0]:ans[1]] if ans is not None else ""
