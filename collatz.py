Last login: Mon Jul 15 21:43:45 on ttys005
(base) Kaylees-MacBook-Pro:~ kayleeasai$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def Collatz(Num):
...     if Num % 2 == 0:
...         Num = Num // 2
...         return Num
...     elif Num % 2 == 1:
...         Num = 3*Num+1
...         return Num
... 
>>> try:
...     print('Enter any number besides 1')
...     Num=int(input())
...     while Num != 1:
...         if Num != 1:
...             Num = Collatz(Num)
...             print(Num)
...         elif Num == 1:
...             print("The number is 1")
... except ValueError:
...     print("Retry with a valid integer")
...     print('Enter any number besides 1')
...     Num=int(input())
...     while Num != 1:
...         if Num != 1:
...             Num = Collatz(Num)
...             print(Num)
...         elif Num == 1:
...             print("The number is 1")
... 
Enter any number besides 1
cat
Retry with a valid integer
Enter any number besides 1
3
10
5
16
8
4
2
1
>>> 


