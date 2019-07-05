Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=list(input())
k=0
while(j<len(x)):
    temp=x[k]
    x[k]=x[k+1]
    x[k+1]=temp
    k+=2
print("".join(x))
