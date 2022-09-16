import math

'''

def r(a, n):
    re = a**n
    return re
a =6
n= 2
print(a,n , "a**n =", r(a,n))



for i in range(2,11):
    x = i ** 0.5
    print( i," is x**2, x = ? ", x)


for i in range(11):
    print( 1<<i , end=' ')



n = int(input("input n"))
if(n>100):
    print("n>100")
else:
    print("n<=100")


n1 = 5
n2 = 6

print(bin(n1), "&", bin(n2),bin(n1&n2))
print(bin(n1), "|", bin(n2),bin(n1|n2))
print(bin(n1), "^", bin(n2),bin(n1^n2))

a = int(input("a : "))
b = int(input("b : "))
print(" a/b 's mok = ", a//b)
print(" a / b ", a%b)



num = int(input("num : "))
print(num//100)
print((num%100)//10)
print((num%10))



num = int(input("num : "))
print((num%10))
print((num%100)//10)
print(num//100)


num = int(input("num : "))
a = num%10
b = (num%100)//10
c = num//100
num2 = a*100 + b*10 + c
print(num2)



av = float(input("km/h : "))
hour = float(input("h : "))
print("arg v = :", av,"km/h")
print(" h : ",hour//1,"시간",int((hour%1)*60//1),"분",int(((hour%1)*60%1)*100),"초")
print(" s = ", hour*av,"km" )


x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

print("range : ", math.sqrt((x1-x2)**2 + (y1-y2)**2))



x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
#???

'''
pi = math.pi

print("1 : ", 13**3)
print("2 : ", 22**3)
print("3 : ", 17*25*16)
print("4 : ",10*10*pi*15/3)
print("5 : ", pi*(25**3)*4/3)
print("6 : ", pi*10*10*15)