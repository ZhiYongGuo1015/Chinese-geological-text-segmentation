from pyhanlp import *
import time
file1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new.txt"
# file2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\testtxt.txt"
outfile1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new_h.txt"
# outfile2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\testresult_h.txt"

with open(file1,'r',encoding="utf-8") as f1:
    lines1 = f1.read()


with open(outfile1,'w',encoding="utf-8") as of1:
    for each in seg:
        if each.word != ' ':
            of1.write(each.word+"\\")


with open(file2,'r',encoding="utf-8") as f2:
    lines2 = f2.read()

seg1 = HanLP.segment(lines2)

with open(outfile2,'w',encoding="utf-8") as of2:
    for each in seg1:
        of2.write(each.word+"\\")