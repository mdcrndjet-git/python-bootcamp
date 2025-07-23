def line_generator(number):
    """ Prints the following:
	    Line 1
	    Line 2
	    ...
	    Line number
    """
    for number in range(1, number + 1):
        print(f"Line {number}")


# Use the function once
line_generator(4)
