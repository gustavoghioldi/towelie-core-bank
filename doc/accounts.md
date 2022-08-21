Accounts
========

Existen 2 tipos de cuentas:
- recaudadoras 
- no recaudadoras

Un cliente solo puede tener una cuenta recaudadora, en caso que se seteen 2 cuentas recaudadoras
las anterior cuenta recaudadora quedara seteada como cuenta NO RECAUDADORA (esto es ejecutado en un post_save), pero es bloqueante.

validaciones:
============
Cuando creamos una cuenta nueva se valida lo siguiente:
- Descubierto <= al descubierto del producto
- Recaudadora: el producto debe poder fuuncionar como cuenta Recaudadora. 

Movimientos en cuenta:
=====================
Todos los movientos del balance de la cuenta se debe hacer a traves del LEDGER.
