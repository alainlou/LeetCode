from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        [year1, month1, day1] = [int(i) for i in date1.split('-')]
        [year2, month2, day2] = [int(i) for i in date2.split('-')]
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
        return abs((date2 - date1).days)
