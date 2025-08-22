#Operation exercise

#2-1 3과 12를 더한 값을 출력해보세요.

print(3 + 12)

#2-2 32를 5로 나눈 정수 몫과 나머지를 구해서 출력해보세요.

print(32 // 5)
print(32 % 5)

#2-3 22가 19보다 큰 지 출력해보세요.

print(22 > 19)

#2-4 5^3이 3^5보다 큰 지 출력해보세요.

print(5**3 > 3**5)

#2-5 254는 3의 배수인지 연산을 통해 알아보세요.

print(254 % 3 == 0)




#Variable exercise

#2-6 3과 12를 더한 값을 출력해보세요. 변수는 하나만 선언하고 print() 함수의 인수로 해당 변수만 사용하여 출력하세요.

n = 3 + 12
print(n)

#2-7 두 변수에 3과 12를 각각 대입하고, 두 변수를 더한 값을 출력해보세요.
#  변수는 두 개만 선언하고 print() 함수의 인수로 해당 변수만 사용하여 출력하세요.

a = 3
b = 12
print(a + b)

#2-8 두 변수에 3과 12를 각각 대입하고, 두 변수를 더한 값을 세 번째 변수에 대입하여 출력해보세요.
#  변수를 세 개 선언하고 print() 함수의 인수로 세 번째 변수만 사용하여 출력하세요.

a = 3
b = 12
c = a + b
print(c)




#Data Type exercise

#2-9 첫 번째 변수에 문자열 37을 대입하고, 두 번째 변수에 정수형 5를 대입하여 두 값을 더한 연산의 결과를 출력하세요.

a = "37"
b = 5
print(int(a) + b)

#2-10 문자열 변수 하나를 인수로 하여 print() 함수를 호출한 다음 그림과 같이 Hello와 World를 한 줄씩 출력해보세요.

text = "Hello\nworld"
print(text)

#2-11 변수 선언 없이 이스케이프 시퀀스와 print() 함수만 사용하여 다음과 같이 출력해보세요.

print('\"What\" is your name?')

#2-12 다음 그립과 같이 선언된 age 변수를 사용하여 Mike is 10 years old.를 출력할 수 있도록 print() 함수의 인수를 채워보세요.

age = 10
print(f"Mike is {age} years old.")
print("Mike is " + str(age) + " years old.")