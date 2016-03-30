def adder(N):
    i = 0 #counter
    accumulator = 0
    while (i < N):
        i = i + 1
        accumulator = accumulator + i
    return accumulator

#test
print "adder(5): ", adder(5)
print "adder(10): ", adder(10)

#
done = False
while not done:
    character = input("Enter some value:")
    if character.isdigit():
        print "Is digit"
    elif character.isalpha():
        print "Is letter"
    else:
        done = True

print "Thanks for using this program"