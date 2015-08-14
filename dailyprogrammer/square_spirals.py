# Credit to /u/Cephian for inspiring a solution that searches concentric squares in the spiral for the given coordinate.
def spiral_value(side_length, coordinate):
	"""Given a spiral size and coordinate, return what point the coordinate is on the spiral.
		Params: side_length - an int representing the length of one side of the spiral
				coordinate - a tuple representing the ordered pair we are looking for
	"""
	if(side_length % 2 == 1):
		return "Invalid side length"
	# Insert a check to make sure the coordinate is within the spiral.
	# First we shift the coordinate to place the center of the spiral on the origin
	x = coordinate[0] - (side_length // 2) - 1
	y = coordinate[1] - (side_length // 2) - 1
	# k is the square the coordinate is located in, useful for locating the point on the 
	k = max(abs(x), abs(y))
	# a is the max value in that square
	a = pow((2 * k + 1), 2)
	if x == k:
		return (a - y - (7 * k))
	elif x == -k:
		return (a + y - (3 * k))
	elif y == k:
		return (a + x - k)
	else:
		return (a - x - (5 * k))
