import doctest



def wears_jacket_with_if(temp,is_raining):
	"""
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
	return (temp < 60) or is_raining






doctest.testmod()