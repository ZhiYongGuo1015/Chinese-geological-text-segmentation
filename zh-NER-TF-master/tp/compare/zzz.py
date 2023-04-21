import codecs

f1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\Iteration1\test_word_standard_bio.txt"
f2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\Iteration1\test_word_bio.txt"
# f3 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\data_path\test_data_tpab.txt"

file_true = codecs.open(f1, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
file_pred = codecs.open(f2, mode='r', encoding='utf-8')


# file3 = codecs.open(f3, mode='r', encoding='utf-8')


def extract(file):
    line = file.readline()
    tag_list = []
    while line:
        a = line.split()
        b = a[0:1]  # 这是选取需要读取的位数
        for each in b:
            tag_list.append(each)  # 将其添加在列表之中
        line = file.readline()
    file.close()
    return tag_list


right = extract(file_true)
wrong = extract(file_pred)

# line = file3.readlines()
# i = 0
# for each in line:
#     if each == '。 O\r\n':
#         i = i+1
# print(i)
# file3.close()

for i in range(557855):
    if right[i] != wrong[i]:
        if '\u4e00' <= right[i] <= '\u9fa5':
            print(i)
            break
