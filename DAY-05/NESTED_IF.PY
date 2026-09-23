
#! 1
# username=input('enter username:')
# user='Gopi'
# pswd='Gopi@0320'
# password=input('enter a password:')
# if(user==username):
#     if(password==pswd):
#         print("LOGIN SUCCESFULLY.....!")   

#! 2
# lst=eval(input('enter a list:'))
# if(type(lst)==list):
#     if(len(lst)%2!=0):
#         mid=len(lst)//2
#         if(type(lst[mid]))==str:
#             print(lst[mid])
#         else:
#             print('it is not a string')
#     else:
#         print('length is even')
# else:
#     print('it is not list')

#! 3
# a=input('enter a char:')
# if 'a'<=a<='z' or 'A'<a<='Z':
#     if a in 'aeiouAEIOU':
#         print('it is VOWEL')
#     else:
#         print('it is consonant')

#! 4
# a=eval(input('enter a list:'))
# if(type(a)==list):
#     if(type(a[-1]==str)):
#         if a[-1][0] in 'aeiouAEIOU':
#             if(a[-1]==a[-1][::-1]):
#                 print(a[-1])

#! 5

# a=input('enter a string:')
# if a[0] in 'AEIOUaeiou' and a[-1] not in 'AEIOUaeiou':
#     if len(a)%2!=0:
#         print(a[::-1])