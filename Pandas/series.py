from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

print(kakao[0])
print(kakao[2])
print(kakao[4])


print("----------------------------------------------------------")
"""
Series 자료구조는 객체를 생성할 때 따로 인덱스를 부여하지 않으면 바인딩한 순서대로 들어가며 기본적으로 0부터 인덱스를 시작한다
허나 아래와 같이 지정해 줄 수 있다.(파이썬의 딕셔너리와 비슷)
인덱스 번호는 향후 프로그램을 위해 구분되는 것이 좋지만 같은 값을 넣어도 오류가 발생하지 않는다.
"""

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                           '2016-02-20',
                                                           '2016-02-21',
                                                           '2016-02-22',
                                                           '2016-02-23'])

print(kakao2)

print(kakao2['2016-02-23'])


print("----------------------------------------------------------")
"""
Series 객체는 또한 index 와 value 라는 이름의 속성으로 접근할 수 있다.
"""
for date in kakao2.index:
    print(date)

for Closing_close in kakao2.values:
    print(Closing_close)


print("----------------------------------------------------------")
"""
Series 는 서로 다르게 인덱싱된 데이터에 대해서도 알아서 덧셈 연산을 처리해준다...
"""
# 각 시리즈 객체의 인덱싱 순서가 다른 상태다.
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

# 인덱싱 값이 같은 것 끼리 덧셈 연산을 수행한다.
merge = mine + friend
print(merge)
