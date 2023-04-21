file1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\txtseg_standard2_20220303_103707_segment.txt"
file2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\featureword2.txt"

f1 = open(file1, 'r', encoding='utf-8')
f2 = open(file2, 'w', encoding='utf-8')
textline = f1.read()
text_line = textline.split('\\')
for each in text_line:
    f2.write(each + '\t' + 'n'+'\n')
f1.close()
f2.close()
