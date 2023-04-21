from seqeval.metrics import f1_score
from seqeval.metrics import precision_score
from seqeval.metrics import accuracy_score
from seqeval.metrics import recall_score
from seqeval.metrics import classification_report
import codecs


def extract(file):
    line = file.readline()
    tag_list = []
    while line:
        a = line.split()
        b = a[1:2]  # 这是选取需要读取的位数
        for each in b:
            tag_list.append(each)  # 将其添加在列表之中
        line = file.readline()
    file.close()
    return tag_list


f1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_standard_bio.txt"
f2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_word_jc_bio.txt"

file_true = codecs.open(f1, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
file_pred = codecs.open(f2, mode='r', encoding='utf-8')

true1 = extract(file_true)
pred1 = extract(file_pred)

y_true = []
y_pred = []

y_true.append(true1)
y_pred.append(pred1)

print("accuary: ", accuracy_score(y_true, y_pred))
print("p: ", precision_score(y_true, y_pred))
print("r: ", recall_score(y_true, y_pred))
print("f1: ", f1_score(y_true, y_pred))
# # print("classification report: ")
# # print(classification_report(y_true, y_pred))
