subs = ["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
        "“", "”", "<", ">", "+", "-", ".", "″", "′"]
file = r'D:\Pycharm\MD\1109\result\txtseg_standard.txt'
outfile = r'D:\Pycharm\MD\1109\result\Bio_standard2.txt'
file = open(file, 'r', encoding='utf-8')
outfile = open(outfile, 'w', encoding='utf-8')
text_line = file.readline()
text_line = text_line.split('/')
for each in text_line:
    if len(each) == 1:
        if each in subs:
            outfile.write(each + ' ' + 'O\n')
        else:
            outfile.write(each + ' ' + 'B\n')
    if len(each) > 1:
        outfile.write(each[0] + ' ' + 'B\n')
        for w in each[1:len(each)]:
            if w == ' ':
                pass
            else:
                outfile.write(w + ' ' + 'I\n')
