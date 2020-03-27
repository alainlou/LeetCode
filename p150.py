class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        idx = 0

        while idx < len(tokens):
            flag = False
            if tokens[idx] == "+":
                tokens[idx] = int(tokens[idx-2]) + int(tokens[idx-1])
                flag = True
            elif tokens[idx] == "-":
                tokens[idx] = int(tokens[idx-2]) - int(tokens[idx-1])
                flag = True
            elif tokens[idx] == "*":
                tokens[idx] = int(tokens[idx-2]) * int(tokens[idx-1])
                flag = True
            elif tokens[idx] == "/":
                tokens[idx] = int(int(tokens[idx-2]) / int(tokens[idx-1]))
                flag = True

            if flag:
                del tokens[idx-2]
                del tokens[idx-2]
                idx -= 1
            else:
                idx += 1

        return int(tokens[0])
