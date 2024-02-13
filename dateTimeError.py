class DateTimeError(Exception):
    def __init__(self, value, cause_error, conclusion_decision):
        self.value = value
        self.cause_error = cause_error
        self.conclusion_decision = conclusion_decision

    def __str__(self):
        return f"Invalid value: {self.cause_error} for {self.value}. It should be {self.conclusion_decision}"