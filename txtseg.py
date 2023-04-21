import os
import jieba
import sys
import re

import time
import jieba.posseg as pseg

import jieba
import jieba.posseg as pseg
import re

subs = [["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
         "“", "”", "<", ">"],# 子句分隔符
        ["+", "-", ".", "″", "′", "°"],  # 不分割连接符
        [],  #
        []]  # 被舍弃的头尾高频字符

jieba.load_userdict(r'D:\Pycharm\MD\1109\featureword.txt')  # 添加自定义词典
file = r'D:\Pycharm\MD\1109\corpus\new.txt'
outfile = open(r'D:\Pycharm\MD\1109\result\txtseg1.txt', "w", encoding='utf-8')


def isChinese(word):
    for a in word:
        if '\u4e00' <= a <= '\u9fa5':
            return True
    return False


file = open(file, 'r', encoding='utf-8')
try:
    while True:
        text_line = file.readline()
        text_line = text_line.strip()
        text_line = re.sub(r'(?<=[0-9])：(?=[0-9])', ':', text_line)
        text_line = re.sub(r'(?<=[a-zA-Z]):(?=[0-9])', '：', text_line)
        text_line = re.sub(r'(?<=[\u4e00-\u9fa5]):(?=[\u4e00-\u9fa5])', '：', text_line)
        if text_line:
            sub_sentence = []
            last_pos = 0
            for j in range(len(text_line)):
                if text_line[j] in subs[0]:
                    if j > 0:
                        sub_sentence.append(text_line[last_pos:j])
                    sub_sentence.append(text_line[j])
                    last_pos = j + 1
            if last_pos < len(text_line):
                sub_sentence.append(text_line[last_pos:])
            segments = []
            for sentence in sub_sentence:
                if isChinese(sentence):
                    pos = []
                    for i in re.finditer(u'[^\u4e00-\u9fa5]{2,}', sentence):
                        pos.append(i.start())
                        pos.append(i.end())
                    if 0 not in pos:
                        pos.append(0)
                    if len(sentence) not in pos:
                        pos.append(len(sentence))
                    pos = sorted(list(pos), reverse=False)
                    for i in range(len(pos)):
                        if i < len(pos) - 1:
                            segments.append(sentence[pos[i]:pos[i + 1]])
                else:
                    segments.append(sentence)

            for each in segments:
                if isChinese(each):
                    words = jieba.cut(each, HMM=True)  # 精确模式
                    outstr1 = ""
                    for word in words:
                        if word != '\t':
                            outstr1 += word + '\\'
                    outfile.writelines(outstr1)
                else:
                    outstr2 = ""
                    if each != '\t':
                        outstr2 += each + '\\'
                    outfile.writelines(outstr2)
        else:
            break

finally:
    outfile.close()