# 一、目的：
**就是想为my girl做一个定制的二维码，里面是我们的内容**
---
# 二、原理：
## 1.生成一个日期动图
dynamic_bar_chart.py是生成一个动图gif，里面是我们一些关键日子距离今天的天数。数据是从data.xlsx中读取的，然后保存在同目录下一个process.gif和一张结束图process_stop.png
## 2.创建一个html页面
html_generate.html是用来创造一个html页面的，里面我加了背景图片html_background1.jpg，一张图片loving_heart.jpg，刚才生成的gif和一些字
## 3.让这个html页面成为一个人人可以访问的链接
传到腾讯云上，然后开启静态网站，将索引文档设置为html.generate.html就可了，访问节点就是我们之前生成的网页链接
## 4.生成一个二维码
QR_code_generate.py是用来生成一个QR_code的，将定制的img.png生成了一个QR_code.png二维码图片保存在同目录，这里面的关联链接就是刚才生成的。
## 5.然后生成这个二维码的链接
其实现在以及大功告成了，但是完美一下，就是给这个QR_code也一个链接，将其所有文件上传到GitHub上之后，settings里github pages里的source设置master branch就可以了，就生成了一个QR_code图片的专属链接http://tx-leo.github.io/QR_code/QR_code.png
（虽然有点多此一举hhh）
---
# 三、参考文献：
https://blog.csdn.net/zohan134/article/details/107170581