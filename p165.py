class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1, lst2 = [int(n) for n in version1.split('.')], [int(n) for n in version2.split('.')]

        while len(lst1) > 0 and lst1[-1] == 0:
            del lst1[-1]
        while len(lst2) > 0 and lst2[-1] == 0:
            del lst2[-1]

        idx = 0

        while idx < len(lst1) and idx < len(lst2):
            if lst1[idx] < lst2[idx]:
                return -1
            if lst1[idx] > lst2[idx]:
                return 1
            idx += 1

        if idx == len(lst1) == len(lst2):
            return 0
        if idx == len(lst1):
            return -1
        return 1
