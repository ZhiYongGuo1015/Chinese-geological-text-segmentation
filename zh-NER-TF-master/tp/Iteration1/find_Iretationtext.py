f1 = open(r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\train_data_tpab.txt', 'r', encoding='utf-8')
f2 = open(r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\Iteration1\Iteration_file2.txt', 'w', encoding='utf-8')
line = f1.readline()
list1 = []
while line:
    a = line.split()
    b = a[0:1]
    c = a[1:2]
    if c in [['B-CH'], ['B-SP'],['O']]:
        list1.append('\\')
        list1.append(b)
    else:
        list1.append(b)
    line = f1.readline()
f1.close()

for each in list1:
    for word in each:
        f2.write(word)
