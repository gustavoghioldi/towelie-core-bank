from django.db import models

class InterestRate(models.TextChoices):
    MONTH = 'M'
    YEAR  = 'Y'
    WHOLE = 'W'

class RepayEvery(models.TextChoices):
    DAY   = 'DAY'
    WEEK  = 'WEEK'
    MONTH = 'MONTH'

class AmortizationType(models.TextChoices):
    EQUALS_INSTALLMENTS     = 'EQUALS_INSTALLMENTS'
    EQUAL_PRINCIPAL_PAYMENT = 'EQUAL_PRINCIPAL_PAYMENT'

class InteresMethod(models.TextChoices):
    FLAT              = 'FLAT'
    DECLINING_BALANCE = 'DECLINING_BALANCE'

class InteresCalculationPeriod(models.TextChoices):
    DAILY = 'DAILY'
    SAME_AS_REPAYMENT_PERIOD = 'SAME_AS_REPAYMENT_PERIOD'

class RepaymenthStrategy(models.TextChoices):
    PENALTIES_FEES_INTEREST_PRINCIPAL = 'PENALTIES_FEES_INTEREST_PRINCIPAL'

class DayInYears(models.TextChoices):
    _360 = '360'
    _364 = '364'
    _356 = '365'

class DayInMonth(models.TextChoices):
    _30    = '30'
    ACTUAL = 'ACTUAL'