import numpy as np

mylist = [1,2,3]

mylist2 = np.array([1,2,3])

mylist3 = np.arange(1,10)

mylist4 = np.arange(1,10,2)

mylist5 = np.zeros((3,2))
#print(mylist5)

mylist6 = np.ones((8,7))
#print(mylist6)

mylist7 = np.random.randint(1,100,10)

mylist7.max()

mylist7.min()

mylist7.argmax()

mylist7.argmin()

mylist7.mean()

mylist7.shape

mylist7.reshape((2,5)) 

mat = np.arange(0,100).reshape((10,10))

mat.shape

mat[3,5]

mat[:,1] # 2. sütunumuzu komple bize verir.

mat[5,:]

mat[0:2,0:2]

copy = mat.copy() # bu işlem ile adresimizi kopyalamk yerine sadece verilerimizi koyalarız.






