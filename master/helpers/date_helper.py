from calendar import monthrange

class DateHelper:
    
    @staticmethod
    def month_days(year:int, month:int):
        return monthrange(year, month)[1]

    