import pandas as pd

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample.csv'
sample = pd.read_csv(file_url)

print(sample.head)
print(sample.tail())

sample.inf0()
sample.describe()

sample_dic={'name': ['John', 'Ann', 'Kevin'], 'age': [23,22,21]}
a = pd.DateFrame(sample_dic)

a.info()

pd.DataFrame([[1,2,],[3,4], [5,6],[7,8]])
pd.DataFrame([[1,2],[3,4],[5,6],[7,8]], columns= ['var_1', 'var_2'], index=['a', 'b', 'c', 'd'])

import pandas as pd
file_url = 'https://media.githubusercontent.com/media/musthave-ML10/date_source/main/sample_df.csv'

sample_df = pd.read_csv(file_url, index_col=0)
print(sample_df.head())

print(sample_df['var_5'])

#print(sample_df['var_1', 'var_2']) #[] 안에는 하니의 값만 들어갈 수 있음
print(sample_df[['var_1', 'var_4']]) #[ [] ] 를 사용하면 [] 가 하나의 값으로 인식팀

#loc 는 location의  앞글자
print(sample_df.loc['a']) #행 가준으로 언대싱
print(sample_df.loc[['a', 'c', 'e']])
print(sample_df.loc['a': 'c'])

# iloc: integer location의 약자
print(sample_df.iloc[[0,1,2]])
print(sample_df.iloc[0:2])
print(sample_df.iloc[0:3])
print(sample_df.iloc[0:3, 2:4]) # 컴림까지 등시에 입댁싱

print(sample_df.drop(['var_1', 'var_3'], axis=1)) #컬럼을 재거하려면 axis =1
print(sample_df.drop(['var_1', 'var_2'], axis=1))
print(sample_df.drop(['a', 'b', 'c'], axis=0)) #형을 재거하려면 axis = 0 또는 다플트로 사용

netflix = pd.read_csv('2.1.1.netflix.csv')
print(netflix.head())

print(netflix['release_year'])
print(netflix['release_year'] > 2015)

more2015 = netflix[netflix['release_year'] > 2015]
print(more2015.head(10))

print(~(netflix['release_year'] > 2015))
