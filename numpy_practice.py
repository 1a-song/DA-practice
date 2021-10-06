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

import numpy as np

#차원=축
#아래 예시는 2개 축(2차원)
#축의 길이는 원소 개수
#아래 예시는 첫번째 축은 길이가 2, 두번째는 3
[[1, 0, 0],
 [0, 1, 1]]

#3개 요소(element)이고 길이(length)는 3
[1, 2, 3]

# 데이터 크기와 모양
# 1) ndarray.shape : 배열의 각 축(axis)의 크기
# 2) ndarray.ndim : 축의 개수(Dimension)
# 3) ndarray.dtype : 각 요소(Element)의 타입
# 4) ndarray.itemsize : 각 요소(Element)의 타입의 bytes 크기
# 5) ndarray.size : 전체 요소(Element)의 개수 ###

a = np.arange(15).reshape(3, 5)
print(a)

a.size #element 개수

a.dtype

a.itemsize #각 element의 byte 크기

# +
#numpy.ndarray 생성하기

a = np.array([1, 2, 3])
print(a)
# -

a.dtype

a = np.array([0.1, 0.01, 0.3])
a.dtype

# +
#섞여있으면 가장 큰 타입을 데이터 타입으로 한다
#float > int

a = np.array([0.1, 1, 0])
a.dtype
# -

# 배열 생성하기

a = np.zeros((3, 4))
print(a)

a = np.ones((2, 3, 4))
print(a)

a = np.empty((2, 3)) #초기화되지 않은 값으로 배열 생성
print(a)

a = np.arange(10, 30, 5)
print(a)

a = np.arange(0, 2, 0.3)
print(a)

a = np.linspace(0, 99, 100) # 0 ~ 99 까지 100등분 (np.arange와 다르게 99를 포함한다)
print(a)

print(np.array([1, 2, 3])) #1차원
print("=======")
print(np.array([[1, 2, 3], [4, 5, 6]])) #2차원
print("=======")
print(np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])) #3차원

a = np.arange(0, 10000).reshape(100, 100)
print(a)

# 행렬 연산

# +
#element-wise

a = np.array([20, 30, 40, 50])
b = np.arange(4)

print('a =', a)
print('b =', b)
print("a - b =", a - b)
# -

print('b**2 =', b**2)

print('a*10 =', a*10)

# +
#boolean 많이 쓰임!

print(a<35)

# +
#여러가지 곱셈
A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )

print("element-wise product \n", A*B)
print("matrix product \n", A@B)
print("dot product \n", A.dot(B))

# +
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi,3)

print(a.dtype.name)
print(b.dtype.name)

#수치연산 진행할 때 각각의 .dtype이 다르면,
#타입이 큰쪽(int < float < complex)으로 자동으로 변경
# -

c = a*b
c.dtype #float으로 upcasting

c = np.exp(a+1j)
c.dtype #complex(복소수)로 upcasting

# 여러가지 연산
#
# 1) .sum( ): 모든 요소의 합
#
# 2) .min( ): 모든 요소 중 최소값
#
# 3) .max( ): 모든 요소 중 최대값
#
# 4) .argmax( ): 모든 요소 중 최대값의 인덱스
#
# 5) .cumsum( ): 모든 요소의 누적합

a = np.arange(8).reshape(2, 4)**2
print(a)

print(a.sum())
print(a.min())
print(a.max())

print(a.argmax()) #인덱스!!
print(a.cumsum()) #파스칼? 덧셈?

print(a.sum(axis=1)) #같은 행끼리 다 더한다
print(a.sum(axis=0)) #같은 열끼리

print(a.min(axis=1))
print(a.cumsum(axis=0))

# 범용 함수 
#
# 참고: https://numpy.org/doc/1.18/reference/ufuncs.html#available-ufuncs

A = np.arange(3)
print(A)

print('지수함수', np.exp(A))
print('제곱근', np.sqrt(A))

a = np.arange(10)**2
print(a)

a[2:5]

print(a[0:6:2])
print(a[:6:2])

# +
print(a[::-1]) #reverse

for i in a:
    print(i**(1/2.))
# -

# Numpy shape 변경
#
# .ravel( )은 1차원으로 변경
#
# .reshape( )은 지정한 차원으로 변경
#
# .T는 전치(Transpose) 변환
#
# 하지만 데이터 원본은 변경하지 않고 복사하여 연산한 결과를 return
#
# *resize는 원본을 변경

a = np.floor(10*np.random.rand(3,4)) #np.floor 내림함수 #np.random.rand 0~1사이 랜덤 난수 생성
print(a)

print(np.ravel(a)) #1차원으로 변경
print()
print(a)
print()
print(a.shape) #원본은 변경하지 않음

print(np.reshape(a, (2, 6)))

print(a.T)
print(a.T.shape)

# 데이터 쌓기
#
# np.vstack() 와 np.hstack()를 통해 데이터를 합칠 수 있음
#
# np.vstack(): axis=0 기준으로 쌓음
#
# np.hstack(): axis=1 기준으로 쌓음

# +
a = np.floor(10*np.random.rand(2,2))
print(a)

print()

b = np.floor(10*np.random.rand(2,2))
print(b)
# -

print(np.vstack((a, b)))

print(np.hstack((a, b)))

a = np.floor(10*np.random.rand(2,12))
print(a)

print(np.hsplit(a, 3))

# +
# a를 3번째 열 ~ 4번째 열 미만 기준으로 분할하여 3개의 array를 반환

print(np.hsplit(a, (3,4)))
# -

print(np.vsplit(a, (1, 12)))

# 데이터 복사
#
# 이슈
#
# 배열의 주소가 같은지, 다른지
#
# 배열의 요소의 주소가 같은지, 다른지
#
# 배열의 요소 값을 변경했을 때 변경이 되는지, 안되는지
#
# 배열에서 복사 이슈에서는, '=', '.view()', '.copy()' 3가지 존재

a = np.arange(5)
b = a

a

b

id(a)

id(b)

id(a[0])

id(b[0])

# +
a = np.array([1,2,3])

b = a

print(a)
print(b)

print(f"id(a):\t\t {id(a)}")
print(f"id(a[0]):\t\t {id(a[0])}")

print(f"id(b):\t\t {id(b)}")
print(f"id(b[0]):\t\t {id(b[0])}")

print("\n"+"="*10 + "변경: a[1] = 4" + "="*10)

a[1] = 4

print(a)
print(b)

print(f"id(a):\t\t {id(a)}")
print(f"id(a[0]):\t\t {id(a[0])}")

print(f"id(b):\t\t {id(b)}")
print(f"id(b[0]):\t\t {id(b[0])}")
# -

# '.view()' 얕은 복사
#
# view()는 실제로 데이터가 복사된다기 보다는 데이터 각각의 참조값이 복사
#
# c와 a의 참조값은 다르지만 각각의 데이터 참조값이 복사됐다는 의미
#
# 따라서 a와 c는 다르지만 c[0, 4]는 a[0, 4]는 같은 참조값을 보고 있어 a가 변경되는 것을 확인할 수 있음
#
# 마찬가지로 s에 a를 슬라이싱하여 데이터를 가져가도 s를 변경하면 a가 변경됩니다.
#
# ===============
#
# '.view()'
#
# a, c라는 배열은 다른 주소 값을 가지고 있다.
# a[0], c[0] 인 요소는 같은 주소 값을 가지고 있다.

# +
a = np.array([1, 2, 3])
c = a.view()

print(a)
print(c)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(c)):\t\t {id(c)}")
print(f"id(c[0]):\t {id(c[0])}")

print("\n"+"="*10 + "변경: a[1] = 4" + "="*10 )

a[1] = 4

print(a)
print(c)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(c)):\t\t {id(c)}")
print(f"id(c[0]):\t {id(c[0])}")
# -

# '.copy()' 깊은 복사
#
# .copy()를 이용
#
# a와 d의 참조값 뿐만 아니라 a의 각각의 데이터 전부가 새로운 객체로 생성
#
# '.copy()'
#
# a, d라는 배열은 다른 주소 값을 가지고 있다.
# a[0], d[0] 인 요소는 다른 주소 값을 가지고 있다.

# +
a = np.array([1, 2, 3])
d = a.copy()

print(a)
print(d)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(d)):\t\t {id(d)}")
print(f"id(c[0]):\t {id(d[0])}")

print("\n"+"="*10 + "변경: a[1] = 4" + "="*10 )

a[1] = 4

print(a)
print(d)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(d)):\t\t {id(d)}")
print(f"id(c[0]):\t {id(d[0])}")
# -

# 정리
#
# '=' 등호
#
# a, b라는 배열이 같은 주소 값을 가지고 있다.
# a[0], b[0] 인 요소는 다른 주소 값을 가지고 있다.
#
# '.view()'
#
# a, c라는 배열은 다른 주소 값을 가지고 있다.
# a[0], c[0] 인 요소는 같은 주소 값을 가지고 있다.
#
# '.copy()'
#
# a, d라는 배열은 다른 주소 값을 가지고 있다.
# a[0], d[0] 인 요소는 다른 주소 값을 가지고 있다.

# +
a = np.array([1, 2, 3])
b = a
c = a.view()
d = a.copy()

print(a)
print(b)
print(c)
print(d)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(b)):\t\t {id(b)}")
print(f"id(b[0]):\t {id(b[0])}")

print(f"id(c)):\t\t {id(c)}")
print(f"id(c[0]):\t {id(c[0])}")

print(f"id(d)):\t\t {id(d)}")
print(f"id(d[0]):\t {id(d[0])}")

print("\n"+"="*10 + "변경: a[1] = 4" + "="*10 )
a[0] = 4

print(a)
print(b)
print(c)
print(d)

print(f"id(a)):\t\t {id(a)}")
print(f"id(a[0]):\t {id(a[0])}")

print(f"id(b)):\t\t {id(b)}")
print(f"id(b[0]):\t {id(b[0])}")

print(f"id(c)):\t\t {id(c)}")
print(f"id(c[0]):\t {id(c[0])}")

print(f"id(d)):\t\t {id(d)}")
print(f"id(d[0]):\t {id(d[0])}")
# -

# 브로드캐스팅 (Broadcasting rules) !!중요
#
# 브로드 캐스팅은 단순하게 편리성을 위해 Shape가 다른 np.narray 끼리 연산을 지원해주기 위함
#
# 데이터 계산 시 자주 등장하는 상황인데, 이것이 없다면 Shape를 맞춰야하는 번거로움이 생기게 되는데 이 개념을 이해하면 잘 활용할 수 있음

np.array([1,2,3,4,5]) * 2  #np.array가 아닌 list 였다면 [1,2,3,4,5,1,2,3,4,5] 

print(np.array([1,2,3,4,5]) * 2)
# Broadcasting
print(np.array([1,2,3,4,5]) * np.array([2,2,2,2,2]))

# 차원(ndim)이 같고 각 축(axis)의 값이 같거나 1이야 연산이 가능
#
# 만약 각 축의 값이 다르면 브로드캐스팅되어 값이 복사

print(np.arange(4) * 2)

# +
print(np.ones((3,4)))
print(np.arange(4))

print(np.ones((3,4)) * np.arange(4))

# +
print(np.arange(3).reshape((3,1)))
print(np.arange(3))

print(np.arange(3).reshape((3,1)) * np.arange(3))

# +
a = np.arange(12)*2

print(a)
# -

a[:2]

a[1:9:2]

a = np.arange(12)*2
print(a)
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])

# +
#현업에서 많이 쓰이는 boolean indexing

a = np.arange(12).reshape(3, 4)
b = a > 4
a[b]
# -

a[b] = 0
print(a)
