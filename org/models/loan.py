from django.db import models
from master.models.abstract_model import AbstractModel
from master.models.country import Country
from master.models.currency import Currency
from master.enums.general import (
    AmortizationType,
    DayInMonth, 
    InteresMethod, 
    InteresCalculationPeriod,
    RepaymenthStrategy,
    DayInYears,
    )


class LoanRefiProduct(AbstractModel):
    pass

#TODO: BaloonPayment
# class LonBaloonProduct(AbstractModel):
#    pass <-- preguntar a Allen para implementar. 

class LoanProduct(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=16)
    description = models.TextField(blank=True, null=True)
    start_date  = models.DateField()
    close_date  = models.DateField()
    currency    = models.ForeignKey(Currency, on_delete=models.CASCADE)
    country     = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    amount_multiples = models.IntegerField()
    principal_max = models.DecimalField(max_digits=48, decimal_places=16)
    principal_min = models.DecimalField(max_digits=48, decimal_places=16)
    repayments_max = models.SmallIntegerField()
    repayments_min = models.SmallIntegerField()
    repayment_step = models.SmallIntegerField()
    #fund_origin
    amortization = models.CharField(max_length=64,  choices=AmortizationType.choices)
    nominal_interes_rate = models.DecimalField(max_digits=6, decimal_places=2)
    interes_method = models.CharField(max_length=64, choices= InteresMethod.choices)
    interes_calculation_period = models.CharField(max_length=64, choices= InteresCalculationPeriod.choices)
    repaymenth_strategy = models.CharField(max_length=64, choices=RepaymenthStrategy.choices)
    interest_free_period = models.SmallIntegerField(default=0)
    days_in_years        = models.CharField(max_length=8, choices=DayInYears.choices)
    day_in_month         = models.CharField(max_length=8, choices=DayInMonth.choices)

    def __str__(self):
        return self.name
