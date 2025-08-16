def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []

    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create a row with i '*' characters and append it to the list
        triangle.append("*" * i)

    # Return the list of rows
    return triangle


triangle = generate_triangle(5)
print(triangle)
