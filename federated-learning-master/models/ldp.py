import random
def ldp(data1,k):
  list = [data1 >> d & 1 for d in range(10)][::-1]
  while True:
    for i in range (2*k):
        n=random.randint(0,len(list)-1)
        if list[n]==0:
            list[n]=1
        else:
            list[n]=0
    decimal_number=0
    for j in range(len(list)):

        decimal_number += int(list[j]) * pow(2, j)
    if decimal_number<=255:
        break

  return(decimal_number)
#print(dec2bin(0.8125))
        # [1, 1, 0, 1]
#print(bin2dec(dec2bin(0.8125)))
        # 0.8125
'''x=40.9882
y=73.9116
X,Y=ldp(x,y,1)
d=((X-x)*(X-x)+(Y-y)*(Y-y))**0.5
print(d)
print(X)
print(Y)
#print(dec2bin(0.01,3))'''
pp=ldp(120,3)
print(pp)