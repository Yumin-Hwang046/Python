#4-16 다음 조건을 만족시키기 위해 반복문을 사용하여 별을 출력하는 프로그램을 작성해보세요.

# 조건 1) 별의 가로 좌표와 세로 좌표의 값이 같습니다.

#Sol

for i in range(0,5):
    star = ""
    for j in range(0,5):
        if i == j:
            star += "*"
        else:
            star += " "
    print(star)

#Sol_Book

for i in range(5):
    for j in range(5):
        if i == j:
            print("*")
            break
        else:
            print(" ", end = "")

# 조건 2) 한 줄에 나타나는 별과 공백의 전체 길이는 일정합니다.

#Sol

for i in range(5):
    star = ""
    for j in range(5):
        if i <= j:
            star += "*"
        else:
            star += " "
    print(star)

#Sol_Book

for i in range(5):
    for j in range(i):
        print(" ", end = "")
    for j in range(5 - i):
        print("*", end = "")
    print()

# 조건 3) 공백은 하나씩 줄어들고 별은 두 개씩 늘어납니다.

#Sol

for i in range(5):
    for j in range(5-i):
        print(" ", end = "")
    for j in range(i):
        print("*"*((2*i)+1), end = "")
    print()

#Sol_Book

for i in range(1,6):
    for j in range(5-i):
        print(" ", end ="")
    for j in range(1, i * 2):
        print("*", end = "")
    print()



