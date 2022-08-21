Loans
=====

restriciones funcionales
========================

Para crear un Loan debe existir un producto Loan Activo y además un cliente activo y este cliente debe tener una cuenta recaudadora.

El prestamo debe serguir un circuito:

submitedd -> Approved -> disbursement

Una vez submiteado el prestamo, se debe crear una tabla con uun registro por cuota, todo moviemiento dentro de ese prestamo debe ser registrado en esta tabla (Loan Ledger)

para la primera version:
- solo admite pagos totales de las cuotas.

