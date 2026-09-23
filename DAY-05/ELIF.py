
#! ----ELIF PROGRAMS-------:

#1
# a=input('enter a character:')
# if 'A'<=a<='Z':
#     print(f"{a} is uppercase")
# elif 'a'<=a<='z':
#     print(f"{a} is lowercase")
# elif '0'<=a<='9':
#     print(f"{a} is number")
# else:
#     print(f"{a} is spl char")

#2
# a=eval(input('enter a list:'))
# if type(a)==list:
#     if len(a)%2!=0:
#         if type(a[len(a)//2])==str:
#             print(a[len(a)//2])
#         else:
#             print('middle value is not string')
#     else:
#         print('length is even')
# else:
#     print(f'{a} is not a list')

#3
# a=eval(input("enter a tuple:"))
# if type(a)==tuple:
#     if type(a[0])==str:
#         if len(a[0])>5:
#             if a[0]==a[0][::-1]:
#                 print('1st value:',a[0])
#             else:
#                 print("string is not palindrome")
#         else:
#             print('len is <5')
#     else:
#         print('not string')
# else:
#     print('not tuple')

#4
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# d=int(input("enter d:"))
# if a>b:
#     if a>c:
#         if a>d:
#             print(f'{a} is greatest number')
#         else:
#             print(f'{d} is greatest number')
#     elif c>d:
#         print(f'{c} is greatest number')
#     else:
#         print(f'{d} is greatest number')
# else:
#     if b>c:
#         if b>d:
#             print(f'{b} is greatest number')
#         else:
#             print(f'{d} is greatest number')
#     elif c>d:
#         print(f'{c} is greatest number')
#     else:
#         print(f'{d} is greatest number')

#1
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# c=int(input('enter c:'))
# if a>c:
#     print(f"{c} is smallest")
# elif a>b:
#     print(f"{b} is smallest")
# else:
#     print(f"{a} is smallest")

#2
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# c=int(input('enter c:'))
# if a<c:
#     print(f"{c} is greatest")
# elif a<b:
#     print(f"{b} is greatest")
# else:
#     print(f"{a} is greatest")

#3
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# if a>0 and b>0:
#     print('1st')
# elif a<0 and b>0:
#     print('2nd')
# elif a<0 and b<0:
#     print('3rd')
# else:
#     print('4th')

#4
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# if a>b:
#     print('a is greatest')
# elif a<b:
#     print('b is greatest')
# elif a<=b:
#     print('b is greatest or equal to a')
# elif a>=b:
#     print('a is greatest or equal to b')
# elif a==b:
#     print('a equal to b')
# elif a!=b:
#     print('a not equal to b')

#5
# a=int(input('enter:'))
# if a%3==0 and a%5==0:
#     print('fizzbuzz')
# elif a%3==0:
#      print('fizz')
# else:
#      print('buzz')

#NESTED IF:

#1
# a=int(input('enter:'))
# b=int(input('enter:'))
# c=int(input('enter:'))
# d=int(input('enter:'))
# if a>b and a>c and a>d:
#     if  b>c and b>d:
#         print(f'{b} is 2nd greatest')
#     elif  c>b and c>d:
#             print(f'{c} is 2nd greatest')
#     else:
#         print(f'{d} is 2nd greatest')
# elif b>a and b>c and b>d:
#     if  a>c and a>d:
#         print(f'{a} is 2nd greatest')
#     elif  c>a and c>d:
#          print(f'{c} is 2nd greatest')
#     else:
#          print(f'{d} is 2nd greatest')
# elif c>a and c>b and c>d:
#     if  a>b and a>d:
#         print(f'{a} is 2nd greatest')
#     elif  b>a and b>d:
#             print(f'{b} is 2nd greatest')
#     else:
#         print(f'{d} is 2nd greatest')
# else:
#     if  b>c and b>a:
#         print(f'{b} is 2nd greatest')
#     elif  c>b and c>a:
#             print(f'{c} is 2nd greatest')
#     else:
#          print(f'{a} is 2nd greatest')

