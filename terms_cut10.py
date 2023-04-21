import sys
from collections import Counter
import time
import numpy as np
import re

subs = [["。", "，", "；", "！", "：", ",", "、", " ", "*", ";", "（", "）", "(", ")", "〔", "〕", "[", "]", "《", "》",
         "“", "”", "<", ">"],
        # 子句分隔符
        ["+", "-", ".", "″", "′", "°"],  # 不分割连接符
        [],  #
        []]  # 被舍弃的头尾高频字符
# files = [r"D:\Pycharm\MD\1109\任村矿调报告（地质部分）终稿.md",
#          r"D:\Pycharm\MD\1109\遥感报告.md"]
dicts = r"D:\Pycharm\MD\1109\词频字典4.txt"
files = [r"D:\Pycharm\MD\论文整理\corpus\new.txt"]
std_ratio = 0.2


# 获取字符串中的中文字符
def is_Chinese(word):
    import re
    res = ''.join(re.findall('[\u4e00-\u9fa5]', word))
    return res == word


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 获取列表排序元素
def takeSecond(elem):
    return elem[1]


# 输出矩阵至文件
def print_matrix(file, matrix):
    w = len("{}".format(matrix.max()))
    for m_row in range(matrix.shape[0]):
        file.write("[")
        ww = w
        for m_col in range(matrix.shape[1]):
            if m_col < cut_cols + 5 or matrix[m_row, m_col]:
                file.write(" {:>{width}}".format(matrix[m_row, m_col], width=ww))
            if m_col == cut_cols - 1:
                file.write("]")
                ww = 2
            elif m_col == cut_cols + 4:
                ww = 5
        file.write("\n")


# 求与下行组合熵最大比值
def entropy_ratio(ll, nn):
    res = 0
    if len(cut_pos[nn]) == 3 and len(cut_pos[nn - 1]) == 3 and cut_pos[nn][1] != cut_pos[nn - 1][1]:
        res = cuts_revise[ll - 1, ll] / cuts_revise[ll - 1, ll - 1] / cuts_revise[ll, ll] * text_len
        cuts_revise[ll - 1, cut_cols + 4] = 1
    else:
        for c in range(1, len(cut_pos[nn])):
            p = cut_pos[nn][c] - 1
            if cuts_revise[ll, p] == 1:
                if c == 1:
                    p = cut_pos[nn][c - 1]
                elif c > 1:
                    break
            b = cuts_revise[ll - 1, p] / cuts_revise[ll - 1, ll - 1] / cuts_revise[ll, p] * text_len
            # f1.write("{} {} {} {} {}\n".format(res, cuts[ll-1, cut_pos[nn][c]-1], cuts[ll-1, ll-1], cuts[ll, cut_pos[nn][c]-1], b))
            if b > res:
                res = b
            if res and cut_pos[nn][c] not in cut_pos[nn - 1]:
                break
    return int(res)


# 构建所有文本所有组合频率统计字典
text_len = 0
files_cuts = []  # 所有子句与分割组合
word_cuts = []  # 子句左右长短组合分割
for file_name in files:
    sub_sentence = []
    with open(file_name, 'rb') as f:  # 读取子句
        for ln in f:
            ln = ln.decode("utf-8", "ignore")
            ln = ln[:-1].strip()
            ln = re.sub(r'(?<=[0-9])：(?=[0-9])', ':', ln)
            ln = re.sub(r'(?<=[a-zA-Z]):(?=[0-9])', '：', ln)
            ln = re.sub(r'(?<=[\u4e00-\u9fa5]):(?=[\u4e00-\u9fa5])', '：', ln)
            if len(ln) > 1:
                sub_sentence.append(ln)
                text_len += len(ln)
    for i in range(len(sub_sentence)):  # 行分割
        ln = sub_sentence[i]
        sub_sentence[i] = []
        last_pos = 0
        for j in range(len(ln)):
            if ln[j] in subs[0]:
                if j > 0:
                    sub_sentence[i].append(ln[last_pos:j])
                sub_sentence[i].append(ln[j])
                last_pos = j + 1
        if last_pos < len(ln):
            sub_sentence[i].append(ln[last_pos:])
    sub_cuts = []
    for row in range(len(sub_sentence)):  # 行
        sub_cuts.append([])
        for col in range(len(sub_sentence[row])):  # 子句
            sub_cuts[row].append([])
            sub_line = sub_sentence[row][col]
            for i in range(len(sub_line)):  # 字
                sub_cuts[row][col].append([])
                for j in range(len(sub_line)):  # 组合
                    if j <= i:
                        sub_cuts[row][col][i].append(sub_line[j:i + 1])
                        word_cuts.append(sub_line[j:i + 1])
                    else:
                        sub_cuts[row][col][i].append(sub_line[i:j + 1])
                        word_cuts.append(sub_line[i:j + 1])
    files_cuts.append([sub_sentence, sub_cuts])
cuts_dict = Counter(word_cuts)  # 所有组合频率统计字典
for key in cuts_dict:
    if len(key) > 0:
        cuts_dict[key] = round(cuts_dict[key] / 11157, 4)

# f2 = open(dicts, 'w', encoding='utf-8')
# for k, v in cuts_dict.items():
#     s1 = str(k)  # 把字典的值转换成字符型
#     s2 = str(v)
#     f2.write(s2 + '\t')  # 键和值分行放，键在单数行，值在双数行
#     f2.write(s1 + '\n')
# f2.write('\n')
# f2.close()


for file_name in files:
    # 获得当前文件对应子句与组合
    file_index = files.index(file_name)
    sub_sentence = files_cuts[file_index][0]
    sub_cuts = files_cuts[file_index][1]
    # 结果文件定义
    time_str = file_name[file_name.rfind('\\') + 1:file_name.rfind('.')] + time.strftime("_%Y%m%d_%H%M%S",
                                                                                         time.localtime())
    f = open(time_str + "_Brief.txt", "w", encoding="utf-8")
    f1 = open(time_str + "_Detail.txt", "w", encoding="utf-8")
    f2 = open(time_str + "_segment.txt", "w", encoding="utf-8")

    # 字典分割
    f.write("文件：{}[{}]\n".format(file_name, text_len))
    f.write("--------------------------------------------------------------------------\n")
    f1.write("文件：{}[{}]\n".format(file_name, text_len))
    f1.write("--------------------------------------------------------------------------\n")
    term_dict = {}  # 入选字典
    # for row in range(30):  # 行
    for row in range(len(sub_sentence)):  # 行
        for col in range(len(sub_cuts[row])):  # 子句
            ln_str = sub_sentence[row][col]
            cut_cols = len(ln_str)  # 列数
            if cut_cols < 1:
                continue
            f.write("【第{}行、第{}子句】".format(row, col))
            f1.write("【第{}行、第{}子句】：{}\n".format(row, col, ln_str))
            sub_words = {}

            # 构建原始词频矩阵
            ln_fre = []
            cuts_origin = np.zeros((cut_cols, cut_cols), dtype=float)
            for i in range(cut_cols):  # 字
                ln_fre.append(cuts_dict[ln_str[i]])
                for j in range(len(sub_cuts[row][col][i])):  # 组合
                    if j >= i:
                        cuts_origin[i, j] = cuts_dict[sub_cuts[row][col][i][j]]
            # 构建修正词频矩阵
            cuts_revise = np.zeros((cut_cols, cut_cols + 6), dtype=float)  # 多加6列标识
            for i in range(cut_cols):  # 字
                cuts_revise[i, :cut_cols] = cuts_origin[i, :]
                if ln_str[i] in subs[2]:  # 特殊符号
                    if i < cut_cols - 1:  # 当特殊符号不在句尾
                        for j in range(i):
                            cuts_revise[j, i] = cuts_revise[j, i + 1]  # 将特殊字符的词频修改成特殊字符与后一个字组合词的词频
                    else:
                        for j in range(1, i):
                            cuts_revise[j, i] = cuts_revise[0, i]
                for j in range(i + 1, cut_cols):
                    if i and cuts_revise[i, j] != cuts_revise[i, j + 1]:
                        if cuts_revise[i - 1, j] < cuts_revise[i - 1, i] < cuts_revise[i, j]:
                            for k in range(i):
                                cuts_revise[k, i:j] = cuts_revise[k, j]
                        break
            #
            # 计算词频均值
            ln_avg = np.mean(ln_fre)
            ln_std = np.std(ln_fre)
            ln_fre = ln_avg - ln_std * std_ratio

            # 定义矩阵处理参数
            ln = 0  # 当前行
            cut_line = -1  # 已分割行
            cut_pos = []  # 行分割点

            # 计算行分割点
            for i in range(cut_cols):
                cut_pos.append([])  # 默认分割点为空
                # 比较列
                for j in range(cut_cols):
                    if not j and cuts_revise[i, j] or j and cuts_revise[i, j] != cuts_revise[i, j - 1]:
                        cut_pos[i].append(j)  # 当前行添加分割点
                cut_pos[i].append(cut_cols)  # 补最后一个位置
                # 调整第1组合分割点
                if i != cut_cols - 1 and cuts_revise[i, i] != cuts_revise[i, i + 1]:
                    cut_pos[i].pop(1)
            # new_cut_pos1 = []
            # # 整合分割点
            # for each in cut_pos:
            #     for eachpos in each:
            #         if eachpos not in new_cut_pos1:
            #             l_eachpos = eachpos - 1
            #             r_eachpos = eachpos + 1
            #             if l_eachpos in new_cut_pos1 and r_eachpos in new_cut_pos1:
            #                 each = []
            #             if l_eachpos not in new_cut_pos1 and r_eachpos not in new_cut_pos1:
            #                 new_cut_pos1.append(eachpos)
            #             if l_eachpos in new_cut_pos1 and r_eachpos not in new_cut_pos1:
            #                 new_cut_pos1.append(eachpos)
            #             if l_eachpos not in new_cut_pos1 and r_eachpos in new_cut_pos1:
            #                 new_cut_pos1.append(eachpos)
            #             if int(0) not in new_cut_pos1:
            #                 new_cut_pos1.append(0)
            #             if cut_cols not in new_cut_pos1:
            #                 new_cut_pos1.append(cut_cols)
            # f1.write("删除分割点{}：\n".format(new_cut_pos1))
            # 行处理
            not_chinese = []  # 连续非汉字起止点
            cuts_result = np.zeros((cut_cols, cut_cols + 6), dtype=int)  # 多加6列标识
            for i in range(cut_cols):
                cuts_revise[i, cut_cols + 1] = i
                # 判断当前是否汉字、修改连续非汉字起止点
                if len(not_chinese) and (is_Chinese(ln_str[i]) or ln_str[i] in subs[2]):
                    not_chinese = []

                # 计算左右商比值
                # if cut_cols > 2 and i < cut_cols - 1:
                #     rt = [i, 0, 0]  # 行号、与上行左右熵比、与下行左右熵比
                #     if i < cut_cols - 2:
                #         rt[2] = cuts_revise[i, i + 1] / cuts_revise[i, i] / (
                #                 cuts_revise[i + 1, i + 2] / cuts_revise[i + 2, i + 2])
                #     if i:
                #         rt[1] = cuts_revise[i, i + 1] / cuts_revise[i + 1, i + 1] / (
                #                 cuts_revise[i - 1, i] / cuts_revise[i - 1, i - 1])
                #     if rt[1] > 1:
                #         cuts_revise[i, cut_cols + 2] = 1
                #     elif 0 < rt[1] < 1:
                #         cuts_revise[i, cut_cols + 2] = -1
                #     if rt[2] > 1:
                #         cuts_revise[i, cut_cols + 3] = 1
                #     elif 0 < rt[2] < 1:
                #         cuts_revise[i, cut_cols + 3] = -1

                # 基于行判断组合
                if i == cut_cols - 1 or cuts_revise[i, i + 1] == 1 and is_Chinese(ln_str[i]) or ln_str[i] in subs[2]:
                    # 组合频率为1、或最后一行、或当汉字字符，无组合
                    cuts_revise[i, cut_cols] = 19
                elif not is_Chinese(ln_str[i]) and ln_str[i - 1] not in subs[2] and ln_str[i] not in subs[2] and not \
                        cuts_revise[i, cut_cols]:
                    # 非汉字，记录起止点
                    if len(not_chinese) <= 1:  # 增加起止点
                        not_chinese.append(i)
                    elif len(not_chinese) == 2:  # 已有起止点，只修改终点
                        not_chinese[1] = i
                    # 对之前行的连续非汉字词频进行处理
                    if len(not_chinese) == 2:
                        for j in range(ln + 1):
                            if not cuts_revise[j, cut_cols]:
                                for k in range(not_chinese[0] + 1, not_chinese[1] + 2):
                                    if k in cut_pos[j]:
                                        cut_pos[j].remove(k)
                        cuts_revise[i, cut_cols] = 12
                elif i < cut_cols - 1 and ln_str[i + 1] in subs[1] and not_chinese == []:
                    cuts_revise[i + 1, cut_cols] = 13  # 连接符
                    if i + 2 in cut_pos[ln]:
                        cut_pos[ln].remove(i + 2)
                elif i and cuts_revise[i, cut_pos[ln][1] - 1] == cuts_revise[i - 1, cut_pos[ln][1] - 1] and cuts_revise[
                    i - 1, cut_cols] != 19:
                    cuts_revise[i, cut_cols] = 11  # 第1组合结尾与上一行同频
                # elif i and (is_Chinese(ln_str[i-1]) or ln_str[i-1] in subs[1]):
                #     if cuts_revise[i, cut_cols + 2] == -1 and cuts_revise[i, cut_cols + 3] == -1 and cuts_revise[i, i + 1] < max(cuts_revise[i - 1, i], cuts_revise[i + 1, i + 2]):
                #         cuts_revise[i, cut_cols] = 14      # 左右熵上下最小、词频上下非最大
                #     elif (cuts_revise[i, cut_cols + 2] == -1 or cuts_revise[i, cut_cols + 3] == -1) and cuts_revise[i, i + 1] < min(cuts_revise[i - 1, i], cuts_revise[i + 1, i + 2]):
                #         cuts_revise[i, cut_cols] = 15      # 左右熵非最小、词频上下最小
                #     elif cuts_revise[i, i + 1] < cuts_revise[i - 1, i] and cuts_revise[i, cut_cols + 2] == -1:
                #         cuts_revise[i, cut_cols] = 18      # 熵、词频小于上行
                #     elif not cuts_revise[i - 1, cut_cols]:
                #         if not cuts_revise[i - 1, cut_cols + 5]:
                #             cuts_revise[i - 1, cut_cols + 5] = entropy_ratio(i, ln)
                #             cuts_result[ln - 1, cut_cols + 5] = cuts_revise[i - 1, cut_cols + 5]
                #         cuts_revise[i, cut_cols + 5] = entropy_ratio(i + 1, ln + 1)
                #         if min(cuts_revise[i - 1, cut_cols + 2:cut_cols + 4]) == 1 or min(cuts_revise[i, cut_cols + 2:cut_cols + 4]) == 1:
                #             if cuts_revise[i - 1, i] <= cuts_revise[i, i + 1] and cuts_revise[i - 1, cut_cols + 5] < cuts_revise[i, cut_cols + 5] and is_Chinese(ln_str[i - 2]):
                #                 cuts_revise[i - 1, cut_cols] = 16
                #                 cuts_revise[i, cut_cols] = 6
                #                 cut_pos.pop(ln-1)
                #                 ln -= 1
                #             elif cuts_revise[i - 1, i] > cuts_revise[i, i + 1] and cuts_revise[i - 1, cut_cols + 5] > cuts_revise[i, cut_cols + 5]:
                #                 cuts_revise[i - 1, cut_cols] = 6
                #                 cuts_revise[i, cut_cols] = 16
                #         else:
                #             if cuts_revise[i - 1, cut_cols + 5] < cuts_revise[i, cut_cols + 5]:
                #                 cuts_revise[i - 1, cut_cols] = 17
                #                 if not cuts_revise[i - 1, cut_cols + 4]:
                #                     cuts_revise[i, cut_cols] = 7
                #                 cut_pos.pop(ln-1)
                #                 ln -= 1
                #             elif cuts_revise[i - 1, cut_cols + 5] > cuts_revise[i, cut_cols + 5]:
                #                 cuts_revise[i, cut_cols] = 17
                #                 if not cuts_revise[i - 1, cut_cols + 4]:
                #                     cuts_revise[i - 1, cut_cols] = 7

                # 单独非汉字处理
                if not cuts_revise[i, cut_cols] and 0 < i < cut_cols - 1 and not is_Chinese(ln_str[i]) and ln_str[
                    i] not in subs[2] and \
                        is_Chinese(ln_str[i + 1]) and ln_str[i + 1] not in subs[2] and cuts_revise[i, i + 1] == \
                        cuts_revise[i, cut_cols - 1]:
                    cuts_revise[i, cut_cols] = 14

                # 处理头尾高频字
                if i and cuts_revise[i - 1, i - 1] > ln_fre and cuts_revise[
                    i - 1, cut_cols] == 16 and i + 1 < cut_cols and cuts_revise[i - 1, i + 1] > 1 and ln_str[
                    i - 1] not in subs[3]:
                    subs[3].append(ln_str[i - 1])
                    f1.write("添加高频字：{}\n".format(ln_str[i - 1]))
                if cuts_revise[i, i] > ln_fre and cuts_revise[i, cut_cols] == 16 and i + 2 < cut_cols and cuts_revise[
                    i, i + 2] > 1 and ln_str[i] not in subs[3]:
                    subs[3].append(ln_str[i])
                    f1.write("添加高频字：{}\n".format(ln_str[i]))

                # 行删除
                if cuts_revise[i, cut_cols] > 10:
                    # 删除无意义行
                    cut_pos.pop(ln)
                    continue
                else:
                    # 添加组合行
                    cuts_result[ln] = cuts_revise[i]
                    ln += 1

            f1.write("原始矩阵：\n")
            print_matrix(f1, cuts_origin)
            f.write("修正矩阵行判断：{:.2f} {:.2f} {:.2f}\n{}\n".format(ln_fre, ln_avg, ln_std, cuts_revise))
            f1.write("修正矩阵行判断：{:.2f} {:.2f} {:.2f}\n".format(ln_fre, ln_avg, ln_std))
            print_matrix(f1, cuts_revise)
            if not ln:
                cuts_result[0] = cuts_revise[0]
                cut_pos.append([0, cut_cols])
                ln += 1
            for j in range(ln, cut_cols):
                cuts_result = np.delete(cuts_result, ln, axis=0)

            corpos = sub_sentence[row][col]
            new_cut_pos = []
            seg_words = []
            # 整合分割点
            for each in cut_pos:
                for eachpos in each:
                    if eachpos not in new_cut_pos:
                        l_eachpos = eachpos - 1
                        r_eachpos = eachpos + 1
                        if l_eachpos in new_cut_pos and r_eachpos in new_cut_pos:
                            each = []
                        if l_eachpos not in new_cut_pos and r_eachpos not in new_cut_pos:
                            new_cut_pos.append(eachpos)
                        if l_eachpos in new_cut_pos and r_eachpos not in new_cut_pos:
                            new_cut_pos.append(eachpos)
                        if l_eachpos not in new_cut_pos and r_eachpos in new_cut_pos:
                            new_cut_pos.append(eachpos)
                        if int(0) not in new_cut_pos:
                            new_cut_pos.append(0)
                        if len(corpos) not in new_cut_pos:
                            new_cut_pos.append(len(corpos))

            # 处理英文字符
            for i in re.finditer(u'[^\u4e00-\u9fa5]{2,}', corpos):
                start = i.start()
                end = i.end()
                # print((start, end))
                if start not in new_cut_pos:
                    new_cut_pos.append(start)
                if end not in new_cut_pos:
                    new_cut_pos.append(end)
                for each in new_cut_pos[:]:
                    if start < each < end:
                        new_cut_pos.remove(each)
                    # print(each)

            new_cut_pos = sorted(list(new_cut_pos), reverse=False)
            # print(new_cut_pos)
            for i in range(len(new_cut_pos)):
                if i < len(new_cut_pos) - 1:
                    seg_words.append(corpos[new_cut_pos[i]:new_cut_pos[i + 1]])
            # print(seg_words)

            f.write("修正矩阵行处理：\n{}\n".format(cuts_result))
            f1.write("修正矩阵行处理：\n")
            print_matrix(f1, cuts_result)
            f1.write("分割点{}：\n".format(new_cut_pos))

            # # 提取组合信息
            # cut_len = cuts.shape[1]
            # len_words = []
            # for i in range(len(cut_pos)):
            #     if len(cut_pos[i]) == 2:
            #         if cuts[i, cut_pos[i][0]] > cut_min or not i:
            #             word_str = sub_sentence[row][col][cut_pos[i][0]:]
            #             sub_words[word_str] = cuts[i, cut_pos[i][0]]
            #             if word_str not in len_words:
            #                 len_words.append(word_str)
            #     else:
            #         for j in range(len(cut_pos[i])-1):
            #             if cuts[i, cut_pos[i][j]] > cut_min*(cut_lowest if i and j and cut_min <= cut_lowest else 1):
            #                 if cut_pos[i][j+1] < cut_len:
            #                     word_str = sub_sentence[row][col][cut_pos[i][0]:cut_pos[i][j+1]]
            #                     sub_words[word_str] = cuts[i, cut_pos[i][j]]
            #                     if word_str not in len_words:
            #                         len_words.append(word_str)
            #                 else:
            #                     word_str = sub_sentence[row][col][cut_pos[i][0]:]
            #                     sub_words[word_str] = cuts[i, cut_pos[i][j]]
            #                     if word_str not in len_words:
            #                         len_words.append(word_str)

            f.write("{}\n分词：{}\n".format(sub_sentence[row][col], seg_words))
            f1.write("子句：{}\n分词：{}\n".format(sub_sentence[row][col], seg_words))
            for each in seg_words:
                if each not in subs[0] and each not in subs[1]:
                    f2.write(each + "\n")
            # # 组合分割
            # for sub_word in sub_words:
            #     if term_dict.get(sub_word) is None:
            #         term_dict[sub_word] = sub_words[sub_word]

    # 结果排序输出
    f.write("--------------------------------------------------------------------------\n")
    f1.write("--------------------------------------------------------------------------\n")
    f.write("\n头尾高频字：{}\n".format(subs[3]))
    f1.write("\n头尾高频字：{}\n".format(subs[3]))
    f.write("\n提取结果：\n")
    f1.write("\n提取结果：\n")
    word_list = []
    for key in term_dict:
        word_list.append([key, term_dict[key]])
    word_list.sort(key=takeSecond, reverse=True)
    subs[2].extend(subs[1])
    subs[3].extend(subs[1])
    for key in word_list:
        if key[1] > 1 and not key[0].isdigit() and key[0][0] not in subs[2] and key[0][-1] not in subs[3]:
            f.write("{}:{}\n".format(key[0], key[1]))
            f1.write("{}:{}\n".format(key[0], key[1]))

    f.close()
    f1.close()
    f2.close()
