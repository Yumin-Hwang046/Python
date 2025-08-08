#Tuple exercise

#3-1 다음과 같이 튜플 자료형이 선언됐을 때 두 번재 원소와 세 번째 원소의 합을 출력하세요.

#Sol 1
prices = (1000, 2000, 3000, 4000, 5000)
print(prices[1]+prices[2])

#Sol 2, Considering readability and reusability
price1 = prices[1]
price2 = prices[2]
total = price1 + price2
print(total)

#3-2 다음과 같이 튜플 자료형이 있을 떄, 두 번째 원소와 두 번째 원소의 가격을 출력해보세요.

fruits = (("apple", 1500),("grape", 2000),("pineapple", 3000))

#Sol 1
print(fruits[1])
print(fruits[1][1])

#Sol 2
fruit2 = fruits[1]
fruit2_price = fruit2[1]

print(fruit2)
print(fruit2_price)

#List exercise

#3-3 다음과 같이 리스트 자료형이 선언되었을 때 두 번째 원소와 세 번째 원소의 합을 출력하세요.

prices = [1000, 2000, 3000, 4000, 5000]

#Sol
price2 = prices[1]
price3 = prices[2]
total = price2 + price3
print(total)

prices.pop(1)
print(prices)
print(prices.pop(1))
prices.append('gfgsd')


#Dictionary exercise

#3-4 다음과 같이 딕셔너리 자료형이 선언되었을 때, apple과 banana 가격의 합을 출력하세요.

fruits = {"apple": 1000, "banana" : 1500, "pineapple": 2000}

#Sol
price_apple = fruits.get("apple")
price_banana = fruits.get("banana")
total = price_apple + price_banana
print(total)

#3-5 pineapple의 가격을 3000으로 변경하세요.

fruits["pineapple"] = 3000
print(fruits)

#3-6 딕셔너리 자료형 fruits가 선언되었을 때, 다음을 수행해보세요.
#조건 1) 가지고 있는 과일의 목록을 출력하세요.
#조건 2) 모든 과일의 가격 합과 평균을 구하세요.

fruits = {"apple": 1000, "banana": 1500, "pineapple": 2000}

#Sol
print(fruits)

price_a = fruits.get("apple")
price_b = fruits.get("banana")
price_p = fruits.get("pineapple")

total = price_a + price_b + price_p
average = total/3

print(total, average)

#Sol
fruits_list = list(fruits.keys())
print(fruits_list)

fruits_list = list(fruits.values())
print(sum(fruits_list))
print(sum(fruits_list)/len(fruits_list))

#3-7 학생들의 국어, 영어, 수학 성적이 다음과 같을 때, 학생 성적 산출 프로그램을 만들어봅시다.
#조건 1) 이름(키)과 과목별 점수(값)가 담긴 딕셔너리 자료형을 만드세요.
#조건 2) 각 학생별 평균 점수를 구하세요.
#조건 3) 국어, 영어, 수학 과목별 평균 점수를 구하세요.

#Sol1
Grade = {"가은":[82, 97, 88], "나영":[92, 87, 82], "다래":[84, 77, 94]}
print(Grade)

가은_average = sum(Grade["가은"])/len(Grade["가은"])
나영_average = sum(Grade["나영"])/len(Grade["나영"])
다래_average = sum(Grade["다래"])/len(Grade["다래"])
print(가은_average, 나영_average, 다래_average)

국어_total = Grade["가은"][0] + Grade["나영"][0] + Grade["다래"][0]
영어_total = Grade["가은"][1] + Grade["나영"][1] + Grade["다래"][1]
수학_total = Grade["가은"][2] + Grade["나영"][2] + Grade["다래"][2]

국어_average = 국어_total/len(Grade)
영어_average = 영어_total/len(Grade)
수학_average = 수학_total/len(Grade)

print(국어_average,영어_average,수학_average)

#Sol2
Grade1 = Grade["가은"]
Grade2 = Grade["나영"]
Grade3 = Grade["다래"]
print(sum(Grade1)/len(Grade1))
print(sum(Grade2)/len(Grade2))
print(sum(Grade3)/len(Grade3))

Grades = list(Grade.values())
print(Grades)

Kor = Grades[0][0] + Grades[1][0] + Grades[2][0]
Eng = Grades[0][1] + Grades[1][1] + Grades[2][1]
Mat = Grades[0][2] + Grades[1][2] + Grades[2][2]

print("국어 평균: ", Kor/3)
print("영어 평균: ", Eng/3)
print("수학 평균: ", Mat/3)
