def Collatz(Num):
     if Num % 2 == 0:
         Num = Num // 2
         return Num
     elif Num % 2 == 1:
         Num = 3*Num+1
         return Num
 
try:
     print('Enter any number besides 1')
     Num=int(input())
     while Num != 1:
         if Num != 1:
             Num = Collatz(Num)
             print(Num)
         elif Num == 1:
             print("The number is 1")
except ValueError:
     print("Retry with a valid integer")
     print('Enter any number besides 1')
     Num=int(input())
     while Num != 1:
         if Num != 1:
             Num = Collatz(Num)
             print(Num)
         elif Num == 1:
             print("The number is 1")


