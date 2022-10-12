import numpy
a = numpy.array([1, 2], float)
b = numpy.array([0, 1], float)
a1 = a**2
b1 = b**2
cos = numpy.dot(a, b)/numpy.dot(a1, b1)
sin = numpy.sqrt(1-cos**2)
print(sin)