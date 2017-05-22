amount = float(input())
firstEx = input()
secondEx = input()
# current = amount
usd = 1.79549
eur = 1.95583
gbp = 2.53405

if firstEx == "USD":
    amount *= usd
elif firstEx == "EUR":
    amount *= eur
elif firstEx == "GBP":
    amount *= gbp

if secondEx == "USD":
    amount /= usd
elif secondEx == "EUR":
    amount /= eur
elif secondEx == "GBP":
    amount /= gbp

print('{0:.2f}'.format(amount), secondEx)
