# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     makewordcloud
   Description :
   Author :       def
   date：          2018/10/18
-------------------------------------------------
   Change Activity:
                   2018/10/18:
-------------------------------------------------
"""
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

word_text = ""
with open("date_processed.txt","r",encoding="utf8") as f_data:
    word_text = f_data.read()
cloud_mask = np.array(Image.open("img/snake.jpg"))
wc = WordCloud(
    background_color="white",
    max_words=500,
    font_path="utlis/msjh.TTF",
    min_font_size=15,
    max_font_size=50,
    width=800,
    height=600,
    mask=cloud_mask
)

wc.generate(word_text)
wc.to_file("wordcloud.png")
img = Image.open("wordcloud.png")
plt.figure("词云制作")
plt.imshow(img)
plt.axis("on")
plt.title("wordcloud")
plt.show()
