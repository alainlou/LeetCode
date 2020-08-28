from random import randint

def rand7():
    return randint(1, 7)

class Solution:
    def rand10(self):
        return int(1 + 10/7 * (rand7()-1) + 10/49 * (rand7()-1) + 10/343 * (rand7()-1))
