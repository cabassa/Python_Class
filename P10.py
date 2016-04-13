print "Salida primer codigo practico"
animals = ['cat','dog','mouse','cow','shack','tiger','elephant']
for animallist in animals:
    print animallist

print
print "Salida segundo codigo practico"
horizontal = ''
for animallist in animals:
    horizontal = horizontal + ' ' + animallist
print horizontal

print
print "Tercer codigo practico"
ages = [18,21,14,7,90,12,30,45,23,33,22,5]
total_age = 0
for age in ages:
    total_age += age
print "Edad total :", total_age
print "average age:", total_age/len(ages)
print "Len        :", len(ages)