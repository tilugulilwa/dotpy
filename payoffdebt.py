# =============================================================================
# This is a continuaton of the previous scenario but in this case
# we are trying to find which minimum repayment (amount) if done equally every month
# for one year will reduce/clear the debt (balance) to zero or less/negative
# =============================================================================

#the outstanding balance on the credit card
balance  = 3926
#annual interest rate as a decimal
annualInterestRate = 0.2
#monthly interest rate
monthly_interest_rate = annualInterestRate/12
# monthly payment minimum - initial - we start with a guess 10 shs; and keep on incrementing by 10
# till when balance is <= 0
monthly_payment_minimum = 10



while(True):
    previous_balance = balance
    for i in range(12):
        monthly_updaid_balance = previous_balance - monthly_payment_minimum
        updated_month_balance = monthly_updaid_balance + monthly_updaid_balance * monthly_interest_rate
        previous_balance = updated_month_balance
    
    if (updated_month_balance > 0):
        monthly_payment_minimum +=10 
        
    else:
        break

print("Lowest payment:", monthly_payment_minimum)

