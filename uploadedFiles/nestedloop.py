# first define area function that calculates area for given length and breadth

 #Remember that i could put anything inside the parentheses here, for eg. def area(l,b) or def area(i,j)
 #by writing def area(length, breadth), it makes easier for anyone to read your function
 #and understand what's going on.
 #Also, I needed to supply those two parameters (lengh and breadth) here because for
 # the function to calculate area, it has to know those two values.
 # If I was writing a function to calculate Volume, it would have been def Volume(l,b,h)

def area(length, breadth):
	return length * breadth
	
# now let's print out that table
def main():
    for i in range (1,12,1): #because we have to calculate both 1 and 11 including
        for j in range (1,12,1): # Note the indentation here.
            print "length: ", i, "breadth: ", j, "Area is: ", area(i,j)
            
main()

# What happens in the Nested loop (inside main() function above)?
# Nested loops are what they say they are. One loop is nested inside another loop.

""" Inside a nested loop, first the first loop runs once and the second loop runs its entire course.
For example, above, first i is set to 1 and then the loop goes to second line where j will 
go through its entire course. Meaning for i= 1, j will go through j = 1, j = 2, j = 3... until j loop
runs its course (which in this case is upto 11).
Then the j loop ends.
Then, it goes back up to i where i is now set to 2.
Then the loop goes to j line and its goes through 1 to 11 again.
So, basically, for every value of i, j goes through all eleven of its values.

If any of this does not make sense, ask Babu. It is best to be crystal clear about these
fundamental principles. """
