
##function parameter is polynomial (float) from lowest exponent to greatest

def evaluate_poly(poly, x):
  polyLength = len(poly)
  total = 0.0
  for i in range(0, polyLength):
    total += poly[i] * x ** i
  return total

print evaluate_poly( (0.0, 0.0, 5.0, 9.3, 7.0), -13)