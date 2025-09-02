#Data Analytics tutorial

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\hym49\Desktop\Python Workspace\Python\10days_analytics_challenge\유동인구데이터.csv", encoding = 'cp949',
                   usecols = ['일평균 유동인구'])

data_array = data.to_numpy()

minimum = np.min(data_array)
maximum = np.max(data_array)
summation = np.sum(data_array)
average = np.average(data_array)
stddev = np.std(data_array)

print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

data2 = [16, 18, 17, 15, 0, 16, 13, 20, 22, 17, 0, 21, 20, 15]

print(data2)

for i in range(0, len(data2)):
    if data2[i] == 0 and i > 0:
        data2[i] = (data2[i-1] + data2[i+1])/2

print(data2)

minimum = np.min(data2)
maximum = np.max(data2)
summation = np.sum(data2)
average = np.average(data2)
stddev = np.std(data2)

print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

#Data Analytics exercise

#6-1 Tutotial의 데이터(Data2)를 사용하여 '0'이라는 이상치 혹은 결측치가 있다면 해당 값은 제거한 후 기술통계를 산출해보세요.
#HINT 리스트의 첫 번쨰 해당 값을 삭제하기 위하여 remove() 함수를 사용하세요.

#Sol
import numpy as np

data2 = [16, 18, 17, 15, 0, 16, 13, 20, 22, 17, 0, 21, 20, 15]

NumOfZeros = 0

for i in range(0, len(data2)):
    if data2[i] == 0:
        NumOfZeros += 1

for i in range(0, NumOfZeros):
    data2.remove(0)

minimum = np.min(data2)
maximun = np.max(data2)
summation = np.sum(data2)
average = np.average(data2)
stddev = np.std(data2)

print(data2)
print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

#6-2 Data2 데이터를 사용하여 홀수 번째의 원소와 짝수 번째의 원소를 더한 값을 새로운 리스트에 추가합니다. 
# 새로운 리스트 원소의 개수는 기존 리스트 원소 개수의 절반이 됩니다. 새로운 리스트에 대한 기술통계를 산출해보세요.

#Sol

data2 = [16, 18, 17, 15, 0, 16, 13, 20, 22, 17, 0, 21, 20, 15]

data2_odd = []
data2_even = []

new_data2 = []

for i in range(0, len(data2), 2):
    data2_odd.append(data2[i])

for i in range(1, len(data2), 2):
    data2_even.append(data2[i])

for i in range(0, len(data2_odd)):
    new_data2.append(data2_odd[i]+data2_even[i])

minimum = np.min(new_data2)
maximun = np.max(new_data2)
summation = np.sum(new_data2)
average = np.average(new_data2)
stddev = np.std(new_data2)

print(new_data2)
print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

#Sol_Book

data2 = [16, 18, 17, 15, 0, 16, 13, 20, 22, 17, 0, 21, 20, 15]

new_data2 = []

for i in range(0, len(data2), 2):
    new_data2.append(data2[i]+data2[i+1])

minimum = np.min(new_data2)
maximun = np.max(new_data2)
summation = np.sum(new_data2)
average = np.average(new_data2)
stddev = np.std(new_data2)

print(new_data2)
print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

#6-3 예제[6-2]와 같은 절차를 수행하기에 앞서 해당 data 리스트의 0을 제거한 후 수행하도록 하는 코드를 작성해보세요.
#  그리고 새로운 리스트에 대한 기술통계를 산출해보세요.

data2 = [16, 18, 17, 15, 0, 16, 13, 20, 22, 17, 0, 21, 20, 15]

NumOfZeros = 0

for i in range(0, len(data2)):
    if data2[i] == 0:
        NumOfZeros += 1
    
for i in range(0, NumOfZeros):
    data2.remove(0)

new_data2 = []

for i in range(0, len(data2), 2):
    new_data2.append(data2[i]+data2[i+1])

minimum = np.min(new_data2)
maximun = np.max(new_data2)
summation = np.sum(new_data2)
average = np.average(new_data2)
stddev = np.std(new_data2)

print(new_data2)
print(minimum)
print(maximum)
print(summation)
print(average)
print(stddev)

#Data Analytics Tutorial2

import pandas as pd

data = pd.read_csv(r"C:\Users\hym49\Desktop\Python Workspace\Python\10days_analytics_challenge\시군별유동인구데이터.csv", encoding ='cp949',
                   usecols = ['년월', '출발지역명', '도착지역명', '20대남성 유입인구'])

print(data)

numOfVisitors = 0
    
for i in range(0, len(data)):
    if "2020-12" in data.loc[i][0] and "경기도 안양시" in data.loc[i][2]:
        numOfVisitors += float(data.loc[i][3])

print(numOfVisitors)

import numpy as np

numOfVisitors = []

for i in range(0, len(data)):
    if "2020-12" in data.loc[i][0] and "경기도 안양시" in data.loc[i][2]:
        numOfVisitors.append(data.loc[i][3])

print(np.min(numOfVisitors))
print(np.max(numOfVisitors))
print(np.sum(numOfVisitors))
print(np.average(numOfVisitors))
print(np.std(numOfVisitors))

numOfVisitors = []
originNames = []

for i in range(0,len(data)):
    if "2020-12" in data.loc[i][0] and "경기도 안양시" in data.loc[i][2]:
        numOfVisitors.append(data.loc[i][3])
        originNames.append(data.loc[i][1])

print(originNames[np.argmin(numOfVisitors)])
print(np.min(numOfVisitors))
print(originNames[np.argmax(numOfVisitors)])
print(np.max(numOfVisitors))

#6-4 앞선 Tutorial의 데이터를 사용하여, 20대남성과 20대여성의 합을 기준으로 2020년 12월 경기도 안양시 유동인구의 기술통계를 산출해보세요.

import pandas as pd

data = pd.read_csv(r"C:\Users\hym49\Desktop\Python Workspace\Python\10days_analytics_challenge\시군별유동인구데이터.csv", encoding = "cp949",
                   usecols = ['년월', '출발지역명', '도착지역명', '20대남성 유입인구', '20대여성 유입인구'])

print(data)

numOfVisitors = []

for i in range(0, len(data)):
    if "2020-12" in data.loc[i][0] and "경기도 안양시" in data.loc[i][2]:
        numOfVisitors.append(float(data.loc[i][3])+float(data.loc[i][4]))

import numpy as np

print(np.min(numOfVisitors))
print(np.max(numOfVisitors))
print(np.sum(numOfVisitors))
print(np.average(numOfVisitors))
print(np.std(numOfVisitors))

