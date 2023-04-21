# -*- coding:utf-8 -*-
import random
from itertools import groupby
def split(all_list, shuffle=False, ratio=0.7):
    num = len(all_list)
    offset = int(num * ratio)
    if num == 0 or offset < 1:
        return [], all_list
    if shuffle:
        random.shuffle(all_list)  # 列表随机排序
    train = all_list[:offset]
    test = all_list[offset:]
    return train, test

# 按照比例ratio将数据集按照句子级别划分训练集、测试集
def file_shffle_split(file, train, test, r):
    infilm = open(file, 'r', encoding='utf-8')
    trainfilm = open(train, 'w+', encoding='utf-8')
    testfilm = open(test, 'w+', encoding='utf-8')
    ratio = r
    li = []
    sentence = []
    for data in infilm.readlines():
        if data != '\n':
            li.append(data)
        else:
            sentence.append(li)
            li = []
    traindatas, testdatas = split(sentence, True, ratio)
    # 写入训练集
    for sentence in traindatas:
        for word in sentence:
            trainfilm.write(word)
        trainfilm.write('\n')
    # 写入测试集
    for sentence in testdatas:
        for word in sentence:
            testfilm.write(word)
        testfilm.write('\n')
    infilm.close()
    trainfilm.close()
    testfilm.close()

if __name__ == '__main__':
    # 设置划分比例 (ratio为训练集占比)
    ratio = 0.7
    # 划分数据集
    file_shffle_split('new_addblank_tpab11.txt', 'train11.txt', 'test11.txt', ratio)
