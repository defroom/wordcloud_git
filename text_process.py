# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     text_process
   Description :
   Author :       def
   date：          2018/10/17
-------------------------------------------------
   Change Activity:
                   2018/10/17:
-------------------------------------------------
"""
import jieba
# 读取停用词表
stopwords = []
with open("utlis/stopwords.txt","r",encoding="utf8") as f_stopwords:
    for word in f_stopwords:
        stopwords.append(word.replace("\n", ""))
#文本清洗
f_write_file = open("date_processed.txt", "w", encoding="utf8")
word_list = []
with open("data.txt", encoding="utf-8") as f_date:
    for line in f_date:
        words = jieba.cut(line.replace("\t", "").replace("\n", "").replace(" ", ""))
        for word in words:
            if word not in stopwords and len(word) > 1:
                word_list.append(word)
f_write_file.write(" ".join(word_list))
f_write_file.flush()
f_write_file.close()
