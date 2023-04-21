import jieba

file1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_word.txt"
# # file2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\testtxt.txt"
outfile1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_word_jc.txt"
# # outfile2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\testresult_j.txt"

with open(file1,'r',encoding="utf-8") as f1:
    lines1 = f1.read()
jieba.load_userdict(r'D:\Pycharm\MD\1109\featureword.txt')
seg = jieba.lcut(lines1)

with open(outfile1,'w',encoding="utf-8") as of1:
    for each in seg:
        if each != ' ':
            of1.write(each+"\\")


# with open(file2,'r',encoding="utf-8") as f2:
#     lines2 = f2.read()
#
# seg = jieba.lcut(lines2)
#
# with open(outfile2,'w',encoding="utf-8") as of2:
#     for each in seg:
#         of2.write(each+"\\")