import pandas as pd

data = pd.read_csv('toy_dataset.csv')


##3##

#a

null_gender = data['Gender'].isna().sum() #2
data.dropna(subset='Gender', inplace=True)



#b
max_income = data['Income'].max() #45345245.0
min_income = data['Income'].min() #-6000.0
null_income =data['Income'].isna().sum() #1


import numpy as np
##4##

#a
arr = np.random.randint(0,10000, size=(4,2)) #dtype = int64
sqrt_arry = np.sqrt(arr)

arr = np.array(arr, dtype='int32')
'''
პატარა რიცხვებისთვის არანაირი ცვლილება არიქნება, 
მაგრამ თუ რიცხვი იმხელაა რომ 32 ბიტი არ ყოფნის ჩასაწერად 
რაღაც რაოდენობის ინფორმაციას დავკარგავთ.

და თუ ფესვამოღებული სია უნდა გადაგვეყვანა 
ამ სიის ტიპი float64 იქნებოდა და Int32-ში გადაყვანით
მხოლოდ მთელი რიხვები დაგვრჩება და ათწილადებს დავკარგავთ. 
'''