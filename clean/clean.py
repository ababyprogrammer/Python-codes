def find_next_square(n):
    """
    Find the next square number that is greater than n.
    
    Parameters:
        n (int): A positive integer.
        
    Returns:
        int: The next square number that is greater than n.
        
    Examples:
        >>> find_next_square(4)
        9
        >>> find_next_square(9)
        16
    """
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer.")
    
    square_root = n ** 0.5
    
    if square_root.is_integer():
        return (square_root + 1) ** 2
    else:
        return n