def fizzbuzz (n):
  for num in range (1, n):
    if num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    elif num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")
    else:
      print(num)

fizzbuzz(100)
