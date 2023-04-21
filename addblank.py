import os

import sys
import re

import time
#import jieba.posseg as pseg

#import jieba
def addblank(path):  # 在以‘。’结尾的每句话后面添加一个空行，形成深度学习模型训练的标准模式
    file = open(path, 'r', encoding='utf-8')
    #outfile = open(r'D:\Pycharm\MD\1109\result\train_data_tpab.txt', "w", encoding='utf-8')
    outfile = open(r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\new_addblank_tpab11.txt', "w", encoding='utf-8')
    try:
        while True:
            text_line = file.readline()
            text_line = text_line.strip()
            if text_line:
                if text_line == '。 O':
                    outfile.writelines(text_line + '\n' + '\n')
                else:
                    outfile.writelines(text_line + '\n')

            else:
                break
    finally:
        outfile.close()


if __name__ == '__main__':
    addblank(r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\new_addblank_tpab.txt')
