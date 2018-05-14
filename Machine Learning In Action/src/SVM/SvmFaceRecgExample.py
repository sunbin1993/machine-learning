'''
Created on May 3, 2018

@author: eusinnb
'''
from __future__ import print_function
from time import time
import logging
import matplotlib.pyplot as plt #绘图
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC #核心
from sklearn.cluster.tests.test_k_means import n_samples
from sklearn.tests.test_multiclass import n_classes

print(__doc__)

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

lfw_people = fetch_lfw_people(min_faces_per_person=70,resize=0.4)

n_samples,h,w=lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]

y=lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_sample:%d " % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)












