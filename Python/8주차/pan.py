import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep='\t')
#-------------------------------------------
# 열 데이터 추출

# country_df = df['country']
# print(type(country_df))
# print(country_df.head())
# print(country_df.tail())

# subset = df[['country', 'continent', 'year']]
# print(type(subset))
# print(subset.head())
# print(subset.tail())
# ---------------------------------------
# 행 데이터 추출
# print(df.loc[0])

# print(df.loc[99])

# print(df.loc[-1])

# number_of_rows = df.shape[0]
# shape는 튜플을 반환하기 때문에 0번째는 행을 반환
# last_row_index = number_of_rows - 1
# print(df.loc[last_row_index])
# print(df.tail(n=1))
# print(df.tail(n=2))
# print(df.loc[[0,99,999]])

# tail 메서드와 loc속성이 반환하는 자료형은 다르다.
# subset_loc = df.loc[0]
# subset_tail = df.tail(n=1)

# print(type(subset_loc))
# print(type(subset_tail))

# iloc 속성으로 행 데이터 추출하기
# print(df.iloc[1])
# print(df.iloc[99])
# print(df.iloc[-1])
# print(df.iloc[1710])
# print(df.iloc[[0,99,999]])
#-------------------------------------------
# 슬라이싱
# subset = df.loc[:,['year','pop']]
# print(subset.head())
# subset = df.iloc[:,[2,4,-1]]
# print(subset.head())

# range 메서드로 원하는 데이터 추출하기
# small_range = list(range(5))
# print(small_range)
# print(type(small_range))
# subset = df.iloc[:, small_range]
# print(subset.head())
# small_range = list(range(3,6))
# print(small_range)
# subset = df.iloc[:, small_range]
# print(subset.head())
# small_range = list(range(0, 6, 2)) 
# subset = df.iloc[:, small_range] 
# print(subset.head())
#--------------------------------------
# 슬라이싱, range 메서드 비교하기
# subset = df.iloc[:, :3] 
# print(subset.head())
# subset = df.iloc[:, 0:6:2] 
# print(subset.head())
#---------------------------------------
# loc, iloc 속성 자유자재로 사용하기
# print(df.iloc[[0, 99, 999], [0, 3, 5]])
# print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])
# print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])
#------------------------------------------------------------
# 그룹화한 데이터의 평균 구하기
# print(df.groupby('year')['lifeExp'].mean())
# grouped_year_df = df.groupby('year')
# print(type(grouped_year_df))
# print(grouped_year_df)
# grouped_year_df_lifeExp = grouped_year_df['lifeExp'] 
# print(type(grouped_year_df_lifeExp))
# mean_lifeExp_by_year = grouped_year_df_lifeExp.mean() 
# print(mean_lifeExp_by_year)
#-------------------------------------------------------------
# lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한 번에 계산하기
# multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean() 
# print(multi_group_var)
# print(type(multi_group_var))
#-----------------------------------------------------------------------------
# 그룹화한 데이터의 개수 세기
# print(df.groupby('continent')['country'].nunique())

# ------------------------------------------------------
# 그래프 그리기 (jupyter notebook)
# %matplotlib inline
# import matplotlib.pyplot as plt
# global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean() 
# print(global_yearly_life_expectancy)
# global_yearly_life_expectancy.plot()
#----------------------------------------------------
# 시리즈와 데이터 프레임만들기
# s = pd.Series(['banana',123456])
# print(s)
# s = pd.Series(['Wes McKinney', 'Creator of Pandas'])
# print(s)
# s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
# print(s)
# scientists = pd.DataFrame({ 
#     'Name': ['Rosaline Franklin', 'William Gosset'], 
#     'Occupation': ['Chemist', 'Statistician'], 
#     'Born': ['1920-07-25', '1876-06-13'], 
#     'Died': ['1958-04-16', '1937-10-16'], 
#     'Age': [37, 61]}) 
# print(scientists)
# scientists = pd.DataFrame( 
#     data={'Occupation': ['Chemist', 'Statistician'], 
#           'Born': ['1920-07-25', '1876-06-13'], 
#           'Died': ['1958-04-16', '1937-10-16'],
#           'Age': [37, 61]},
#     index=['Rosaline Franklin', 'William Gosset'],
#     columns=['Occupation', 'Born', 'Age', 'Died']) 
# print(scientists)
# from collections import OrderedDict

# scientists = pd.DataFrame(OrderedDict([ 
#     ('Name', ['Rosaline Franklin', 'William Gosset']),
#     ('Occupation', ['Chemist', 'Statistician']), 
#     ('Born', ['1920-07-25', '1876-06-13']), 
#     ('Died', ['1958-04-16', '1937-10-16']), 
#     ('Age', [37, 61])
# ])
# ) 
# print(scientists)
#--------------------------------------------
# 데이터 프레임에서 시리즈 선택하기
# scientists = pd.DataFrame(
#     data={'Occupation': ['Chemist', 'Statistician'], 
#           'Born': ['1920-07-25', '1876-06-13'], 
#           'Died': ['1958-04-16', '1937-10-16'],
#           'Age': [37, 61]},
#     index=['Rosaline Franklin', 'William Gosset'],
#     columns=['Occupation', 'Born', 'Died', 'Age']) 
# first_row = scientists.loc['William Gosset'] 
# print(type(first_row))
# print(first_row)
# print(first_row.index)
# print(first_row.values)
# print(first_row.keys())
# print(first_row.index[0])
# print(first_row.keys()[0])
# ages = scientists['Age'] 
# print(ages)
# print(ages.mean())
# print(ages.min())
# print(ages.max())
# print(ages.std())
#----------------------------------
# 시리즈와 불린 추출하기
scientists = pd.read_csv('data/scientists.csv')
# ages = scientists['Age'] 

# print(ages.max())
# print(ages.mean())
# print(ages[ages > ages.mean()])
# print(ages > ages.mean())
# print(type(ages > ages.mean()))
# manual_bool_values = [True, True, False, False, True, True, False, True] 
# print(ages[manual_bool_values])
#---------------------------------------------------
# 벡터와 스칼라로 브로드캐스팅 수행하기
# print(ages + ages)
# print(ages * ages)
# print(ages + 100)
# print(ages * 2)
# print(pd.Series([1, 100]))
# print(ages + pd.Series([1, 100]))
# rev_ages = ages.sort_index(ascending=False) 
# print(rev_ages)
# print(ages * 2)
# print(ages + rev_ages)
#-------------------------------------------------

# 불린 추출과 브로드캐스팅
# print(scientists[scientists['Age'] > scientists['Age'].mean()])
# print(scientists.loc[[True, True, False, True, False, False, False, False]])
# print(scientists * 2)
#----------------------------------------------

# 시리즈와 데이터프레임의 데이터 처리하기
# print(scientists['Born'].dtype)
# print(scientists['Died'].dtype)
# born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d') 
# print(born_datetime)
# died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
# print(died_datetime)
# scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
# print(scientists.head())
# print(scientists.shape)
# scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
# print(scientists)
#------------------------------------------------------
# 시리즈, 데이터프레임의 데이터 섞기
# print(scientists['Age'])
# import random

# random.seed(42)
# random.shuffle(scientists['Age'])
# print(scientists['Age'])
#---------------------------------------------------
# 데이터 프레임 열 삭제하기
# print(scientists.columns)
# scientists_dropped = scientists.drop(['Age'], axis=1)

# print(scientists_dropped.columns)
#-------------------------------------------
# 데이터 저장하기
# names = scientists['Name']
# names.to_pickle('scientists_names_series.pickle')
# scientists.to_pickle('scientists_df.pickle')
# scientist_names_from_pickle = pd.read_pickle('scientists_names_series.pickle')
# print(scientist_names_from_pickle)
# scientists_from_pickle = pd.read_pickle('scientists_df.pickle')
# print(scientists_from_pickle)
#----------------------------------------
# csv 파일과 tsv 파일로 저장하기
# names.to_csv('scientist_names_series.csv')
# scientists.to_csv('scientists_df.tsv', sep='\t')
# 엑셀 파일로 저장하기
# names_df = names.to_frame()

# import xlwt 
# names_df.to_excel('scientists_names_series_df.xls')

# import openpyxl 
# names_df.to_excel('scientists_names_series_df.xlsx')
#-------------------------------------------------------