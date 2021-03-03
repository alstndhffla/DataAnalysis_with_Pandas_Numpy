import usecsv
import numpy as np
import os
os.chdir(r'C:\Users\alstn\PycharmProjects\data-analysis-Pandas-Numpy\Numpy')
# quest.csv 저장한 경로

# 파일을 열어 숫자 원소를 실수형으로 바꾼 후 배열 형태로 저장
quest = np.array(usecsv.swith(usecsv.opencsv('quest.csv')))

print(quest)

# 4보다 큰 점수를 만점인 5점으로 동기화
quest[quest > 5] = 5
# 결과물을 저장
usecsv.writecsv('result.csv', list(quest))