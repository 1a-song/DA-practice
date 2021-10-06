# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
###python 기본문법 이해를 위한 pandas, numpy 없이 시각화
# -

import csv
import matplotlib.pyplot as plt

# +
max_temp = -999
max_date = ''


f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)

for row in data:
    max_temp = float(max_temp)

    if row[-1] == '':
        pass
    else: 
        row[-1] = float(row[-1])
        if max_temp < row[-1]:
            max_temp = row[-1]
            max_date = row[0]

print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로, ', max_temp, '도 였습니다.')

f.close()

# +
## 내 생일의 기온 변화 그래프

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)


highest = []
lowest = []

for row in data:
    if row[-1] != '':
        if int(row[0].split('-')[0]) >= 1983 :
               if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14':
                    highest.append(float(row[-1]))
                    lowest.append(float(row[-2]))
                    
plt.rcParams['axes.unicode_minus'] = False #그래프에서 음수 (-) 깨지는 오류 수정
plt.rc('font', family = 'AppleGothic') #그래프에서 한글 깨지는 오류 수정

plt.title('내 생일의 기온 변화 그래프')
plt.rc('font', family = 'AppleGothic')
plt.plot(highest, 'hotpink', label = '최고기온')
plt.rc('font', family = 'AppleGothic')
plt.plot(lowest, 'skyblue', label = '최저기온')
plt.legend()
plt.show()

f.close()

# +
## 1월과 8월의 최고기온

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)

jan = []
aug = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

plt.rcParams['axes.unicode_minus'] = False
plt.rc('font', family = 'AppleGothic')
plt.title('1월과 8월의 최고기온')       

plt.rc('font', family = 'AppleGothic')
plt.hist(aug, bins = 100, color = 'r', label = '8월')
plt.rc('font', family = 'AppleGothic')                       
plt.hist(jan, bins = 100, color = 'b', label = '1월')


plt.legend()
plt.show()

f.close()

# +
# 8월의 기온 분포표

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)

date = []
for i in range(31):
    date.append([])

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            date[int(row[0].split('-')[2])-1].append(float(row[-1]))
            
plt.rc('font', family = 'AppleGothic')
plt.title('8월의 기온분포')  
            
plt.boxplot(date)
plt.show()

f.close()

# +
# 원하는 지역의 성별 인구 분포 찾기

import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
male = []
female = []

where = input("찾고 싶은 지역의 이름을 알려주세요: ")

for row in data:
    if where in row[0]:
        for i in range(101):
            male.append(-int(row[i+3]))
            female.append(int(row[-(i+1)]))
            
female.reverse()

plt.figure(dpi=80, figsize=(20,10))
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('도담동 지역의 남녀 성별 인구 분포')

plt.style.use('ggplot')
plt.barh(range(101), male, label='남성', color='r')
plt.barh(range(101), female, label='여성', color='b')

plt.legend()
plt.show

f.close()
