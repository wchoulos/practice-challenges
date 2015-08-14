# July 17th Challenge The Heighway Dragon Fractal
#
# Write a program to print out the (x, y) coordinates of each point in the nth iteration of the Heighway dragon fractal . Start at the origin (0, 0) and take steps of length 1, 
# starting in the positive x direction (1, 0), then turning to the positive y direction (1, 1). Your program should generate 2n + 1 lines of output.
# You can use any resources you want for help coming up with the algorithm, but if you want to start from the very beginning, use only the fact that the nth iteration can be made 
# by folding a strip of paper in half n times, then unfolding it so that each crease is at a right angle .

# My idea using this method is to later make it very easy to draw the fractal in pygame, as well as
# not having to store any coords. Run time likely not optimal. Using helpers makes it cleaner but slows it down here. 
# TODO: Add pygame to draw the fractal. 


def move_forward(coords, orientation):
	if orientation == 0:
		return [coords[0]+1,coords[1]]
	elif orientation == 1:
		return [coords[0],coords[1]+1]
	elif orientation == 2:
		return [coords[0]-1,coords[1]]
	else:
		return [coords[0],coords[1]-1]

def list_of_turns(prev):
	right = 0
	left = 1
	tail = []
	for direction in reversed(prev):
		if(direction == right):
			tail.append(left)
		else:
			tail.append(right)
	return prev + [right] + tail

def print_n(iterations):
	#print the origin
	print(0, 0)
	#variables
	right = 0
	left = 1
	orientation = 0 # Key for directions: 0 == East; 1 == South; 2 == West; 3 == North
	curr_coords = [0,0]
	folds = [0]
	coord_sums = [0,0]
	#base case
	if(iterations == 1):
		base_case = [[1,0], [1,1]]
		for coord in base_case:
			print(coord[0], coord[1])
		return
	for N in range(1, iterations): 
		folds = list_of_turns(folds)
		N += 1
	for direction in folds:
		curr_coords = move_forward(curr_coords, orientation)
		print(curr_coords[0], curr_coords[1])
		coord_sums[0] += curr_coords[0]
		coord_sums[1] += curr_coords[1]
		if direction == right:
			orientation = (orientation + 1) % 4
		else:
			orientation = (orientation - 1) % 4
	curr_coords = move_forward(curr_coords, orientation)
	print(curr_coords[0], curr_coords[1])
	coord_sums[0] += curr_coords[0]
	coord_sums[1] += curr_coords[1]
	return coord_sums

