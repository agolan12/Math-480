import itertools

def parenthesizations(n):
  """
  Returns a set of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A set of strings, where each inner string represents a valid parenthesization of length n.
  
   Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """
  if n == 0:
    return {""}
  else:
    output = set()
    parenthesizations_helper("", n, n, output)
    return output

"""
res - result string
open - number of open parenthesis
close - number of close parenthesis
output - output set
"""
def parenthesizations_helper(res, open, close, output):
  if open == 0 and close == 0:
    output.add(res)
  else:
    if open > 0:
      parenthesizations_helper(res + "(", open - 1, close, output)
    if close != open:
      parenthesizations_helper(res + ")", open, close - 1, output) 

def product_orders(n):
  """
  Returns a set of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.
  
  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  if n == 0:
    return {""}
  elif n == 1:
    return {"?"}
  elif n == 2:
    return {"?*?"}
  else:
    # TODO
    pass

def permutations_avoiding_231(n):
  """
  Returns a set of permutations of length n avoiding the pattern 2-3-1.
  
  Parameters:
    n (int): The length of the permutation.
  
  Returns:
    A set of permutations of length n that do not contain the pattern 2-3-1.
  
  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    # TODO
    pass

def triangulations(n):
  """
  Returns a set of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
  
  Example:
  >>> triangulations(3)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    pass
    # TODO