
'''
(x,y,z..) -> final amouny

calculates the future balance of a financial repository
based on:
- the initial amount
- the yearly interest or return in %
- number of forward years to include
- monthly deposits
- tax
    
example:
>>> interest(250000, 1, 1)
252500
<'''


def interest(amount, interest, years,deposit,tax):
    taxAmount=0
    newAmount=0
    for year in range(years):
        newAmount = interest/100*amount
        taxAmount = tax/100*newAmount
        amount += deposit*12
        amount+=newAmount
        amount-=taxAmount
        
    return int(amount)
