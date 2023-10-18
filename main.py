from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
  """ Determines if a number is even and return an even list.
  Args:

  int_list: A list of integer.

  Returns:

  A list of even integers. 
  """
  # TODO: Implement even_list 
  pass

# Skeleton code for sum_of_squares_of_even 
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """ Computes the sum of the squares of all even numbers in a list of integers.

    Args:
        even_int_list: A list of even integers.

    Returns:
        The sum of the squares of all even numbers in the list.
    """
    # Initializing a variable to keep track of the sum
    sum_squares = 0
    
    # Iterating through each even integer in the list
    for number in even_int_list:
        # Squaring the integer and accumulating the sum
        sum_squares += number ** 2
    
    # Returning the sum of squares of even integers
    return sum_squares


# Main function 
def main():
# Example list
  int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_int_list = even_list(int_list)
  output = sum_of_squares_of_even(even_int_list)
  print(output)

# Boilerplate code 
if __name__ == "__main__":
  main()
