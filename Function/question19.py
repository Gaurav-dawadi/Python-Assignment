"""Write a Python program to create Fibonacci series upto n using Lambda."""

        
fib = lambda n: n if n<=1 else fib(n-1)+fib(n-2)
# print(fib(10))
print("The Fibonacci Series is :")
for i in range(10):
    print(fib(i))
