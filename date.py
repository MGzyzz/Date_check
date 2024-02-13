from dateTimeError import DateTimeError


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show_datetime(self):
        return print(f"Date: {self.year:04}/{self.month:02}/{self.day:02}")

    def check_validation(self):
        if not isinstance(self.year, int):
            raise DateTimeError("year", self.year, "an integer")
        elif not isinstance(self.month, int):
            raise DateTimeError("month", self.month, "an integer")
        elif not isinstance(self.day, int):
            raise DateTimeError("day", self.day, "an integer")

        if not 0 <= self.year <= 9999:
            raise DateTimeError("year", self.year, "between 0 and 9999")
        elif not 1 <= self.month <= 12:
            raise DateTimeError("month", self.month, "between 1 and 12")
        elif not 1 <= self.day <= 31:
            raise DateTimeError("day", self.day, "between 1 and 31")

        if self.month == 2 and self.leap_year() and not (1 <= self.day <= 29):
            raise DateTimeError("day", self.day, "between 1 and 29 because this year is a leap year")
        elif self.month == 2 and not self.leap_year() and not (1 <= self.day <= 28):
            raise DateTimeError("day", self.day, "between 1 and 28 because this year is not a leap year")

        elif self.month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= self.day <= 31):
            raise DateTimeError("day", self.day, "between 1 and 31")
        elif self.month in [2, 4, 6, 9, 11] and not (1 <= self.day <= 30):
            raise DateTimeError("day", self.day, "between 1 and 30")

    def leap_year(self):
        if self.year % 400 == 0 and self.year % 100 == 0:
            return True
        elif self.year % 4 == 0 and self.year % 100 != 0:
            return True
        else:
            return False