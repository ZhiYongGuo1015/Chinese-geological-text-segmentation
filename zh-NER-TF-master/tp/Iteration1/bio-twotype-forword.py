subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"]
file = r'D:\Pycharm\MD\1109\zh-NER-TF-master\tp\Iteration1\newwords1-delete.txt'
file2 = r'D:\Pycharm\MD\1109\zh-NER-TF-master\tp\Iteration1\txtseg_standard.txt'
outfile = r'D:\Pycharm\MD\1109\zh-NER-TF-master\tp\Iteration1\newwords_bion1.txt'

with open(file, 'r', encoding='utf-8') as f:
    lines = f.read()

lines = lines.split('\n')

with open(file2,'a',encoding="utf-8") as f2:
    for each in lines:
        f2.write(each+'\\')

outfile = open(outfile, 'w', encoding='utf-8')


def isChinese(word):
    for a in word:
        if '\u4e00' <= a <= '\u9fa5':
            return True
    return False


for each in lines:
    if len(each) == 1:
        if each in subs:
            outfile.write(each + ' ' + 'O\n')
        elif isChinese(each):
            outfile.write(each + ' ' + 'B-CH\n')
        elif not isChinese(each):
            outfile.write(each + ' ' + 'B-SP\n')
    if len(each) > 1:
        if isChinese(each):
            outfile.write(each[0] + ' ' + 'B-CH\n')
            for w in each[1:len(each)]:
                if w == ' ':
                    pass
                else:
                    outfile.write(w + ' ' + 'I-CH\n')
        if not isChinese(each):
            outfile.write(each[0] + ' ' + 'B-SP\n')
            for w in each[1:len(each)]:
                if w == ' ':
                    pass
                else:
                    outfile.write(w + ' ' + 'I-SP\n')
    outfile.write("。"+" "+"O\n"+'\n')
# outfile.write("。"+" "+"O\n")
outfile.close()
