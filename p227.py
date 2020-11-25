class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        
        operators = {'+', '-', '*', '/'}
        
        def read_int(idx):
            ans = 0
            for i in range(idx+1, len(s)+1):
                if i == len(s) or s[i] in operators:
                    return [ans, i]
                else:
                    ans *= 10
                    ans += ord(s[i])-ord('0')
        
        def read_int_reverse(idx):
            ans = 0
            place = 0
            for i in range(idx-1, -1, -1):
                if s[i] == '-' and (i == 0 or s[i-1] in operators):
                    return[-ans, i-1 if i != 0 else 0]
                elif s[i] in operators:
                    return [ans, i+1]
                else:
                    ans += (ord(s[i])-ord('0'))*10**place
                    place += 1
            return [ans, 0]
        
        i = 0        
        while i < len(s):
            if s[i] == '*':
                arg1, end = read_int(i)
                arg2, start = read_int_reverse(i)
                prefix = s[:start] + str(arg1*arg2)
                s = prefix + s[end:]
                i = len(prefix)
            elif s[i] == '/':
                arg1, end = read_int(i)
                arg2, start = read_int_reverse(i)                
                prefix = s[:start] + str(arg2//arg1)
                s = prefix + s[end:]
                i = len(prefix)
            else:
                i += 1
        
        i = 0
        while i < len(s):
            if s[i] == '+':
                arg1, end = read_int(i)
                arg2, start = read_int_reverse(i)
                prefix = s[:start] + str(arg1+arg2)
                s = prefix + s[end:]
                i = len(prefix)
            elif s[i] == '-':
                arg1, end = read_int(i)
                arg2, start = read_int_reverse(i)
                prefix = s[:start] + str(arg2-arg1)
                s = prefix + s[end:]
                i = len(prefix)
            else:
                i += 1
        
        return int(s)