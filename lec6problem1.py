def evaluate_poly(poly, x): 
    """ 
	Computes the polynomial function for a given value x. Returns that value.
	Example:
	>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
	# f(x) = 7.0x**4 + 9.3x**3 + 5.0x**2 
	>>> x = -13 
	>>> print evaluate_poly(poly, x) 
	# f(-13) = 7.0(-13)**4 + 9.3(-13)**3 + 5.0(-13)**2 
	180339.9 
	poly: tuple of numbers, length > 0
	x: number 
	returns: float 
    """
    if len(poly) == 1:
		#base case
		return poly[0]
    else:
        #recursive case
        #the first item in the tuple is the coefficient of X**0, so it's the final value
        #the rest of the items in the tuple need multiplied by X and put in  new tuple
        #Yes, I'm cheating and casting a list to a tuple. GFY and your immutability.
        return poly[0] + evaluate_poly(tuple([x * coeff for coeff in poly[1:]]), x)

if __name__ == '__main__':
    print evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), -13)
	
