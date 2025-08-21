#For exercise

#enumerate

#4-4 for 반복문을 사용하여 0부터 20미만 짝수의 합을 구하세요.

#Sol
sum = 0

for i in range(0,20):
    if i % 2 == 0:
        sum += i

print(sum)

#Sol_Book
sum = 0
for i in range(0,20,2):
    sum += i
print(sum)

#4-5 for 반복문을 사용하여 10부터 1까지의 자연수를 역순으로 출력하세요.

#Sol
for i in range(0,10):
    num = 10
    num -= i
    print(num)

#Sol_Book
for i in range(10,0,-1):
    print(i)

#4-6 단일 for 반복문을 사룔하여 다음 모양을 출력해보세요.
#*
#**
#***

#Sol
for i in range(1,6):
    print('*'*i)

#Sol_Book
star = '*'
for i in range(0,5):
    star += '*'
    print(star)

#4-7 while 반복문을 활용하여 1부터 10까지 출력하세요.

#Sol
num = 0
while num < 10:
    num += 1
    print(num)

#Sol2
num = 1
while num < 11:
    print(num)
    num += 1

#Sol_Book
n = 0
while (n < 10):
    n += 1
    print(n)

n = 1
while (n <= 10):
    print(n)
    n += 1

#4-8 while 반복문을 사용하여 10부터 1까지 출력하세요.

#Sol
n = 10
while (n > 0):
    print(n)
    n -= 1

#4-9 while 반복문을 사용하여 1부터 10까지 자연수의 합을 구하세요.

#Sol
n = 1
sum = 0
while n < 11:
    sum += n
    n += 1
print(sum)

#Sol_Book
n = 0
sum = 0
while n < 10:
    n += 1
    sum += n
print(sum)

#4-10 while 반복문을 사용하여 다음과 같은 결과를 출력하세요.

#Sol
count = 0
star ='*'
while count < 5:
    count += 1
    print(star*count)

#Sol_Book
n = 0
star = ''
while (n < 5):
    n += 1
    star += '*'
    print(star)

#4-11 1부터 10 사이에 있는 임의의 두 정수의 곱을 연산하여 '20'이라는 결과가 나올 때까지 반복 실행하는 while 반복문을 작성하세요.

#Sol

import random
a = 0
b = 0
mul = 0
while (mul != 20):
    a = random.randint(1,10)
    b = random.randint(1,10)
    mul = a * b
    print(a,'*',b,'=',mul)

#Sol_Book

import random
n = 0
m = 0
while (n * m != 20):
    n = random.randint(1,10)
    m = random.randint(1,10)
    print(n,'*',m,'=',n*m)

#4-12 어떤 공장에서 생산품의 불량 여부를 판별하기 위한 방법으로 '무게'를 사용하고 있습니다. 생산품 무게의 범위는 8~17kg입니다.
# 무게가 10~15kg인 생산품은 양품이고, 10kg보다 가벼운 생산품의 경우 빠진 부품을 추가해주기 위해서 물건 번호를 출력해주며, 
# 15kg가 넘는 물건은 판별하는 기계에 부담이 될 수 있어 바로 기계를 종료하도록 합니다. 이를 수행하는 코드를 작성하세요.

#Sol_판별_machine

import random

product_num = 0
product_weight = 0

while product_weight < 15:
    product_num += 1
    product_weight = random.randint(8,17)

    if product_weight < 10:
        print('product',product_num, "you need to add the 부품")
    elif product_weight < 15:
        print('product',product_num,'is fine.')
    else:
        print('product',product_num, 'is too heavy, the machine stops.')

#Sol_Book

import random

index = 0
while True:
    index += 1
    m = random.randint(8,17)
    if m >= 10 and m <= 15:
        continue
    elif m < 10:
        print(index, ' is ',m, 'kg')
    else:
        print(index,' is ',m,' kg.')
        break


#4-13 우리가 사용하는 구구단은 9단까지 있지만 인도에서는 19단까지 있는 구구단을 사용한다고 합니다. 
# 앞서 작성한 구구단 코드를 19단으로 수정하여 출력해보세요.

#Sol

n = 2
while n < 20:
    i = 1
    while i < 20:  
        print(n,' * ',i,' = ',n*i)
        i += 1
    n += 1

#Sol_Book

for n in range(2,20):
    for m in range(1,20):
        print(n,' * ',m,' = ',n*m)

#4-14 강수 확률이 50% 이상이면 우산을 챙기고, 50% 미만이면 우산을 챙기지 않습니다. 
# 입력받은 강수 확률에 따라 우산을 챙겨야 할지 말아야 할지 구분하는 프로그램을 작성하세요.

#Sol

rain = int(input("What is the percent of today's rain coming: "))

if rain >= 50:
    print("It'll be raining today, take your umbrella.")
else:
    print("It'll be sunny today. leave your umbrealla at home.")

#Sol_Book

prob = float(input("Precipitation Probability: "))

if (prob >= 50.0):
    print("Take your umbrella")
else:
    print("No need to take an umbrealla")

#4-15 x와 y 변수가 있습니다. 입력받은 x와 y 값이 같을 때는 x and y are the same을 출력하고,
#  다르면 더 큰 값을 출력하는 프로그램을 작성하세요.

#Sol

x = float(input('Enter the x value :'))
y = float(input('Enter the y value :'))

if x == y:
    print("x and y are the same.")
else:
    if x > y:
        print("the bigger one is x(",x,")")
    else:
        print("the bigger one is y(",y,")")

#Sol_Book

x = float(input("Input value for X : "))
y = float(input("Input value for Y : "))

if x > y:
    print("x is greater than y" + str(x))
elif y > x:
    print("y is greater than x" + str(y))
else:
    print("x and y are the same.")

