n = float(input())
print("Units Consumed: %d" % n)

if n < 200:
    d = 1.20
    bill = d * n
    surcharge = 0
elif n>=200 and n < 400:
    d = 1.40
    bill = d * n
    surcharge = 0
elif  n>=400 and n < 600:
    d = 1.60
    bill = d * n
    surcharge = (15 / 100) * bill
elif  n>=600 and n < 800:
    d = 1.80
    bill = d * n
    surcharge = (15 / 100) * bill
else:
    d = 2.00
    bill = d * n
    surcharge = (15 / 100) * bill

total_amount = bill + surcharge

print("Cost per Unit: %.2f" % d)
print("Bill: %.2f" % bill)
print("Surcharge: %.2f" % surcharge)
print("Total Amount: %.2f" % total_amount)