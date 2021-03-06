#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成词向量空间"""

from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
import numpy as np
import logging
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# sentencestest = [['中国', '人'], ['美国', '人']]
# # train word2vec on the two sentences
# model = gensim.models.Word2Vec(sentences, min_count=1)
#
# print model["中国"]


# class MySentences1(object):
#
#     def __init__(self, dir_name):
#         self.dir_name = dir_name
#         self.do()
#
#     def do(self):
#         res = []
#         for file_name in os.listdir(self.dir_name):
#             for line in open(os.path.join(self.dir_name, file_name)).readlines():
#                 res.append(line.strip())
#         return res


# 读取文件夹中的所有数据
# class MySentences(object):
#     def __init__(self, dir_name):
#         self.dir_name = dir_name
#
#     def __iter__(self):
#         for file_name in os.listdir(self.dir_name):
#             for line in open(os.path.join(self.dir_name, file_name)):
#                 yield line.split(",")

# #  a memory-friendly iterator
# sentences = MySentences('/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data')
# sentences = MySentences('/Users/li/Kunyan/DataSet/trainingSets')  # a memory-friendly iterator


# 按照标签读取数据
#
# def read_data(pos_file_path, neg_file_path):
#     with open(pos_file_path) as input_file:
#         pos_file = input_file.readlines()
#         resp = []
#         for p in pos_file:
#             resp.append(p.split(","))
#
#     with open(neg_file_path) as input_file:
#         neg_file = input_file.readlines()
#         resn = []
#         for n in neg_file:
#             resn.append(n.split(","))
#
#     res = (resp, resn)
#     return res

def read_data(pos_file_path, neg_file_path):
    with open(pos_file_path) as input_file:
        pos_file = input_file.readlines()

    with open(neg_file_path) as input_file:
        neg_file = input_file.readlines()

    res = (pos_file, neg_file)
    return res

# 数据预处理,设置标签,训练集测试集准备
def data_split(pos_file, neg_file):
    # 标签
    label = np.concatenate((np.ones(len(pos_file)), np.zeros(len(neg_file))))

    # 训练集,测试集
    x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos_file, neg_file)), label, test_size=0.1)

    res = (x_train, x_test, y_train, y_test)
    return res


def text_clean(corpus):
    corpus = [z.lower().replace('\n', ' ').split(',') for z in corpus]
    return corpus
