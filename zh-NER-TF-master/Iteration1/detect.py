subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"," "]

originaltxt = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\Iteration1\Iteration_file2.txt'
newtxt = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\tp\Iteration1\Iteration_result1.txt'
newwordstxt = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\tp\Iteration1\newwords1.txt'
newwords_bio = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\tp\Iteration1\newwords_bio1.txt'

def readtxt(file):
    f = open(file, 'r', encoding='utf-8')
    lines = f.read()
    f.close()
    return lines


originallines = readtxt(originaltxt)
originallist = originallines.split('\\')

newlines = readtxt(newtxt)
newlist = newlines.split('\\')

print(len(originallist))
f1 = open(newwordstxt, 'w', encoding='utf-8')
i = 1
newwords = []
for each in newlist:
    if each not in originallist:
        newwords.append(each)
        i = i + 1
print(i)

for each in newwords:
    f1.write(each + '\n')
f1.close()

# f2 = open(newwords_bio, 'w', encoding='utf-8')
# for each in newwords:
#     if len(each) == 1:
#         if each in subs:
#             f2.write(each + ' ' + 'O\n')
#         else:
#             f2.write(each + ' ' + 'B\n')
#     if len(each) > 1:
#         f2.write(each[0] + ' ' + 'B\n')
#         for w in each[1:len(each)]:
#             if w == ' ':
#                 pass
#             else:
#                 f2.write(w + ' ' + 'I\n')
# f2.close()