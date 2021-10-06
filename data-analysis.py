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
import pandas as pd

chipo = pd.read_csv('chipotle.tsv', sep='\t')

# +
### 1. Veggie Salad Bowl의 총 주문횟수는 몇 회인가요?
# -

chipo_salad = chipo[chipo['item_name']=="Veggie Salad Bowl"]
chipo_salad = chipo_salad.drop_duplicates(['item_name','order_id'])
print(len(chipo_salad))

# +
### 2. Canned Soda를 두병 이상(>1) 주문한 고객은 총 몇명인가요? #20
# -

chipo_soda = chipo[chipo['item_name']=='Canned Soda'] 
print(len(chipo_soda[chipo_soda['quantity'] > 1]))

# +
### 3. 한국의 술 소비량 대비 알코올 비율 값과, 전체 국가 순위 중 한국의 순위 알아내기]
#한국은 전체 국가 중 15위입니다.

# +
import pandas as pd
import numpy as np

drinks = pd.read_csv('drinks.csv')

# 국가별 total_servings 피처를 만들어서 병합합니다.
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 술 소비량 대비 알콜 비율에 대한 칼럼을 만들어서 병합합니다.
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

# 술 소비량 대비 알콜 비율 : 전체 순위 중 한국의 순위를 구합니다.
drinks['alcohol_rate_rank'] = drinks['alcohol_rate'].rank(ascending=False)
print("한국은 전체 국가중 " + str(drinks[drinks['country']=='South Korea']['alcohol_rate_rank'].values[0].astype(int)) + "위입니다.")
# -

drinks.head()

# +
### 4. user 정보를 읽어들여, user의 연령대별 분포 가시화 하기

# +
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

user_data = pd.io.parsers.read_csv("users.dat", names=['user_id', 'gender', 'age', 'occupation', 'zipcode'], delimiter='::')
user_data.head()


# +
def age_classification(age):
    if age == 1: # 연령에 1이 들어가 있는 경우엔, outlier로 취급
        return 'outlier'
    else:
        return str(age)[0] + "0"

user_data['ages'] = (                         A                               )
user_ages = (                 B                    )
print(user_ages)

plt.bar(user_ages.index, user_ages.values, alpha=0.8)
plt.title('User ages')
plt.ylabel('Count', fontsize=12)
plt.xlabel('Ages', fontsize=12)
plt.show()


# +
def age_classification(age):
    if age == 1: # 연령에 1이 들어가 있는 경우엔, outlier로 취급
        return 'outlier'
    else:
        return str(age)[0] + "0"

user_data['ages'] = age_classification(lambda age : age == user_data['age'])


user_data['ages'] = user_data['age'].apply(lambda x:age_classification(x))
user_ages = user_data.ages.value_counts()
print(user_ages)

plt.bar(user_ages.index, user_ages.values, alpha=0.8)
plt.title('User ages')
plt.ylabel('Count', fontsize=12)
plt.xlabel('Ages', fontsize=12)
plt.show()
# -

age_classification(1)

user_data.describe()


# +
def age_classification(age):
    if age == 1: # 연령에 1이 들어가 있는 경우엔, outlier로 취급
        return 'outlier'
    else:
        return str(age)[0] + "0"
    
age_classification(10.1)
# -

user_data.age.value_counts()
