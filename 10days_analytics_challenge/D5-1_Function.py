#Numpy exercise

#5-1 random 클래스를 사용하여 0부터 100 사이의 정수 20개를 반환받아 리스트를 구성하고, 
# 이 리스트에 포함된 원소의 합계, 평균, 최소, 최대, 표준편차 등의 기술통계량을 구해보세요.
#HINT random 클래스의 sample(sequence, k) 함수를 사용하면 sequence 범위까지 k개의 랜덤 숫자를 반환받을 수 있습니다.

#Sol

import numpy

import random

rand_list = random.sample(range(100), 20)

rand_list_sum = numpy.sum(rand_list)
rand_list_average = numpy.average(rand_list)
rand_list_min = numpy.min(rand_list)
rand_list_max = numpy.max(rand_list)
rand_list_std = numpy.std(rand_list)

print(rand_list)
print(rand_list_sum)
print(rand_list_average)
print(rand_list_min)
print(rand_list_max)
print(rand_list_std)

#Sol2

import numpy

import random

rand_list = []

for i in range(20):
    rand_list.append(random.randint(0,100))

rand_list_sum = numpy.sum(rand_list)
rand_list_average = numpy.average(rand_list)
rand_list_min = numpy.min(rand_list)
rand_list_max = numpy.max(rand_list)
rand_list_std = numpy.std(rand_list)

print(rand_list)
print(rand_list_sum)
print(rand_list_average)
print(rand_list_min)
print(rand_list_max)
print(rand_list_std)

#5-2 철수의 1월부터 6월까지 수입액과 지출액은 다음과 같다.
#  철수는 수입액 중 지출액을 제외한 나머지 금액은 저축합니다.
#  1년 간 철수의 수입액, 지출액, 저축액의 기술통계(합계, 평균, 최솟값, 최댓값, 표준편차)를 산출해보세요.

#      수입액       지출액
# 1   2323000     1230000
# 2   2702000     1402530
# 3   2234000      904000
# 4   3001000     1123300
# 5   3023000     1007000
# 6   2623100     1805000



Jan_income = 2323000
Feb_income = 2702000
Mar_income = 2234000
Apr_income = 3001000
May_income = 3023000
Jun_income = 2623100

income = [Jan_income, Feb_income, Mar_income, Apr_income, May_income, Jun_income]



Jan_expenditure = 1230000
Feb_expenditure = 1402530
Mar_expenditure = 904000
Apr_expenditure = 1123300
May_expenditure = 1007000
Jun_expenditure = 1805000

expenditure = [Jan_expenditure, Feb_expenditure, Mar_expenditure, Apr_expenditure, May_expenditure, Jun_expenditure]

Jan_save = income[0] - expenditure[0]
Feb_save = income[1] - expenditure[1]
Mar_save = income[2] - expenditure[2]
Apr_save = income[3] - expenditure[3]
May_save = income[4] - expenditure[4]
Jun_save = income[5] - expenditure[5]

save = [Jan_save, Feb_save, Mar_save, Apr_save, May_save, Jun_save]

print("income analysis report______________________________")

income_sum = numpy.sum(income)
income_average = numpy.average(income)
income_min = numpy.min(income)
income_max = numpy.max(income)
income_std = numpy.std(income)

print("the total income: ", income_sum)
print("The average of income: ", income_average)
print("The min of income: ", income_min)
print("The max of income: ", income_max)
print("The standard deviation of income: ", income_std)

print("expenditure analysis report______________________________")

expenditure_sum = numpy.sum(expenditure)
expenditure_average = numpy.average(expenditure)
expenditure_min = numpy.min(expenditure)
expenditure_max = numpy.max(expenditure)
expenditure_std = numpy.std(expenditure)

print("the total expenditure: ", expenditure_sum)
print("The average of expenditure: ", expenditure_average)
print("The min of expenditure: ", expenditure_min)
print("The max of expenditure: ", expenditure_max)
print("The standard deviation of expenditure: ", expenditure_std)

print("save analysis report______________________________")

save_sum = numpy.sum(save)
save_average = numpy.average(save)
save_min = numpy.min(save)
save_max = numpy.max(save)
save_std = numpy.std(save)

print("the total save: ", save_sum)
print("The average of save: ", save_average)
print("The min of save: ", save_min)
print("The max of save: ", save_max)
print("The standard deviation of save: ", save_std)

#Sol_Book

income = [2323000, 2702000, 2234000, 3001000, 3023000, 2623100]
spending = [1230000, 1402530, 904000, 1123300, 1007000, 1805000]

save = []

for i in range(6):
    save.append(income[i]-spending[i])

print("monthly income: ",income)
print("income's sum/average/min/max/standard deviation is: ", numpy.sum(income),"/", numpy.average(income),"/", numpy.min(income),"/", numpy.max(income),"/", numpy.std(income))

print("monthly spending: ", spending)
print("spending's sum/average/min/max/standard deviation is: ", numpy.sum(spending),"/", numpy.average(spending),"/", numpy.min(spending),"/", numpy.max(spending),"/", numpy.std(spending))

print("monthly save: ", save)
print("save's sum/average/min/max/standard deviation is: ", numpy.sum(save),"/", numpy.average(save),"/", numpy.min(save),"/", numpy.max(save),"/", numpy.std(save))

#Function exercise

#5-3 문자열과 반복 횟수를 입력받으면, 해당 문자열을 입력받은 횟수만큼 출력하는 함수릏 작성해보세요.

#Sol

def print_string(str, n):
    for i in range(n):
        print(str)

if __name__ == '__main__':
    string = input("Enter the string: ")
    num = int(input("Enter the number of loop: "))
    print_string(string, num)

#Sol_Book

def PrintRepeatedly():
    text = input()
    n = int(input())
    for i in range(n):
        print(text)

if __name__ == '__main__':
    PrintRepeatedly()

#5-4 사용자로부터 값을 입력받으면, 구구단을 출력하는 함수를 작성해보세요.

#Sol

def multiplication_table(a):
    for i in range(1,10):
        print(a, " * ", i, " = ", a * i)

if __name__ == '__main__':
    num = int(input("Enter the number for multiplication table: "))
    multiplication_table(num)

#Sol_Book

def showMultiplicationTable():
    n = int(input())
    for i in range(1,10):
        print(n, " * ", i, " = ", n*i)

if __name__ == '__main__':
    showMultiplicationTable()