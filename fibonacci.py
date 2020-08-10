def run():
    def fibonacci(n):
        """Este código hace las series de Fibonacci.
        n int > 0
        returns n fibonacci
        """
        if n == 0 or n == 1:
            return 1
            
        return fibonacci(n - 1) + fibonacci(n - 2)


    n = int(input("Introduce el numero de fibonacci que quieres generar: "))

    print(fibonacci(n))


if __name__ == "__main__":
    run()