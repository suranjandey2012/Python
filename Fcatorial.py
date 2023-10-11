def factorial(n): # Recursive version
   if n < 0:
      return -1 # Error condition
   print("Value of n ( @", hex(id(n)), ") = ", n)
   if n == 0 or n == 1:
      return 1 # Base case
   else:
      print ("Entering into factorial(", n-1, ")");
      return n * factorial(n-1) # Recursive call
factorial(5)