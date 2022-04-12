def problem2():
  def gen(max):
    a, b = 1, 2
    while a < max:
      yield a
      a, b = b, a+b
  result = 0
  for n in gen(4000000):
    if n%2 == 0:
      result += n
  return result
