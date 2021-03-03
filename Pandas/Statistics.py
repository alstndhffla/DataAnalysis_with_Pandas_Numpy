import os, re
import pandas as pd
from scipy import stats
# t검정을 사용하기 위한 싸이파이 패키지와 그 안에 있는 stats 모듈

os.chdir(r'C:\Users\alstn\PycharmProjects\data-analysis-Pandas-Numpy\Pandas')

"""
설문조사 데이터의 t검정, 상관관계 분석
"""

df2 = pd.read_csv('survey.csv')
# 데이터프레임 저장순서상 상위 5개
print(df2.head())

# 데이터프레임의 각 컬럼별 평균
print(df2.mean())

# 수입합계
print(df2.income.sum())

# 중앙값
print(df2.income.median())

print("------------------------------------------------")
"""
평균이나 중앙값을 일일이 구해야 하는 번거로움 없이 데이터 분석을 위해 필요한 분석과
표준편차, 최대, 최소 등의 값을 한 번에 출력해주는 함수 - 통상 논문에서는 통계를 본격적으로 분석하기 전에 해당
정보를 먼저 보여주고 시작한다. 이 데이터가 대략 어떻게 생긴 데이터인지 사용자에게 알려주고 시작하는 것.
describe()
"""
print(df2.describe())

print("------------------------------------------------")
# 빈도 분석하기 - 얼마나 자주 나왔는지. value_counts()
print(df2.sex.value_counts())

print("------------------------------------------------")
# 그룹으로 나누어 분석하기(집단의 평균 구하기) - groupby()
# 영어점수, 직업만족도, 스트레스에 대해서도 평균을 내 비교해볼 수 있다.
print(df2.groupby(df2.sex).mean())

# 그러나 해당 데이터의 차이로 무조건적인 결론을 내릴 순 없다. 두 집단이 유의한 평균 차이가 나는지는 검증해봐야하기 때문
# 독립된 두 집단의 평균을 비교하는 가장 간편한 데이터분석법은 t검정
print("------------------------------------------------")
# 설문조사 결과를 남성의 수입과 여성의 수입으로 분리
male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']
# ttest_ind() 함수로 t검정 실행 -> 변수를 여러개 넣을 수 있는데 여기서는 두 집단만.
print(stats.ttest_ind(male, female))
# 결과값 : Ttest_indResult(statistic=-0.10650308143428423, pvalue=0.9161940781163369)
"""
실행 값중 pvalue 는 유의확률을 의미. 즉 이 값이 작을수록 유의 차이가 있다고 해석된다.
일반적으로 95% 또는 99%를 유의한 확률의 기준으로 삼기 때문에 유의확률 값이 0.05 미만이거나
0.01 미만이면 유의한 차이가 나타난다고 말할 수 있다.
해당 결과에서는 pvalue 가 0.916 으로 1에 가까울 정도로 높지만 유의한 차이가 있다고 보기는 어렵다.
유의확률이 0.05 보다 작을 때는 95% 수준에서 유의하고, 0.01 보다 작으면 99% 수준에서 유의하다.
"""
# 해당 결과값을 변수에 저장하고
ttest_result = stats.ttest_ind(male, female)
# 각 인덱스를 확인하면 statistic 와 pvalue 가 각각 들어가있다.
print(ttest_result[0])
print(ttest_result[1])

# TypeError: not enough arguments for format string
if ttest_result[1] > .05:
    print("p_value 는 %f 로 95% 수준에서 유의하지 않음" % round(ttest_result[1], 6))
else:
    print("p_value 는 %f 로 95% 수준에서 유의함" % round(ttest_result[1], 6))

"""
두 변수의 상관관계 분석하기
corr()
"""
# 피어슨 상관관계 분석
print(df2.corr())
# 스피어만 상관관계 분석
print(df2.corr(method='spearman'))

# 수입과 스트레스의 상관관계
df2.income.corr(df2.stress)
# 유의확률이 0.05 나 0.01 보다 낮아야 상관계수도 의미를 갖는다. 하지만 판다스의 corr 메서드로는 유의확률을 구할 수 없다.


"""
회귀 분석
"""


