print('Interesr Calculator: ')

amount = float(input('Principal amout ? '))

roi = float(input('Rate of Interest ? '))
yrs = int(input('Duration (no. of years) ? '))

total = (amount * pow(1 + (roi / 100), yrs))
interest = total - amount
print('\nInterest = %0.2f' %interest)

