#This is a combination of problems 2 and 3, I started writing a bisection search before I saw problem 3

starting_balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_ir = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

#What is the minimum payment to pay off the debt in 12 months?
#Knowns
    #The payment will be less than the balance, if it's more, it won't be the minimum payment
    #The payment will be more than the balance / 12 to account for interest
    #The lower bound of the payment is balance / 12
    #The payment must be a multiple of 10
    #The payment must be the same every month

#Bisection search
    #Start at the middle of the range: (starting_balance - (starting_balance / 12)) / 2
    #Calculate how many monthly payments it takes to pay off the balance
    #If it's less than 12, bisect the lower half
    #If it's more than 12, bisect the upper half

months_in_year = 12.0
payment_lower_bound = starting_balance / months_in_year
payment_upper_bound = starting_balance
monthly_ir = annual_ir / months_in_year
final_payment = payment_lower_bound
months_needed = 11
while True:
    payment = (payment_lower_bound + payment_upper_bound) / 2.0
    print 'Checking payment: ', payment
    balance = starting_balance
    month = 1
    while month < months_in_year:
        #Calculate interest
        interest = round(balance*monthly_ir, 2)
        balance += interest - payment
        #Increment month
        month += 1

    #If payment is too low, bisect the upper range, else, the lower range
    if balance > .02:
        print 'Payment too low. Balance after 12 months:', balance
        payment_lower_bound = payment
    elif balance < -.02:
        print 'Payment too high. Balance after 12 months:', balance
        payment_upper_bound = payment
    else:
        final_payment = payment
        months_needed = month
        break
    
print 'RESULT'
print 'Monthly payment to pay off the debt in 1 year:', final_payment
print 'Number of months needed:', months_needed
print 'Balance:', "$%s" % balance
