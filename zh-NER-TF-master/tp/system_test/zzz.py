import codecs

f1 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_standard_bio.txt"
# f2 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\system_test\test_word_bio.txt"
# f3 = r"D:\Pycharm\MD\1109\zh-NER-TF-master\data_path\test_data_tpab.txt"

file_true = codecs.open(f1, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取


# file_pred = codecs.open(f2, mode='r', encoding='utf-8')


# file3 = codecs.open(f3, mode='r', encoding='utf-8')


def extract(file):
    line = file.readline()
    tag_list = []
    word_list = []
    while line:
        a = line.split()
        b = a[0:1]  # 这是选取需要读取的位数
        c = a[1:2]
        for eachb in b:
            word_list.append(eachb)
        for each in c:
            tag_list.append(each)  # 将其添加在列表之中
        line = file.readline()
    file.close()
    return tag_list, word_list


right, word1 = extract(file_true)
wrong,word2 = extract(file_pred)

# line = file3.readlines()
# i = 0
# for each in line:
#     if each == '。 O\r\n':
#         i = i+1
# print(i)
# file3.close()
for i in range(len(right)):
    if word1[i]

    if right[i] == 'O' and right[i + 1] == 'O':

        # print(wordl[i+1] +  " " +right[i+1])
        break
