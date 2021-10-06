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

import pandas as pd
import numpy as np

titanic = pd.read_csv("titanic.csv")

print(type(titanic))

#데이터 내용 확인
titanic.head()

titanic.tail()

names = titanic['Name']
names.head()

example = pd.Series(["Kim Tuna", 11.1, 12, 13, 14], 
                    index=['a','b','c','d','e'],
                   name='example')
example.head()

# Series는 모든 데이터 타입(정수, 소수, 객체 등)을 가질 수 있는 레이블링된 1차원 배열이다
# 인덱스는 시계열(Time series)도 포함할 수 있다

print(type(example))
print(example.shape)

print(type(names))
print(type(titanic))

print(names.shape)
print(titanic.shape)

# +
###데이터 확인하기
#columns 
#type
#shape
#describe
#info
# -

print(titanic.columns)

# +
#데이터 재구성
#성별, 연령대별 생존률 분석해보기

passenger = titanic[["Sex", "Age", "Survived"]]
passenger.head()
# -

print(passenger.shape)
print(type(passenger))

passenger.info()

passenger.describe()

# +
### Age에 null값 처리하기 (평균으로 대체해보기)
## notna로 결측값 있는 데이터 삭제하는 방법도 있음!!

passenger["Age"].fillna(passenger["Age"].mean(), 
                        axis=0, inplace=True)
# -

passenger.info()

passenger.head()

survive = passenger.groupby("Age")["Survived"].sum()
survive[:10]

# +
import matplotlib.pyplot as plt

plt.barh(survive.index, survive)

# +
#남녀 구분해서 항아리 그래프 그리기

survive_f = passenger[passenger["Sex"] == "female"]
survive_m = passenger[passenger["Sex"] == "male"]

survive_f = survive_f.groupby("Age")["Survived"].sum() * -1
survive_m = survive_m.groupby("Age")["Survived"].sum()

# +
plt.barh(survive_f.index, survive_f, label="female")
plt.barh(survive_m.index, survive_m, label="male")
plt.legend()

plt.figure(figsize=(10,10), dpi=800)
plt.show()
# -

under20 = passenger[passenger["Age"] < 20]
print(passenger["Age"]  < 20)
under20.head()

# +
### 불리언 인덱싱 + .isin()

titanic["Pclass"].isin([1])
# -

class13 = titanic[titanic["Pclass"].isin([1,2,3])]
class13.count()

titanic.describe()

# +
#class23 = titanic[titanic["Pclass"].isin([2,3])]
class23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)] #조건 or 조건

class23.head()

# +
# isin 함수를 사용해 30대 여성만 추출 가능?
# & 로 2개 이상 조건으로 불린 인덱싱 w/ .isin 해보기

age30f = passenger[passenger["Age"].isin(np.arange(30, 40)) 
                  & passenger["Sex"].isin(["female"])]

age30f.head(10)
# -

# **특정 row/column 선택하기**
#
# .loc[] : key로 검색
#
# .iloc[] : index로 검색

names35 = titanic.loc[titanic["Age"] > 35, ["Name", "Age"]]
names35.head()

df = titanic.iloc[9:25, 2:5]
df

df.iloc[0:3, 1] = "No name"
df

# **데이터 통계**

print("평균나이: ", titanic["Age"].mean())
print("="*20)
print(titanic.columns)

# +
# 특정 변수를 추출해서 통계 요약 보기

titanic[["Age", "Fare"]].describe()

# +
# agg() 를 통해 여러 개 열에 여러가지 함수 적용 !!

# 모든 열에 여러 함수 매핑 : group객체.agg([함수1, 함수2, 함수3, ...])
# 각 열마다 다른 함수 매핑 : group객체.agg({'열1':함수1, '열2':함수2, ...})

print(titanic.agg({"Age": ["min", "max", "median", "std"],
                  "Fare": ["min", "max", "mean", "median"]}))

# +
# groupby 성별과 클래스로 묶어주고 나이와 요금의 평균 구하기

titanic.groupby(["Sex", "Pclass"])[["Age", "Fare"]].mean()

# +
#성별, 클래스별 생존자 수 총합 구하기

titanic.groupby(["Sex", "Pclass"])[["Survived"]].sum()

# +
#성별에 따른 생존률

survive_s = titanic.groupby("Sex")["Survived"].mean()
(survive_s * 100).head()

# +
#클래스에 따른 생존률

survive_c = titanic.groupby("Pclass")["Survived"].mean()
(survive_c * 100).head()
# -

print(titanic.shape)

# 열 추가
titanic['Ages'] = titanic['Age']*0.1

print(titanic.shape)

titanic.head()

# 열 삭제
titanic = titanic.drop('Ages', axis=1)

print(titanic.shape)

# +
# 행 추가

print(titanic.columns)
# -

titanic = titanic.append(titanic.iloc[0, :], ignore_index=True)
titanic

print(titanic.shape)

# 행 삭제
titanic = titanic.drop(891, axis=0)
titanic

# +
# 열 이름 수정 (df.rename)

titanic = titanic.rename(columns={'Fare':'Fare(USD)'})
# -

titanic


