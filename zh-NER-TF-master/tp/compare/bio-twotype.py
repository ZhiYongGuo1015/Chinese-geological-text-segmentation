subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"]
file = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\txtseg_standard.txt"
outfile = r"D:\Pycharm\MD\1109\zh-NER-TF-master\tp\compare\txtseg_bio_tp.txt"

with open(file, 'r', encoding='utf-8') as f:
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
            if each == '。':
                outfile.write(' ' + each + ' ' + 'O\n' + '\n')
            else:
                outfile.write(' ' + each + ' ' + 'O\n')
        elif isChinese(each):
            outfile.write(' ' + each + ' ' + 'B-CH\n')
        elif not isChinese(each):
            outfile.write(' ' + each + ' ' + 'B-SP\n')
    if len(each) > 1:
        if isChinese(each):
            outfile.write(' ' + each[0] + ' ' + 'B-CH\n')
            for w in each[1:len(each)]:
                if w == ' ':
                    pass
                else:
                    outfile.write(' ' + w + ' ' + 'I-CH\n')
        if not isChinese(each):
            outfile.write(' ' + each[0] + ' ' + 'B-SP\n')
            for w in each[1:len(each)]:
                if w == ' ':
                    pass
                else:
                    outfile.write(' ' + w + ' ' + 'I-SP\n')
outfile.close()
