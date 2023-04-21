subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"]
file = r'D:\Pycharm\MD\1109\result\testtxt.txt'
outfile = r'D:\Pycharm\MD\1109\result\test_data_oc.txt'

with open(file,'r',encoding='utf-8') as f:
    lines = f.read()
    words = lines.split('\\')

outfile = open(outfile, 'w', encoding='utf-8')
def isChinese(word):
    for a in word:
        if '\u4e00' <= a <= '\u9fa5':
            return True
    return False

for each in words:
    if len(each) == 1:
        if each in subs:
            outfile.write(each + ' ' + 'O\n')
        elif isChinese(each):
            outfile.write(each + ' ' + 'B\n')
    if len(each) > 1:
        if isChinese(each):
            outfile.write(each[0] + ' ' + 'B\n')
            for w in each[1:len(each)]:
                if w == ' ':
                    pass
                else:
                    outfile.write(w + ' ' + 'I\n')
outfile.close()