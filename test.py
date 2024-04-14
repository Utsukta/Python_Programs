def print_Kaprekar_nums(start, end):  
   for i in range(start, end ):  
      sqr = i ** 2  
      digits = str(sqr)  
  
      length = len(digits)  
      for x in range(1, length):  
         left = int("".join(digits[:x]))  
         right = int("".join(digits[x:]))  
         if (left + right) == i:  
            print("%s "%(str(i)), end = " ");  
  
print_Kaprekar_nums(1, 100000)  