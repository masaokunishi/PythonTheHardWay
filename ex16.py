from sys import argv

script, filename = argv

#1st prompt to erase the file
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#open the file being empty
print "Opening the file..."
target = open(filename, 'w')

#Make the file empty"
print "Truncating the file. Goodbye!"
target.truncate()

#Write something into the file
print "Now I'm going to ask you for these lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#Writing what you wrote
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#Close the file
print "And finally, we close it."
target.close()