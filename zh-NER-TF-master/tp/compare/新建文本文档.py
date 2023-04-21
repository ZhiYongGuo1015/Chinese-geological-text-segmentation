file = r'D:\Pycharm\MD\1109\featureword.txt'
outfile = r'D:\Pycharm\MD\1109\TCPM-R.txt'
with open(file,'r',encoding="utf-8") as f:
    lines = f.read()

lines = lines.split('\n')

with open(outfile,'w',encoding='utf-8') as f2:
    for each in lines:
        f2.write(each + '\\')