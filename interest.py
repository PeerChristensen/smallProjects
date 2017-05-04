def interest(amount, interest, years,deposit,tax):

    '''
    (x,y,z..) -> final amount
    
    calculates the balance of a
    savings account based on the initial amount,
    the yearly interest in %, number of years, monthly deposits and tax
    
    example:
    >>> interest(250000, 1, 1)
    252500
    '''
    
    tax_amount=0
    new_amount=0
    for year in range(years):
        new_amount = interest/100*amount
        tax_amount = tax/100*new_amount
        amount += deposit*12
        amount+=new_amount
        amount-=tax_amount
        
    return int(amount)
