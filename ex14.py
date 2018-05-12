from sys import argv

script, uname = argv

prompt = '>'

print "Hi %s, I'm the %s script." % (uname, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % uname, 
likes = raw_input(prompt)

print "Where do you live %s?" % uname
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
An you have a %r computer. Nice.
""" % (likes, lives, computer)
