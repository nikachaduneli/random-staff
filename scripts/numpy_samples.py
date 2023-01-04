import numpy as np




a = np.array([1,2,3,4])

b = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#get dimentions
print('a.ndim: ',a.ndim)

#get Shape
print('a.shape:',a.shape)

#Get type
print('a.dtype:',a.dtype)

#specify dType
a = np.array([1,2,3,4],dtype = 'int16')

#Get Itemsize in bites
print('a.itemsize: ',a.itemsize)

#get size of array
print('a.size: ',a.size)

#total size in bites
print('a.nbytes:',a.nbytes, end = "\n \n")


print("IN TWO DIMETIONS", end = "\n \n")


#Get element
print('Get element: b[1,2] ->', b[1,2])

#Get specific row
print('Get specific row: b[1,] ->',b[1,])

#Get specific column
print('Get specific column: b[:,1] ->',b[:,1])

#slicing
print('slicing: b[0,2:-1] ->',b[0,2:-1])

#change element
b[1,2]=2
print('change element: b[1,2]=2 ->',b[1,2],end='\n \n')

#Create matrix of zeros
zeros = np.zeros((3,3))
print('Create matrix(3,3) of zeros np.zeros((3,3)):\n' ,zeros)

#Create matrix of ones
ones = np.ones((3,3))
print('Create matrix(3,3) of ones np.ones((3,3)):\n' ,ones)

#matrix of any number
matr = np.full((3,3),17)
print('Create matrix(3,3) of any number np.full((3,3),17):\n' ,matr)

#matrix of random numbers
rmatr = np.random.randint(1,12,size=(3,3))
print('Create matrix(3,3) of random numbers np.random.randint(from-1,to-12,size = (3,3)):\n' ,rmatr, end='\n \n')

##COPYING##
a = np.array([1,2,3])
b = a.copy()
b[1]=100

## MATHEMATICS ##
print('MATHEMATICS')
print('a: ',a)
print('a+2: ',a+2)
print('a*3: ',a*3)
print('np.sin(a): ',np.sin(a),end='\n \n')

print('LINEAR ALGEBRA')
a = np.full((2,3),1)
b = np.full((3,2),2)
print('a:', '\n',a, '\n','b: ', '\n',b)

print('gamravleba -> np.matmul(a,b): \n',np.matmul(a,b))
c = np.identity(4)
print('c: \n',c)
print('determinanti -> np.linalg.det(c):',np.linalg.det(c),'\n')


## STATISTICS ##
print('STATISTICS')
stats = np.array([[1,2,3,2],[3,1,1,9],[3,1,1,2]])
print('stats:\n',stats)
print('np.max(stats,axis=0)',np.max(stats,axis=0))
print('np.sum(stats): ',np.sum(stats))



##REORGANIZE##

#change shape

print('reshape stats -> stats.reshape(4,3)\n',stats.reshape(4,3))



## LOAD FROM FILE ##
data = open('txtsss/numpy_data.txt','r')

from_txt = np.genfromtxt(data,delimiter=',',dtype='int32')
print('from_txt: ',from_txt)
