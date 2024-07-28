num = int(input("Enter a no.: "))
if num < 0:
   print("Enter a positive no.")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)