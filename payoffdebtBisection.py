# =============================================================================
# an improvement of the previous algorithm using bisection search
# an interesting hint in this example is -> without applying round function
# the loop won't end because the else code will never be executed as the first 
# two if blocks will always be true (eithe of the two) 
# i.e. updated_month_balance will never go 0 unless rounded
# =============================================================================

#the outstanding balance on the credit card
balance  = 999999
#annual interest rate as a decimal
annualInterestRate = 0.18
#monthly interest rate
monthly_interest_rate = annualInterestRate/12

#Monthly payment lower bound = Balance / 12
lower_bound = balance/12.0
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
upper_bound = (balance*((1+monthly_interest_rate)**12))/12.0


while(True):
    previous_balance = balance
    for i in range(12):
        monthly_updaid_balance = previous_balance - (lower_bound + upper_bound)/2
        updated_month_balance = monthly_updaid_balance + monthly_updaid_balance * monthly_interest_rate
        previous_balance = updated_month_balance
        
    if (round(updated_month_balance,2) < 0):
        upper_bound =(lower_bound + upper_bound)/2
        #print("less",updated_month_balance)
    elif(round(updated_month_balance,2) > 0):
        lower_bound = (lower_bound + upper_bound)/2
        #print("over",updated_month_balance)
    else:
        break

lowest_payment = (lower_bound + upper_bound)/2
lowest_payment = round(lowest_payment,2)
print("Lowest payment:", lowest_payment)

