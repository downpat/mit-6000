balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_ir = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
min_pr = float(raw_input('Enter the minimum monthly payment rate as a decimal:'))

#Run the minimum payment simulation for 12 months
months = 12
total_paid = 0
for month in xrange(months):
    min_payment = round(min_pr * balance, 2)
    interest_paid = round(annual_ir / 12 * balance, 2)
    principle_paid = round(min_payment - interest_paid, 2)
    balance -= principle_paid
    total_paid += min_payment
    print 'Month:', month + 1
    print 'Minimum monthly payment:', "$%s" % min_payment
    print 'Principle paid:', "$%s" % principle_paid
    print 'Remaining balance:', "$%s" % balance

print 'RESULT'
print 'Total amount paid:', "$%s" % total_paid
print 'Remaining balance:', "$%s" % balance
