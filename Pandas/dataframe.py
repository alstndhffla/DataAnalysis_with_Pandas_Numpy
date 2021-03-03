from pandas import Series, DataFrame
"""
dataframe : 로우와 칼럼으로 구성된 2차원 형태의 자료구조
"""

row_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

print(row_data)

# 2차원 배열형태로 데이터를 저장.
# 딕셔너리의 키 값이 컬럼의 구분 값으로 들어간다.
data = DataFrame(row_data)
print(data)

print("-----------------------------------------")
"""
데이터프레임화 된 컬럼에 접근할 수 있다.
"""
print(data['col1'])
print(data['col2'])


print("-----------------------------------------")
daeshin = {'open': [11650, 11100, 11200, 11100, 11000],
           'high': [12100, 11800, 11200, 11100, 11150],
           'low': [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day1 = DataFrame(daeshin)
print(daeshin_day1)


print("-----------------------------------------")
"""
dataframe 역시 객체를 생성하는 시점에 index 를 통해서 인덱스값을 지정할 수 있다.
"""
date = ['16.02.01', '16.02.02', '16.02.03', '16.02.04', '16.02.05']
daeshin_day2 = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
# 위처럼 컬럼명을 지정하나 안하나 출력 값을 같다.
daeshin_day3 = DataFrame(daeshin, index=date)

print(daeshin_day2)
print("-----------------------------------------")
print(daeshin_day3)


print("-----------------------------------------")
"""
dataframe 의 특정 칼럼, 로우 선택
"""
close = daeshin_day3['close']
# 데이터프레임의 인덱스 값이랑 같이 출력됨.
print(close)


print("-----------------------------------------")
# dataframe 객체의 로우에 접근하려면 ix 메서드를 사용해야 한다. -> ix 메서드 삭제로 loc 사용.
# 컬럼별 값을 출력할 때는 키 값이 컬럼명이라 출력이 가능했지만 인덱스로 불러오는 것은 loc 메서드를 사용해야 한다.

day_data = daeshin_day3.loc['16.02.01']
print(day_data)
print(type(day_data))


print("-----------------------------------------")
"""
dataframe 객체의 칼럼이름과 인덱스 값을 확인하기
"""

print(daeshin_day3.index)
print(daeshin_day3.columns)







