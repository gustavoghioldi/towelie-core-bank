import numpy as np
import numpy_financial as npf

principal = 90000.00
per = np.arange(1*3) + 1
ipmt = npf.ipmt(0.0861, per, 1*3, principal)
ppmt = npf.ppmt(0.0861, per, 1*3, principal)

pmt = npf.pmt(0.0861, 1*3, principal)

print(ipmt)
print(ppmt)
print(pmt)
print(np.sum(ipmt))