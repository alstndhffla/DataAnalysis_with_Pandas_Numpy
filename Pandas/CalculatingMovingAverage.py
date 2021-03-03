import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


"""
주가이동평균계산하기, 그리기
*검증하고 수익이 날 확률이 얼마나 되는지 꼭 계산해보기
"""

# 조회 시작일과 종료일을 직접 입력
gs = web.DataReader('078930.ks', 'yahoo', '2016-01-01', '2020-10-10')

# 데이터가 잘 받아졌는지 끝에서부터 5개의 데이터를 확인
print(gs.tail())

# 5일치 종가를 기준으로 평균을 내기
ma5 = gs['Close'].rolling(window=5).mean()

# 위에서 만들어 놓은 이평선 구하는 변수를 끝에서부터 10일간의 데이터에 연동해 계산하기
print(ma5.tail(10))

# dataframe 객체에 이평선을 새 칼럼으로 추가하기
gs['MA5'] = ma5
print(gs.tail())

ma20 = gs['Close'].rolling(window=20).mean()
ma60 = gs['Close'].rolling(window=60).mean()
ma120 = gs['Close'].rolling(window=120).mean()

gs['MA20'] = ma20
gs['MA60'] = ma60
gs['MA120'] = ma120

print(gs.tail())

# 종가 그래프 그리기
plt.plot(gs.index, gs['Close'], label="Close")

# 이평선 5일
plt.plot(gs.index, gs['MA5'], label="MA5")

# 이평선 20일
plt.plot(gs.index, gs['MA20'], label="MA20")

# 이평선 60일
plt.plot(gs.index, gs['MA60'], label="MA60")

# 이평선 120일
plt.plot(gs.index, gs['MA120'], label="MA120")

# 그래프의 범례(속성) 표시 -> loc='best' 내부에 그리되 가장 데이터를 가리지 않는 범위
plt.legend(loc='best')
# 그래프 안에 격자 표시
plt.grid()
# 그래프 출력
plt.show()
