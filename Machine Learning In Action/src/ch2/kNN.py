from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

'''
inX:分类的输入向量
dataSet:输入的训练样本集
labels:标签向量
k:选择最近邻居的数目
'''
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0] # 第一维的长度 shape函数:查看矩阵或数组的维数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet  #tile函数：重复某个数组，tile(A,n)，功能是将数组A重复n次，构成一个新的数组
    sqDiffMat = diffMat ** 2 # x ** y 返回x的y次幂
    sqDistances = sqDiffMat.sum(axis=1)# sum(iterable[, start]) iterable -- 可迭代对象，如列表。start -- 指定相加的参数，如果没有设置这个值，默认为0。 
                                       # 对于二维数组 axis=1表示按行相加 , axis=0表示按列相加
    distances = sqDistances ** 0.5 
    sortedDistIndicies = distances.argsort()# argsort 返回的是数组值从小到大的索引值
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
    key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
    