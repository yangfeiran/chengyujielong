#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hanzi2pinyin
import random
import sys
from pypinyin import pinyin,Style

data = []

def get_pinyin(word):
    pin_yin = []
    for i in word:
        pin_yin.append(hanzi2pinyin.hanzi2pinyin(i))
    return pin_yin

def get_all_starts_with(letter):
    result = []
    target_pinyin = pinyin(letter, heteronym=False,style=Style.TONE3)
    print target_pinyin
    try:
        target_pinyin_last = target_pinyin[-1]
    except IndexError,e:
        print("input is empty!")
        return None
    for i in data:
        data_word = i[0]
        data_pinyin = i[1]
        data_meaning = i[2]
        data_pinyin_first = data_pinyin[0]
        if data_pinyin_first == target_pinyin_last and data_word != letter:
            result.append([data_word, data_pinyin, data_meaning])
    return result


def get_random_result(data):
    if data:
        return random.choice(data)
    else:
        return None

def format_data(data):
    if data:
        return "[%s] (%s): [%s]" % (data[0], data[1] , data[2])

    else:
        return 'none match!'

def init():
    with open("/Users/feiran/Desktop/data.txt", "r") as f:
        counter = 0
        for line in f:
            content = line.decode("UTF-8").split("\t")
            word = content[0]
            pin_yin = pinyin(content[0], heteronym=False,style=Style.TONE3)
            meaning = content[2].replace("\n", "")
            data.append([word, pin_yin, meaning])
            counter += 1
        print "[+] Init finished! [%d] words." % (counter)

def guess(word):
    all_data_matched = get_all_starts_with(word)
    result_data = format_data(get_random_result(all_data_matched))
    return result_data

def main():
    init()
    while(True):
        word = raw_input("Input your word: ").decode("UTF-8")
        all_data_matched = get_all_starts_with(word)
        result_data = format_data(get_random_result(all_data_matched))
        print result_data


if __name__ == "__main__":
    main()
