def fib(n):
  a, b = 0, 1 #tuple
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()

fib(1000)