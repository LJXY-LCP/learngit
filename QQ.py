import wordcloud
import jieba
from scipy.misc import imread
mask=imread("F:\\python\\1.jpg")
f=open("F:\\python\\QQ.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc",mask=mask
                      ,background_color="white",max_words=20)
w.generate(txt)
w.to_file("F:\\python\\pywordcloud.png")
