# coding: utf-8

import re
import os
import sys
import re
import time

# 保留字母、数字、汉字和标点符号(),.!?":
def remove_others(s):
    return re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5(),.!?":《》、；：，。～′—（）″°/—%×—‘’“”—]', ' ', s)

# 删除多余的空白(including spaces, tabs, line breaks)'''
def remove_whitespaces(s):
    # return re.sub(r'\s{2,}', ' ', s)
    return re.sub(r' ', '', s)


def readFile(path):
    str_doc = ""
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

# def addjuhao(path):
#     print("添加句号")
#     # stopwords = {}.fromkeys([line.rstrip() for line in open(stop, "r",encoding='utf-8')])  # 添加停用词表
#     file = open(path, 'r', encoding='utf-8')
#     outfile = open(r'../corpus/data/data/任村processed.txt', "w", encoding='utf-8')
#     try:
#         while True:
#             text_line = file.readline()
#             text_line = text_line.strip()
#             if text_line:
#                 if text_line[len(text_line) - 1] == '，':
#                     text_line = text_line[0:len(text_line) -1]+ '。'
#                     outfile.writelines(text_line + '\n')
#                 elif text_line[len(text_line) - 1] == '；':
#                     text_line = text_line[0:len(text_line) -1]+ '。'
#                     outfile.writelines(text_line + '\n')
#                 elif text_line[len(text_line) - 1] == '。':
#                     outfile.writelines(text_line + '\n')
#                 else:
#                     text_line = text_line + '。'
#                     outfile.writelines(text_line + '\n')
#             else:
#                 break
#
#     finally:
#         outfile.close()


if __name__ == '__main__':
    # 1 读取文本
    path = r'D:\Pycharm\MD\1109\任村矿调报告（地质部分）终稿.md'
    # str_doc = readFile(path)
    # print(str_doc)
    out = r'D:\Pycharm\MD\1109\任村矿调报告（地质部分）终稿1.md'
    inputs = open(path, 'r', encoding='UTF-8')
    outfile = open(out, 'w', encoding='UTF-8')

    # 2 数据清洗
    for line in inputs.readlines():
        if line == '\n':
            text_line = line.rstrip('\n')
        else:
          stag1 = remove_others(line)   # 去符号
          stag2 = remove_whitespaces(stag1)    # 删空格
          # if len(stag2) > 25:#去掉小于25个字符的行
          #     if stag2[len(stag2) - 1] == '，':    #在每句话后面加上句号
          #         stag2 = stag2[0:len(stag2) - 1] + '。'
          #         outfile.writelines(stag2 + '\n')
          #     elif stag2[len(stag2) - 1] == '；':
          #         stag2 = stag2[0:len(stag2) - 1] + '。'
          #         outfile.writelines(stag2 + '\n')
          #     elif stag2[len(stag2) - 1] == '：':
          #         stag2 = stag2[0:len(stag2) - 1] + '。'
          #         outfile.writelines(stag2 + '\n')
          #     elif stag2[len(stag2) - 1] == '。':
          #         outfile.writelines(stag2 + '\n')
          #     else:
          #         stag2 = stag2 + '。'
          outfile.writelines(stag2 + '\n')
    inputs.close()
    outfile.close()