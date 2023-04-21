# coding=utf-8
import pynlpir
import os

pynlpir.open(encoding="utf-8")

# dict_path = bytes(r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\user_dict.txt", "utf-8")
pynlpir.nlpir.ImportUserDict(b"D:\\Pycharm\\MD\\1109\\zh-NER-TF-master\\tp\\compare\\user_dict.txt")

with open(r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\featureword.txt", encoding="utf-8") as f:
    word = f.read()
words = word.split('\n')
# for each in words:
# pynlpir.nlpir.AddUserWord('卡卡')
file1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new.txt"
outfile1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new_nc.txt"

with open(file1, 'r', encoding="utf-8") as f1:
    lines1 = f1.read()
txt = pynlpir.segment(lines1)

with open(outfile1, 'w', encoding="utf-8") as f2:
    for t in txt:
        if t[0] != ' ':
            f2.write(t[0] + '\\')

pynlpir.close()
