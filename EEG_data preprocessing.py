import pandas as pd
import numpy as np

file_name = '/home/kelab/PycharmProjects/EEG Confusing/EEG_data.csv'
data = pd.read_csv(file_name)
#print(data.head())

index = []
y = []
X = []
xx = []
length = []

def datatolist(data):
    datalist = np.mat(data)
    datalist = np.ndarray.tolist(datalist)
    return datalist

subject = data['SubjectID']
VideoID = data['VideoID']
subject = datatolist(subject)
VideoID = datatolist(VideoID)


def getindex(subject,video,n,m):
    for i in range(len(subject[0])):
        if subject[0][i] ==n:
            if video[0][i] == m:
                index.append(i)
    return index
def length(subject,VideoID):
    length = []
    for i in range(10):
        for j in range(10):
            indexs = getindex(subject,VideoID,i,j)
            length.append(indexs)
    return length
feature = ['Raw','Delta','Theta','Alpha1','Alpha2','Beta1','Beta2','Gamma1','Gamma2']
Y = data['user-definedlabeln']
Y = datatolist(Y)
def getlabel(Y,length):
    for i in length:
        t = Y[0][i-1]
        n = int(t)
        y.append(n)
    return y

def getX(subject,VideoID,length):
    for i in range(10):
        for j in range(10):
            indexs = getindex(subject,VideoID,i,j)
            length.append(len(indexs))
    feature = ['Raw', 'Delta', 'Theta', 'Alpha1', 'Alpha2', 'Beta1', 'Beta2', 'Gamma1', 'Gamma2']
    for feature in feature:
        xx.append(data[feature])
    for length in length:
        x = []
        for m in range(9):
            x.append((xx[m][length+1 : length + 120]))
        X.append(x)