# Defining variable x
x = "There are %d types of people." % 10
# Defining variable binary
binary = "birnary"
# Defining variable do_not
do_not = "don't"
# Defining variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# print line 2
print x
# print line 8
print y

# print Line 2 with additional string 
print "I said: %r." % x
# print Line 8 with additional string
print "I also said: '%s'." % y

#Defining variable
hilarious = False
#Defining variable 
joke_evaluation = "Isn't that joke so funny?! %r"
#Print Line 20 and 23
print joke_evaluation % hilarious

#Defining w and e variables
w = "This is the left side of..."
e = "a string with a right side."

#print line 28 and 29
print w + e