def absolute(N):
    if N < 0:
        return -1 * N
    else:
        return N

    print "|-1| = ", absolute(-1)
    print "|100| = ",absolute(100)
    print "|0| = ", absolute(0)


x = 9
if x < 0:
    print "negative"
elif x == 0:
    print "Zero"
else:
    print "positive"



x = 0
if x < 0:
    print 'negative'
elif x == 0:
    print 'zero'
else:
    print 'positive'

##############################TAX EXAMPLE###########################

def get_tax_amount(salary):
    if salary < 20000:
        return 0
    elif salary >= 20000 and salary < 50000:
        return salary*0.15
    elif salary >= 50000 and salary < 100000:
        return salary *0.20
    else:
        return salary*0.33

print "bob tax -", get_tax_amount(30000)
print "jill tax- ", get_tax_amount(45000)
print "Apu tax - ", get_tax_amount(13000)
print "Tom tax - ", get_tax_amount(17000)



