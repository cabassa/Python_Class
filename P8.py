class ComplexNumber(object):
    def __init__(self, a=0,b=0): #inicializacion de valores
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + " + " + str(self.b) + "i"

    def conjugate(self):
        return ComplexNumber(self.a, -1*self.b)

    def add(self, N):
        return ComplexNumber(self.a+N.a, self.b+N.b)

    def subtract(self, N):
        real = self.a - N.a
        imaginary = self.b - N.b
        return ComplexNumber(real, imaginary)

# Value for variables
C1 = ComplexNumber(2,4)
C2 = ComplexNumber(-9,20)

print "Complex Number:"
print "C1: ",C1
print "C2: ",C2
print
print "Conjugate result:"
print "C1: the conjugate is:", C1.conjugate()
print "C2: the conjugate is:", C2.conjugate()
print
print "Addition result:"
print "C1 + C2:", C1.add(C2)
print "C1 + C1.conjugate()", C1.add(C1.conjugate())
print
print "Subtraction result"
print "C1 - C2:",C1.subtract(C2)


