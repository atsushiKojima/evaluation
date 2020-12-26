# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:20:07 2020

@author: a-kojima
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
"""

from sklearn.linear_model import LogisticRegression
import pickle
import os
import numpy as np

import matplotlib.pyplot as pl

def get_npy_list(file_path_):
    f = open(file_path_, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    dump = []
    
    for line in lines:
        split_line = line.replace('\n', '').split('\t')
        if len(split_line) == 4:
            features = split_line[3]
            npy_path =  feature_path + '/' + os.path.basename(features)
            dump.append(np.load(npy_path))
    return np.reshape(np.array(dump), [len(dump), 300]), len(dump)
    

# ============================
# padams.
# ============================
feature_path = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\sentence_vector'

train_h = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\amed-text-data\parameters\parameter_list_H_train.txt'
train_d = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\amed-text-data\parameters\parameter_list_D_train.txt'

test_h = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\amed-text-data\parameters\parameter_list_H_test.txt'
test_d = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\amed-text-data\parameters\parameter_list_D_test.txt'

X_h, a = get_npy_list(train_h)
X_d, b = get_npy_list(train_d)
weight=  {1:0.5, 0:0.5}
features_train = np.concatenate((X_h, X_d), 0)
label = np.zeros(a+b)
label[:a] = 1

X_h, a = get_npy_list(test_h)
X_d, b = get_npy_list(test_d)
features_test = np.concatenate((X_h, X_d), 0)
#label = np.zeros(a+b)
#label[:, :a] = 1




#clf = LogisticRegression(solver='liblinear', C=1,  random_state=0).fit(features_train, label)
clf = LogisticRegression(random_state=0, max_iter=1000, class_weight=weight).fit(features_train, label)

# gg = clf.predict_proba(features_test)

#pickle.dump(sample_list,f)

#filename = 'finalized_model.sav'
pickle.dump(clf, open('logistic1225_05.sav', 'wb'))


# pl.figure()
# pl.plot(gg)
# pl.show()

