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
#t2 = r'C:\Users\a-kojima\Documents\work_python\C_ken_friends\result_logistic_result.txt'
t2 = sys.argv[1]

l1 = get_dict(t1)
l2 = get_dict(t2)

print('accuracy=', accuracy_all(l1, l2))
pre = precision(l1, l2)
recall = recall(l1, l2)
f = 2 * recall * pre / (recall + pre)
print('precsion=', pre)
print('recall=', recall)
print('F-value=', f)
print(' Specificity', Specificity(l1, l2))

