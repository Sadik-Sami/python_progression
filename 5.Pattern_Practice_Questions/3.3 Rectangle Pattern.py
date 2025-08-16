def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.

    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Initialize an empty list to store the rows of the rectangle
    rectangle = []

    # Loop through each row from 1 to n
    for _ in range(n):
        # Create a row with m stars
        row = "*" * m
        # Add the row to the rectangle list
        rectangle.append(row)

    # Return the list of rectangle rows
    return rectangle


rectangle = generate_rectangle(3, 4)
print(rectangle)
