import math

radians = float(input())
degrees = radians * 180 / math.pi  # last is always / to be accurate
print(round(degrees))
