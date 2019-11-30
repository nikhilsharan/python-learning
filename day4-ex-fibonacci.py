def fibonacci(n):
    f1 = 0
    f2 = 1
    print(f1, f2, end = " ")
    fib = 0
    for i in range(1,n):
        fib = f1 + f2
        f1 = f2
        f2 = fib
        print(fib, end = " ")
        
n = int(input("Enter a number for fibonacci series: "))

fibonacci(n)