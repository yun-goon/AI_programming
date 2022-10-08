import wikipedia
import wordcloud
import matplotlib.pyplot as plt

kbo = wikipedia.page("KBO League")
txt_kbo = kbo.content

print(txt_kbo)
print(type(txt_kbo))
image = wordcloud.WordCloud(width = 1000, height = 800).generate(txt_kbo)


plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()
