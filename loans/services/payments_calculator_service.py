class PaymentsCalculatorService:
    
    @staticmethod
    def payments(loan):
        #TODO: que funcione para mas casos de uso
        return loan.balance/loan.number_of_repayments