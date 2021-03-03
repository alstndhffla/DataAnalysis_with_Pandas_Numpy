import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
# 파이썬 그래프를 그릴 때 사용하는 matplotlib 패키지와 pyplot 모듈

"""
실시간/틱/분봉 데이터가 아닌 일봉 데이터는 구글이나 야후에서도 쉽게 구할 수 있다.
datareader 라는 함수는 웹 상의 데이터를 dataframe 객체로 만드는 기능을 제공한다.
야후 파이낸스로부터 데이터를 가져와 그래프까지 그려보는 걸로.
"""

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs1 = web.DataReader('078930.ks', 'yahoo', start, end)

print(gs1)

# 데이터프레임의 객체를 요약해서 볼 수 있다
print(gs1.info())


print("---------------------------------------------------------")
# 차트 분석을 위해 더 많은 데이터를 받아오기 위함
# 날짜를 명시하지 않으면 2010/1/1 일부터 데이터를 조회한 날까지의 데이터를 가져온다
gs = web.DataReader('078930.ks', 'yahoo')
print(gs)

plt.plot(gs['Close'])
# plt.show() 이거 안입력하면 출력했을 때 결과물을 콘솔창에 문자로 표현해준다.
plt.show()

