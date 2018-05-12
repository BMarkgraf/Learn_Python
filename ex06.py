# # What is the difference between %r and %s?
# We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and others for displaying to users.

# What’s the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are for actually displaying variables to users.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'."  % y

hilarious = False
joke_eval = "Isn't that joke so funny?! %r"

# This is interesting in that is uses a variable with a %r in it 
# and then defines %r as variable hilarious
print joke_eval % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
