# coding=utf -8

import fnmatch
import os
from win32com import client as wc
from win32com.client import Dispatch
'''
功能描述：word文件转存txt,默认保存在根目录下，支持自定义
参数描述：1 filePath 文件路径 2 savePath:保存路径
'''


def Word2Txt(filePath, savePath=''):
    dirs, filename = os.path.split(filePath)
    # print(dirs, '\n', filename)
    new_name = " "
    if fnmatch.fnmatch(filename, '*.doc'):
        new_name = filename[:-4] + '.txt'
    elif fnmatch.fnmatch(filename, '*.docx'):
        new_name = filename[:-5] + '.txt'
    else:
        print('格式不正确，仅支持doc or docx 格式。')
        return

    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    word2txtPath = os.path.join(savePath, new_name)
    print('-->', word2txtPath)

    wordapp1 = wc.gencache.EnsureDispatch('Word.Application')
    mytxt1 = wordapp1.Documents.Open(filePath)

    mytxt1.SaveAs(word2txtPath, 4)  # 参数4
    mytxt1.Close()


if __name__ == '__main__':
    filePath = os.path.abspath(r'D:\Pycharm\论文整理\数据\原始文件\2012.5陕县葫芦峪金矿生产勘探工作总结.doc')
    Word2Txt(filePath)
