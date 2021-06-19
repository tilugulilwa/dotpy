# =============================================================================
# This assignement was to simulate balance of a credit card after one year 
# if card owner is paying only a portion of monthtly interest every months
# =============================================================================

#initial balance at the start of first month
balance = 484
#annual interest
annualInterestRate = 0.2
#the portion being paid by card owner monthly
monthlyPaymentRate = 0.04 

for i in range(12):
    #calculating monthly rate card owner has to be paying
    monthlyRate = annualInterestRate/12
    #calculating what the card owner is paying monthly
    minimumMonthlyPayment = monthlyPaymentRate*balance
    #calculating what will remain after paying minimal monthly payments
    monthly_unpaid_balance = balance - minimumMonthlyPayment
    #applying monthly interest at the end of the month
    balance = monthly_unpaid_balance + monthlyRate*monthly_unpaid_balance

print("Remaining balance:",round(balance,2))