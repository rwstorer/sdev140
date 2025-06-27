"""
Author: Your name
Original program prints a payment table for an input purchase price.  Includes a 
10% down payment and 12% interest rate for the remaining balance.  Payment is calculated 
as 5% of the remaining balance (Amount Financed).  Note that if all payments are made on time, 
the loan will be paid off in 23 months.  

Does the necessary formatting to print the payment schedule with columns for month, starting balance, 
interest amount of payment, principal amount of payment, total payment 
(fixed amount for the first 22 months of the loan) and the ending balance..

 

---- Sample output is below for an input of $200 Purchase Price

Enter the purchase price of item (currency): 200
Down Payment is         20.00
Amount Financed is     180.00

Month Starting Bal   Interest to Pay  Principal to Pay     Payment  Ending Balance
 1        180.00           1.80                  7.20      9.00           172.80
 2        172.80           1.73                  7.27      9.00           165.53
 3        165.53           1.66                  7.34      9.00           158.18
 4        158.18           1.58                  7.42      9.00           150.77
 5        150.77           1.51                  7.49      9.00           143.27
 6        143.27           1.43                  7.57      9.00           135.71
 7        135.71           1.36                  7.64      9.00           128.06
 8        128.06           1.28                  7.72      9.00           120.34
 9        120.34           1.20                  7.80      9.00           112.55
10        112.55           1.13                  7.87      9.00           104.67
11        104.67           1.05                  7.95      9.00            96.72
12         96.72           0.97                  8.03      9.00            88.69
13         88.69           0.89                  8.11      9.00            80.57
14         80.57           0.81                  8.19      9.00            72.38
15         72.38           0.72                  8.28      9.00            64.10
16         64.10           0.64                  8.36      9.00            55.74
17         55.74           0.56                  8.44      9.00            47.30
18         47.30           0.47                  8.53      9.00            38.77
19         38.77           0.39                  8.61      9.00            30.16
20         30.16           0.30                  8.70      9.00            21.46
21         21.46           0.21                  8.79      9.00            12.68
22         12.68           0.13                  8.87      9.00             3.80
23          3.80           0.04                  3.80      3.84             0.00
 End Program 
"""

DOWN_PMT: float = 0.1  # 10% down
INT_RATE: float = 0.01 # 12% annually = 1% per month
PMT_PCT: float = 0.05  # 5% monthly payment based on the initial loan amount
INPUT_ERR_MSG: str = 'Input error: Please enter a valid number greater than zero.'
str_loan_amt: str = input('Enter the loan amount: ')

def print_payment_schedule(loan_amount: float) -> None:
    """See the example of the output above

    Args:
        loan_amount (float): what is the loan amount
    """
    down_payment: float = loan_amount * DOWN_PMT
    current_amt: float = loan_amount - down_payment
    month_cnt: int = 0
    int_pay: float = 0.0
    principal: float = 0.0
    end_bal: float = 0.0
    print(f"Down Payment is:    {down_payment:10.2f}")
    print(f"Amount Financed is: {current_amt:10.2f}")
    print("\nMonth Starting Bal   Interest to Pay  Principal to Pay     Payment  Ending Balance")
    
    monthly_pmt: float = current_amt * PMT_PCT
    while current_amt > 0.01:
        month_cnt += 1
        print(f"{month_cnt:3}",end='')
        print(f"{current_amt:16.2f}",end='')
        int_pay = (current_amt * INT_RATE)
        print(f"{int_pay:15.2f}",end='')
        if monthly_pmt > current_amt:
            monthly_pmt = current_amt + int_pay
            end_bal = 0.00
            current_amt = 0.00
        else:
            end_bal = current_amt - monthly_pmt + int_pay
        principal = monthly_pmt - int_pay
        print(f"{principal:15.2f}",end='')            
        print(f"{monthly_pmt:16.2f}",end='')
        print(f"{end_bal:12.2f}")
        current_amt = end_bal
    

loan_amt: float = 0.0
if str.isdigit(str_loan_amt):
    loan_amt = float(str_loan_amt)
    if loan_amt <= 0:
        print(INPUT_ERR_MSG)
        exit(-1)
else:
    print(INPUT_ERR_MSG)
    exit(-1)

print_payment_schedule(loan_amt)
