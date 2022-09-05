class LoanCalculateHelper:
    def __init__(self, principal, payments, tea) -> None:
        self.principal = principal
        self.payments = payments
        self.tea      = tea


    def get_tem(self):
        tea = self.tea/100
        return ((1+tea)**(30/360)-1)

    def get_payment_value(self, periodo="mensual"):
        tasa = self.get_tem()
        monto = self.principal
        cuotas = self.payments

        if periodo == "diario":
            tasa /= 30.4167
        elif periodo == "semanal":
            tasa /= 4.34524
        if periodo == "quincenal":
            tasa /= 2.0
        elif periodo == "bimestral":
            tasa *= 2
        elif periodo == "trimestral":
            tasa *= 3
        elif periodo == "cuatrimestral":
            tasa *= 4
        elif periodo == "semestral":
            tasa *= 6
        elif periodo == "anual":
            tasa *= 12

        return monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )

    def get_payment_detail(self):
        return {
                "tem" : round(self.get_tem(), 4)*100,
                "payment_value": round(self.get_payment_value(), 2),
                "payment_interest": round((self.get_payment_value()*self.payments)-self.principal, 2),
                "loan_total": round(self.get_payment_value()*self.payments, 2)
            }