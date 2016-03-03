from math import sqrt
def find_hypotenuse(a,b):
    a_square = a * a
    b_square = b * b
    result = sqrt(a_square + b_square)
    return result

leg1= 9
leg2= 12

hypotenuse = find_hypotenuse(leg1,leg2)
print
print "The hypotenuse is:", hypotenuse
print

def print_name(name):
    print 'Person name: ' + name

print_name('Jose')
print_name('Ned')


