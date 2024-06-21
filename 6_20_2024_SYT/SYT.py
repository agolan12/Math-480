import itertools
import random

def is_valid_SYT(candidate):
  """
  Check if the given candidate tableau is a valid standard Young tableau.

  Parameters:
  - candidate (Tuple[Tuple[int]]): The tableau to be checked.

  Returns:
  - bool: True if the matrix is valid, False otherwise.

  The function checks if the given matrix is a valid SYT matrix by verifying that:
  1. The elements in each column are in strictly increasing order.
  2. The elements in each row are in strictly increasing order.

  Example:
  >>> is_valid_SYT(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
  True
  >>> is_valid_SYT(((1, 2, 3), (5, 4), (6))
  False
  """
  for T in candidate:
    for i in range(len(T) - 1):
      if T[i] >= T[i + 1]:
        return False
  for i in range(len(candidate) - 1):
    top = candidate[i]
    bottom = candidate[i + 1]
    for j in range(len(bottom)):
      if top[j] >= bottom[j]:
        return False
  return True
    

def reshape_perm(perm, shape):
  """
  Reshapes a permutation into a tableau based on the given shape.

  Parameters:
  - perm (Tuple[int]): The permutation to be reshaped.
  - shape (Tuple[int]): The shape of the resulting tableau as a weakly decreasing tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A tuple of tuples representing the reshaped permutation as a tableau.

  Example:
  >>> reshape_perm((1, 2, 3, 4, 5, 6), (3, 2, 1))
  ((1, 2, 3), (4, 5), (6,))
  """
  output = tuple()
  index = 0
  for lvl in shape:
    row = []
    for i in range(lvl):
      row.append(perm[index])
      index += 1
    output += (tuple(row),)
  return output

def SYTs(shape):
  """
  Generates SYTs (Standard Young Tableaux) of on the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYTs as a tuple of integers.

  Returns:
  - List[Tuple[Tuple[int]]]: A list of valid SYTs generated based on the given shape.

  Example:
  >>> SYTs((2, 1))
  [((1, 2), (3,)), ((1, 3), (2,))]
  """

  n = sum(shape)
  results = []
  for perm in itertools.permutations(range(1, n + 1)):
    if is_valid_SYT(reshape_perm(perm, shape)):
      results.append(reshape_perm(perm, shape))
  return results

def random_SYT(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  This function generates a random permutation of numbers from 1 to n+1, where n is the sum of the elements in the `shape` tuple. It then reshapes the permutation into a tableau using the `reshape_perm` function. If the resulting tableau is not valid, it shuffles the permutation and tries again. The function continues this process until a valid SYT is found, and then returns the reshaped permutation as a tableau.

  Example:
  >>> random_SYT((2, 1))
  ((1, 2), (3,))
  """
  perm = []
  for i in range(1,sum(shape) + 1):
    perm.append(i)
  random.shuffle(perm)
  while not is_valid_SYT(reshape_perm(tuple(perm), shape)):
    random.shuffle(perm)
  return reshape_perm(tuple(perm), shape)
  

def random_SYT_2(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  The function generates a random SYT by starting off with the all zeroes tableau and greedily filling in the numbers from 1 to n. The greedy generation is repeated until a valid SYT is produced.

  Example:
  >>> random_SYT_2((2, 1))
  ((1, 2), (3,))
  """
  size = sum(shape)
  tableau = []
  lvl = 0
  for row_length in shape:
    tableau.append([])
    for i in range(row_length):
      tableau[lvl].append(0)
    lvl += 1
  for i in range(1, size + 1):
    square_options = valid_squares(tableau)
    coordinates = random.choice(square_options)
    tableau[coordinates[0]][coordinates[1]] = i
  output = []
  for row in tableau:
    output += (tuple(row),)
  return tuple(output)


"""
parameters:
  - tableau : input tableau
returns:
  - list of tuples of valid squares in the tableau where the next element can be placed
"""
def valid_squares(tableau):
  output = []
  lvl = 0
  for row in tableau:
    for column in range(len(row)):
      if tableau[lvl][column] == 0:
        if lvl == 0 or tableau[lvl - 1][column] != 0:
          if column == 0 or tableau[lvl][column - 1] != 0:
            output.append([lvl, column])
    lvl += 1
  return output