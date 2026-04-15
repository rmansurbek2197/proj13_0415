# 56
class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        while self.b:
            self.a, self.b = self.b, self.a % self.b
        return self.a

a, b = map(int, input().split())
print(GCD(a, b).solve())

# 57
class LCM:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        x, y = self.a, self.b
        while y:
            x, y = y, x % y
        return self.a * self.b // x

a, b = map(int, input().split())
print(LCM(a, b).solve())

# 58
class Factorial:
    def __init__(self, n):
        self.n = n
    def solve(self):
        res = 1
        for i in range(1, self.n+1):
            res *= i
        return res

print(Factorial(int(input())).solve())

# 59
class Fibonacci:
    def __init__(self, n):
        self.n = n
    def solve(self):
        a, b = 0, 1
        for _ in range(self.n):
            a, b = b, a+b
        return a

print(Fibonacci(int(input())).solve())

# 60
class Armstrong:
    def __init__(self, n):
        self.n = n
    def solve(self):
        s = str(self.n)
        return sum(int(d)**len(s) for d in s) == self.n

print(Armstrong(int(input())).solve())
