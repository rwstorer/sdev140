# 3.10 - tidbit.py

'''
Write a program in a file named tidbit.py that takes the purchase price as input.
The program should display a table, with appropriate headers, of a payment schedule
for the lifetime of the loan. Each row of the table should contain the following items:

- the month number (beginning with 1)
- the current total balance owed
- the interest owed for that month
- the amount of principal owed for that month
- the payment for that month
- the balance remaining after payment

The amount of interest for a month is equal to balance \* rate / 12.
The amount of principal for a month is equal to the monthly payment minus the interest owed. 
'''

DOWN_PAYMENT: float = 0.1
ANNUAL_INTEREST_RATE: float = 0.12

def monthly_interest_payment(current_balance: float) -> float:
    """Monthly payments are 5% of the listed purchase price, minus the down payment.

    Args:
        current_balance (float): current loan balance

    Returns:
        float: monthly interest amount in dollars
    """
    INTEREST_RATE: float = 0.12
    
    return current_balance * (INTEREST_RATE/12)


def monthly_payment(purchase_price: float) -> float:
    """calculate monthly payment

    Args:
        purchase_price (float): what did we pay for the item

    Returns:
        float: monthly payment in dollars
    """
    MONTHLY_PMT_RATE: float = 0.05
    return purchase_price * MONTHLY_PMT_RATE


REPORT_HEADER: str = 'Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance'
purchase_price: float = 0.0
purchase_entry: str = input('Enter the purchase price:')
down_pmt_entry: str = input('Enter the down payment:')
purchase_price = float(purchase_entry)
down_pmt: float = float(down_pmt_entry)
month_number: int = 0
start_balance: float = purchase_price
interest_to_pay: float = 0.0
# ... other variables
ending_balance: float = 0.0

print(REPORT_HEADER)
while True:
    month_number += 1
    print(month_number, end="")
    print(f"{start_balance:18,.2f}", end="")
    print(f"{interest_to_pay:18,.2f}", end="")
    #... other variables
    print(f"{ending_balance:10,.2f}")
    if ending_balance < 1.0:
        break

