class Solution:
    def toHexspeak(self, num: str) -> str:
        tmp = list(str(hex(int(num)))[2:].upper())
        for i in range(len(tmp)):
            if tmp[i] == "1":
                tmp[i] = "I"
            elif tmp[i] == "0":
                tmp[i] = "O"
            elif not (ord('A') <= ord(tmp[i]) and ord(tmp[i]) <= ord('F')):
                return "ERROR"
        return "".join(tmp)