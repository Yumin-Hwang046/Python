#If exercise

#4-1 코로나 바이러스의 일일 감염자 수를 입력받아 다음과 같은 조건으로 위험 지수를 '보통','위험','매우 위험'으로 출력하는 코드를 작성해보세요
#조건) 1000명 미만 = 보통, 1000명 이상 10만명 미만 = 위험, 10만 명 이상 = 매우 위험

#Sol
DailyCovidCases = int(input('Enter the numeber of Daily Covid-19 cases: '))

if DailyCovidCases < 1000:
    print("보통")
elif DailyCovidCases < 100000:
    print("위험")
else:
    print("매우 위험")

#4-2 입력받은 금액으로 구매할 수 있는 비행기표에 해당하는 국가를 출력하는 프로그램을 작성하세요.(입력값은 만 원 단위이고, 단위 없이 숫자만 입력을 받습니다, 20만원 -> 20).
#조건) 
# 20만 원 미만 = 국내
# 20만 원 이상 50만 원 미만 = 일본, 중국, 홍콩, 괌
# 50만 원 이상 100만원 미만 = 베트남, 대만, 인도네시아, 말레이시아
# 100만 원 이상 = 미국, 유럽 등 모든 국가

#Sol
BudgetOfTicket = int(input("Enter the your budget for a plane ticket: "))

if BudgetOfTicket < 20:
    print("국내")
elif BudgetOfTicket < 50:
    print("일본, 중국, 홍콩, 괌")
elif BudgetOfTicket < 100:
    print("베트남, 대만, 인도네시아, 말레이시아")
else:
    print("미국, 유럽 등 모든 국가")

#AirFare = 항공료, input("Enter your air fair: ")

#4-3 어떤 학생이 국어, 영어, 수학 과목을 시험본 후 다음 조건과 같이 평균 점수에 따라 합격, 재시험, 불합격으로 구분하는 프로그램을 작성하세요.

#조건) 80.0점 이상 = 합격, 70.0점 이상 80.0점 미만 = 재시험, 70.0점 미만 = 불합격

#Sol
Kor = float(input("Enter your korean grade: "))
Eng = float(input("Enter your English grade: "))
Mat = float(input("Enter your math grade: "))
Average = (Kor + Eng + Mat)/3

print("Your average score is " + str(Average))

if Average > 80.0:
    print("PASS")
elif Average > 70.0:
    print("RETAKE")
else:
    print("FAIL")