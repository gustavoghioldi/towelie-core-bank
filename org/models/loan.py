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

class LoanProduct(AbstractModel):
    #can change
    name = models.CharField(max_length=128)
    #can change
    short_name = models.CharField(max_length=16)
    #can change
    description = models.TextField(blank=True, null=True)
    #only if not allow loans
    start_date  = models.DateField()
    #can change
    close_date  = models.DateField()
    #cant change
    currency    = models.ForeignKey(Currency, on_delete=models.CASCADE)
    #cant change
    country     = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    #can change
    amount_multiples = models.IntegerField()
    #can change
    principal_max = models.DecimalField(max_digits=48, decimal_places=16)
    #can change
    principal_min = models.DecimalField(max_digits=48, decimal_places=16)
    #can change
    repayments_max = models.SmallIntegerField()
    #can change
    repayments_min = models.SmallIntegerField()
    #can change
    repayment_step = models.SmallIntegerField()
    ######cant change#####
    amortization = models.CharField(max_length=64, choices=AmortizationType.choices)
    nominal_interes_rate = models.DecimalField(max_digits=6, decimal_places=2)
    interes_method = models.CharField(max_length=64, choices= InteresMethod.choices)
    interes_calculation_period = models.CharField(max_length=64, choices= InteresCalculationPeriod.choices)
    repaymenth_strategy = models.CharField(max_length=64, choices=RepaymenthStrategy.choices)
    interest_free_period = models.SmallIntegerField(default=0)
    days_in_years        = models.CharField(max_length=8, choices=DayInYears.choices)
    day_in_month         = models.CharField(max_length=8, choices=DayInMonth.choices)
    ######end cant change#####
    def __str__(self):
        return self.name
