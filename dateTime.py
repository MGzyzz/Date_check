from date import Date
from dateTimeError import DateTimeError


class DateTime(Date):
    def __init__(self, year, month, day, hours, minute, second):
        super().__init__(year, month, day)
        self.hours = hours
        self.minute = minute
        self.second = second
        self.check_validation()

    def show_datetime(self):
        super().show_datetime()
        return print(f"Time: {int(self.hours):02}:{int(self.minute):02}:{int(self.second):02}")

    def check_validation(self):
        super().check_validation()
        if not isinstance(self.hours, int):
            raise DateTimeError("hours", self.hours, "an integer")
        elif not isinstance(self.minute, int):
            raise DateTimeError("minute", self.minute, "an integer")
        elif not isinstance(self.second, int):
            raise DateTimeError("second", self.second, "an integer")

        if not 0 <= self.hours <= 23:
            raise DateTimeError("hours", self.hours, "between 0 and 23")
        elif not 0 <= self.minute <= 59:
            raise DateTimeError("minute", self.minute, "between 0 and 59")
        elif not 0 <= self.second <= 59:
            raise DateTimeError("second", self.second, "between 0 and 59")


try:
    date = DateTime(2023, 4, 1, 0, 0, 0)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2020, 4, 1, 10, 0, 0)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2020, 2, 29, 22, 59, 59)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(-1, 1, 1, 23, 13, 50)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime("a", 4, 1, 0, 0, 0)
    date.show_datetime()

except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 0, 1, 23, 13, 50)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, "a", 1, 0, 0, 0)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2020, 2, 30, 0, 0, 0)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2021, 2, 29, 0, 0, 0)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 3, 32, 23, 13, 50)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 4, "a", 0, 0, 0)
    date.show_datetime()

except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 3, 1, 24, 13, 50)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 4, 1, "a", 0, 0)
    date.show_datetime()

except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 3, 1, 23, 60, 50)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 4, 1, 0, "a", 0)
    date.show_datetime()

except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 3, 1, 23, 13, 60)
    date.show_datetime()
except DateTimeError as e:
    print(e)

try:
    date = DateTime(2023, 4, 1, 0, 0, "a")
    date.show_datetime()

except DateTimeError as e:
    print(e)