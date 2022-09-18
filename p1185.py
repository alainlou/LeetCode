class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        def is_leap_year(y):
            return True if y%4 == 0 and (y%100 != 0 or y%400 == 0) else False

        long_months = set([1, 3, 5, 7, 8, 10, 12])

        # jan 1 1971 is a Friday
        days = 0
        for i in range(1971, year):
            days += 366 if is_leap_year(i) else 365

        for i in range(1, month):
            if i == 2:
                days += 29 if is_leap_year(year) else 28
            elif (i in long_months):
                days += 31
            else:
                days += 30

        days += day-1

        lookup = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        return lookup[days%7]
