import pandas as pd

data = pd.read_csv('toy_dataset.csv')

#1 მონაცემთა ტიპები 

print(data.dtypes)  # Number       int64
#                     # City        object
#                     # Gender      object
#                     # Age        float64
#                     # Income     float64
#                     # Illness     object
#                     # dtype: object

#2 
data = data[data['Age']>25]
data = data[data['Age']<65]
print(data)
pd.read_excel
# #3
# #სხვადასხვა ქალაქების რადენობა
print(data['City'].drop_duplicates().count())  #8

# #ქალაქების ფარდობითი განაწილება 
print(data['City'].value_counts())  # New York City      50305
#                                     # Los Angeles        32173
#                                     # Dallas             19704
#                                     # Mountain View      14219
#                                     # Austin             12291
#                                     # Boston              8301
#                                     # Washington D.C.     8119
#                                     # San Diego           4881

#4
#რა რაოდენობაა უცნობი ხელფასების
print(data['Income'].isna().sum()) # 5

#უნცობი ხელფასების მოშორებᲐ
data['Income'].dropna(axis=0)
print(data)

#5
#საშუალო შემოსავალი
print(data['Income'].mean()) # 91620

