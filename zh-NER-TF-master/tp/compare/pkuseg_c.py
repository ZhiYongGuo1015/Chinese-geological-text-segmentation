import pkuseg

file1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new.txt"
outfile1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\new_pc.txt"

with open(file1, 'r', encoding="utf-8") as f1:
    lines1 = f1.read()

seg = pkuseg.pkuseg(user_dict=r'D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\featureword.txt')           # 以默认配置加载模型
result = seg.cut(lines1)

with open(outfile1, 'w', encoding="utf-8") as f2:
    for each in result:
        if each != ' ':
            f2.write(each + '\\')