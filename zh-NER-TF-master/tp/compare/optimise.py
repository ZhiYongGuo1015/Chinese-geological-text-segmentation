import re

file = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\txtseg_standard2_20220303_103707_segment.txt"

f = open(file, 'r', encoding='utf-8')
textline = f.read()

timeline = re.findall(r"年\\[0-9][1-9]?月", textline)
print(timeline)
f.close()
