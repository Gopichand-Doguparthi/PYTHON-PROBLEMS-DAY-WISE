# #1
# a=(input("enter a string:"))
# if (len(a)==5):
#     print("yes")

# #2
# a=int(input('enter:'))
# if a%2==0:
#     print('even')

# #3
# a=abs(int(input('enter:')))
# print(a)
# if (a>=10 and a<=99):
#     print("yes")

# #4
# a=int(input("enter:"))
# if a%3==0 and a%5==0:
#     print('yes')

#5
# a=input('enter:')
# if a[-1]=='p':
#     print('yes')

#6
# a=input('enter:')
# if a>='a' and a<='z':
#     print('yes')

#7
# a=set(input('enter:'))
# if a<{'a','e','i','o','u'}:
#     print('yes')

#8
# a=eval(input('enter:'))
# if type(a)==list:
#     print('yes')

#9
# a=eval(input('enter:'))
# if type(a)==float:
#     print("yes")

#10
# a=int(input('enter:'))
# if a>100:
#     print('yes')

#11
# a=input('enter:')
# if 'A'<=a<='Z':
#     print('yes')

#12
# a=eval(input('enter:'))
# if type(a)==int or type(a)==float or type(a)==complex or type(a)==bool:
#     print('yes')

#13
# a=input("enter:")
# if a[-1]=='a':
#     print("yes")

#14
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# if a<b:
#     print(a+b)

#15
# a=eval(input('enter:'))
# if type(a[-1])==list or  type(a[-1])==set or type(a[-1]) ==dict:
#     print('yes')

#16
# a=eval(input('enter:'))
# if type(a)==dict:
#     print('yes')

#17
# a=input('enter:')
# if a[0]==a[-1]:
#     print('yes')

#18
# a=(input('enter:'))
# if 'A'<=a<='Z' and a[-1] in '1234567890':
#     print('yes')


#if else programs:-

#1
# a=int(input('enter:'))
# if a%2==0:
#     print('square vale:',a**2)
# else:
#     print('cube value:',a**3)

#2
# a=eval(input("enter:"))
# if type(a) in [list,set,dict]:
#     print('mutable datatypes')
# else:
#     print('immutable datatypes')

#3
# a=(input('enter:'))
# if 'A'<=a<='Z' or 'a'<=a<='z' or a not in '1234567890':
#     print('not special')
# else:
#     print(' spl')

#4
# import keyword
# a=input('enter:')
# if a not in keyword.kwlist:
#     print(f' {a} is not keyword')
# else:
#     print(f' {a} is a keyword')

#5
# a=['sita','geetha','ramya','geetha sis']
# b=input('enter girl name:')
# print('hunting start!!!!')
# if b==a[0]:
#     print('accepted')
# elif b==a[1]:
#     print('accepted')
# elif b==a[2]:
#     print('aaccepted')
# elif b==a[3]:
#     print('aaccepted')
# else:
#     print('stay single!!!!!')

#IF -ELSE PROGRAMS:

#1
# a=input('enter a string:')
# if a[::-1]==a:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")

#2
# a=eval(input('enter tha value:'))
# if type(a) not in [set,list,dict]:
#     print(f'{a} is immutable')
# else:
#     print(f'{a} is immutable')

#3
# a=eval(input('enter tha value:'))
# if type(a)  in [int,float,complex,bool]:
#     print(f'{a} is sv')
# else:
#     print(f'{a} is not singlevalue')

# #4
# a=input('enter a string:')
# if len(a)>5:
#     print(a[0]+a[-1])
# else:
#     print(f"reverse of {a} is :",a[::-1])

#5
# a=eval(input('enter tha 1st input:'))
# b=eval(input('enter tha 2nd input:'))
# if b is a:
#     print('both pointing same address')
# else:
#     print('both not pointing same address')

#6
# a=eval(input('enter tha value:'))
# if type(a[0])==type(a[1]):
#     print(f'{a} is homogeneous tuple')
# else:
#     print(f'{a} is heterogeneous tuple')

#7
# a=eval(input('enter values:'))
# if len(a)%2==0:
#     print(a[1::2])
# else:
#     print(a[::2])

#8
# a=int(input('enter a number:'))
# if a>0:
#     print(f'{a} is positive number')
# else:
#      print(f'{a} is negative number')