from seqeval.metrics import f1_score
from seqeval.metrics import precision_score
from seqeval.metrics import accuracy_score
from seqeval.metrics import recall_score
from seqeval.metrics import classification_report
import codecs
import re

subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"]


def getbio(lines):
    pred1 = []
    words = lines.split('\\')
    for each in words:
        if len(each) == 1:
            if each in subs:
                pred1.append('O')
            else:
                pred1.append("B")
        if len(each) > 1:
            for i in range(len(each)):
                if i == 0:
                    pred1.append('B')
                else:
                    pred1.append('I')
    return pred1


txtfile = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new.txt"
standardfile = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\ts_bio.txt"

with open(txtfile, 'r', encoding="utf-8") as f1:
    sentence1 = f1.read()

with open(standardfile, 'r', encoding="utf-8") as f2:
    sentence2 = f2.read()

sentence2 = sentence2.split('\n')

lines = r"熊耳山\西段\金\异常\主要\分布\在\蒿\坪\沟\矿区\\"
lines1 = re.sub(r'\\', '', lines)

y_true = []
y_pred = []
res = []
if lines1 in sentence1:
    y_pred.append(getbio(lines))
    for i in range(len(sentence1) - len(lines1) + 1):
        if sentence1[i] == lines1[0] and sentence1[i:i + len(lines1)] == lines1:
            for j in range(len(lines1)):
                res.append(sentence2[i + j][2:3])
y_true.append(res)

# print("accuary: ", accuracy_score(y_true, y_pred))
# print("p: ", precision_score(y_true, y_pred))
# print("r: ", recall_score(y_true, y_pred))
print("%.2f" % (f1_score(y_true, y_pred)*100) + "%")
# # # print("classification report: ")
# # # print(classification_report(y_true, y_pred))
