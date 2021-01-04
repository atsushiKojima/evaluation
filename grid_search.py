# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:00:57 2021

@author: a-kojima
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:31:42 2020

@author: a-kojima

accuracy, Precision
 F1 score
 Sensitivity/Recall
 Specificity

"""
import sys

import matplotlib.pyplot as pl

def get_dict(file_path_):
    dict_ = {}
    f  = open(file_path_, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        tmp = line.replace('\n', '').split('\t')
        if len(tmp) == 2:
            dict_[tmp[0]] = tmp[1]
    return dict_

def get_dict2(file_path_):
    dict_ = {}
    f  = open(file_path_, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        tmp = line.replace('\n', '').split('\t')
        if len(tmp) == 2:
            dict_[tmp[0]] = float(tmp[1].split(',')[0])
    return dict_

def accuracy_all(dic_correct, dic_predict):
    npys = list(dic_correct.keys())    
    correct = 0
    for npy in npys:
        
        if dic_correct[npy] == dic_predict[npy]:
           correct+=1
    return correct / len(npys)
    
def Specificity(dic_correct, dic_predict):
    npys = list(dic_correct.keys())    
    sample = 0
    correct = 0
    for npy in npys:
        if dic_predict[npy] == 'H':
            sample+=1
            if dic_correct[npy] == dic_predict[npy]:
               correct+=1
    return correct / sample


def precision(dic_correct, dic_predict):
    npys = list(dic_correct.keys())    
    sample = 0
    correct = 0
    for npy in npys:
        if dic_predict[npy] == 'D':
            sample+=1
            if dic_correct[npy] == dic_predict[npy]:
               correct+=1
    return correct / sample


def recall(dic_correct, dic_predict):
    npys = list(dic_correct.keys())    
    sample = 0
    correct = 0
    for npy in npys:
        if dic_correct[npy] == 'D':
            sample+=1
            if dic_correct[npy] == dic_predict[npy]:
               correct+=1
    return correct / sample


t1 = r'\\ami-storage\CTD_Works\a-kojima\hayashi_work\correct_label.txt'
#t2 = r'C:\Users\a-kojima\Documents\work_python\C_ken_friends\result_logistic_result_05_prob2.txt'
t2 = sys.argv[1]

threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

l1 = get_dict(t1)
l2 = get_dict2(t2)


pre_all = []
recall_all = []
f_all = []
sp_all = []
accu_all = []

jj = list(l2.keys())
for th in threshold:
    gg = {}
    for kk in jj:
        if th < l2[kk]:
            gg[kk] = 'D'
        else:
            gg[kk] ='H'
            
    accu_all.append(accuracy_all(l1, gg))
    
    pre = precision(l1, gg)
    recall_ = recall(l1, gg)
    f = 2 * recall_ * pre / (recall_ + pre)
    
    f_all.append(f)
    pre_all.append(pre)
    recall_all.append(recall_)
    
    sp_all.append(Specificity(l1, gg))
            

pl.figure()
pl.plot(threshold, f_all, 'b')

pl.plot(threshold, pre_all, 'r')




pl.plot(threshold, recall_all, 'k')

pl.plot(threshold, sp_all, 'y')

pl.plot(threshold, accu_all, 'c')


pl.legend(['f_value', 'precision', 'recall', 'specificity', 'accuracy'])



pl.plot(threshold, f_all, 'bo')
pl.plot(threshold, pre_all, 'ro')
pl.plot(threshold, recall_all, 'ko')
pl.plot(threshold, sp_all, 'yo')
pl.plot(threshold, accu_all, 'co')

pl.grid()
pl.show()

