'''
Created on Apr 17, 2018

@author: eusinnb
'''
from sklearn import svm

X = [[2,0],[1,1],[2,3]]
y = [0,0,1] #label
clf = svm.SVC(kernel="linear")#线性核函数
clf.fit(X,y) #建立模型  fit

print(clf)

# get support vectors
print(clf.support_vectors_)

# get index of support vectors
print(clf.support_)

# get number of support vectors for each class
print(clf.n_support_)

print(clf.predict([[2, .0]]))