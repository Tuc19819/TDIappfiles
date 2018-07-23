import glob
import numpy as np
import pandas as pd


path = 'C:\\Users\\Administrator\\Desktop\\data.07.22.18\\bbc-fulltext\\bbc\\test\*.*'   
files=glob.glob(path)

hold=0
store=np.array([])#[];
store=np.array([])#[];
i=0
for file in files:

    f=open(file, 'r')  
    #print ('%s' % f.readlines())
    #print (f.readlines())
    #store[i] = f.readlines()
    store1=f.readlines()
    store=np.append(store,store1)
    #print(store1)
    #store=np.append(f.readlines())

    #print(store[i])
    f.close()
    i=i+1
#print(store[0])
#print('')
#print (store[2])

df=pd.DataFrame(store,dtype='str')
df.to_csv('bbc2.csv')
print(df.iloc(0))
