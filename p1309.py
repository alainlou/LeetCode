class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        d2s = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10': 'j',
            '11': 'k',
            '12': 'l',
            '13': 'm',
            '14': 'n',
            '15': 'o',
            '16': 'p',
            '17': 'q',
            '18': 'r',
            '19': 's',
            '20': 't',
            '21': 'u',
            '22': 'v',
            '23': 'w',
            '24': 'x',
            '25': 'y',
            '26': 'z'
        }
        i = 0
        n = len(s)
        while i < n:
            if i+2 < n:
                dig = int(s[i:i+2])
                if s[i+2] == '#' and 10 <= dig <= 26:
                    ans.append(d2s[s[i:i+2]])
                    i += 3
                    continue
            ans.append(d2s[s[i]])
            i += 1
        return ''.join(ans)
