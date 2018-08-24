# ========================================================================================== #
############
# FUNCTIONS
############

def num_loop (x, y, z):
    print "x is %d" % x

    while x < y:
        print "At the top x is %d" % x
        numbers.append(x)

        x += z
        print "Numbers now: ", numbers
        print "At the bottom x is %d" % x
    
    return numbers

# ========================================================================================== #

#########
# MAIN
#########

# VARIABLES
numbers = []

# Gain input from user
i = int(raw_input("Enter Starting Point: "))
y = int(raw_input("Enter End Point: "))
z = int(raw_input("Enter CHG Number: "))

# pass input to function call
results = num_loop(i, y, z)

print "The numbers: "
for num in numbers:
    print num
