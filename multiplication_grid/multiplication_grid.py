for i in range(0,13):#A for loop with a range of numbers from 0-12
	for j in range(0,13):#A nested loop also with a range from 0-12
		print(i*j, end='\t') #By multiplying i and j after establishing the two loops with a 0-12 range a 0-12 multiplication table is established
	print(' ')               #end was added to help shape multiplication by presenting the information horizontally/vertically, almost like a grid as opposed to solely vertically. 
                            #'\t' was added to end parameter to help clean up the overall look by adding space between numbers while still keeping information as a grid.
                            #print('') on line 4 was added to establish the grid as 12x12, adding a new line after each set of 12 numbers.