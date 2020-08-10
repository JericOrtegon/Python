import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(10000)

def factorial (n):
    """ Calcula el factorial de n.

    n int > 0
    returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input("Escribe un número entero: "))

print(factorial(n))

if __name__ == "__main__":
    factorial(n)