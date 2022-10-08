# import wikipedia
# import wordcloud
# import matplotlib.pyplot as plt
#
# kbo = wikipedia.page("KBO League")
# txt_kbo = kbo.content
# print(txt_kbo)
# image = wordcloud.WordCloud(width = 1000, height = 700).generate(txt_kbo)
# plt.figure(figsize = (40, 30))
# plt.imshow(image)
# plt.show()

import string

s1 = string.ascii_uppercase
s2 = s1[3:]+s1[:3]
print(s2)

s = input("문장을 입력하시오")
for s3 in range(s):
    num =s1.index(s3)
    print(s2[num])
