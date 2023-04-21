import os
import pickle
import random
import sys

import numpy as np

## tags, BIO
tag2label = {"O": 0,
             "B": 1, "I": 2
             }


def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()
    sent_, tag_ = [], []
    for line in lines:
        if line != '\n':
            # print(line)
            [char, label] = line.strip().split()
            sent_.append(char)
            tag_.append(label)
        else:
            data.append((sent_, tag_))
            sent_, tag_ = [], []

    return data


def vocab_build(vocab_path, corpus_path, min_count):
    """

    :param vocab_path:
    :param corpus_path:
    :param min_count:
    :return:
    """
    data = read_corpus(corpus_path)
    word2id = {}
    for sent_, tag_ in data:
        for word in sent_:
            if word.isdigit():
                word = '<NUM>'
            elif ('\u0041' <= word <= '\u005a') or ('\u0061' <= word <= '\u007a'):
                word = '<ENG>'
            if word not in word2id:
                word2id[word] = [len(word2id) + 1, 1]
            else:
                word2id[word][1] += 1
    low_freq_words = []
    for word, [word_id, word_freq] in word2id.items():
        if word_freq < min_count and word != '<NUM>' and word != '<ENG>':
            low_freq_words.append(word)
    for word in low_freq_words:
        del word2id[word]

    new_id = 1
    for word in word2id.keys():
        word2id[word] = new_id
        new_id += 1
    word2id['<UNK>'] = new_id
    word2id['<PAD>'] = 0

    # print(len(word2id))
    with open(vocab_path, 'wb') as fw:
        pickle.dump(word2id, fw)


if __name__ == '__main__':
    vocab_path = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\word2id_h.pkl'
    corpus_path = r'C:\Users\11921\PycharmProjects\ZYcode\ZYpaper\zh-NER-TF-master\data_path\trainresult_bio_h.txt'
    min_count = 1
    vocab_build(vocab_path, corpus_path, min_count)
    data = read_corpus(corpus_path)
