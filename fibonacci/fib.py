def fib(x):
  # Your code here
  if x <= 2:
      return 1
  else:
      return fib(x-2) + fib (x-1)
print(fib(7))
