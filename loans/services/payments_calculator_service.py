class PaymentsCalculatorService:
    
    @staticmethod
    def payments(loan):
        #TODO: que funcione para mas casos de uso
        total = loan.principal * (1 + loan.loan_product.nominal_interes_rate/100)
        return total/loan.number_of_repayments