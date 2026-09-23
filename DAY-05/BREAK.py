#1
# for i in range(0,100):
#     if i==5:
#         break
#     print(i)

#2
# for i in range(1,100):
#     if i%5==0 and i%3==0:
#         break
#     print(i)

#3
# or_username='gopichand123'
# username=input('enter:')
# while or_username!=username:
#     username=input('enter:')

#     if or_username==username:
#         print('username is valid')
#         break
    
#4
# a=input('enter:')
# for i in a:
#     if not('a'<=i<='z'):
#         print(f'{a} is not in lowercase')
#         break
# else:
#     print('it is lowercase')

#5
# i=1
# while i<=30:
#     if i%5==0:
#         i+=1
#         continue
#     if i%3==0:
#         print(i)
#     i+=1

#6
# a=int(input('enter:'))
# sum=0
# i=1
# while i<a:
#     if a%i==0:
#         sum+=i
#     i+=1
# if sum==a:
#     print('perfect')
# else:
#     print('not perfect')

#7
# a=input('enter:').split()
# b={}
# for i in range(0,len(a)):
#     if a[0]:
#         b[a[i]]=1
#     else:
#         b[a[i]]=0
# print(b)











# a=int(input('enter:'))
# b=True
# for i in range(2,a):
#     if a%i==0:
#         count+=1
#         if count>2:
#             break
# if count==2:
#     print('pm')
# else:
#     print('not')

# a=eval(input('enter:'))
# for i in range(0,len(a)):
#     if type(a[0])!=type(a[i]):
#         print('hetro')
#         break


# d=9,16,25
# for i in d:
#     sr=int(i**(1/2))
#     print(sr)

n=int(input("enter:"))
w=[]
for i in range(n):
    a=input()
    w.append(a)
max=w[0]

for j in w:
  if(len(j)>len(w[0])):
     max=j
  else:
     max=w[0]
print(f''' "{max}" is lrgest ''' )