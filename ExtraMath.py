import math

class ExtraMath:

    def binomial(self, n, i):

        return math.factorial(n) / (math.factorial(i) * math.factorial(n-i))
