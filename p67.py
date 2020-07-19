class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = []
        carry = 0

        a = a.zfill(max(m, n)+2)
        b = b.zfill(max(m, n)+2)

        i = 0

        while i < max(m, n) or int(a[~i]) or int(b[~i]) or carry:
            res.insert(0, str(int(a[~i])^int(b[~i])^carry))
            carry = (int(a[~i])+int(b[~i])+carry) > 1
            i += 1

        return ''.join(res)
