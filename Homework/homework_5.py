# -*- coding: utf-8 -*-
"""Homework-5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rBJFIXEhDArkaCmJVmaXYs8Alm2N7CdT

https://github.com/lsjsj92/keras_basic/blob/master/7.%20predict_multi_img_with_CNN.ipynb

https://lsjsj92.tistory.com/355

1. 라벨링 # 함
2. 파일 열기 #함
3. 픽셀값으로 변경 # 함
4. train, validation 비율 자유 #
5. 컨벌루젼 최대 4개, dense 최대 2개 # 이거 모르겠음
6. max pooling, dropout 필수 # 함
7. 손실함수 : categorical_crossentropy # 함
8. early_stopping # 함
9. test 데이터 사용해서 예측값과 실제값 비교 시각화 # 해야함
sklearn - confusion_matrix
seaborn -  heatmap


옵션

성능 향상을 위해, data augmentation 기법 적용 가능
예: rotation [1], jigsaw puzzle [2], colorization [3], and inpainting [4]
"""

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import numpy as np
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from keras.models import load_model

from PIL import Image
import os, glob, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score


from google.colab import drive

"""라벨링, 파일 불러오기기, 픽셀값 변경경"""

drive.mount('/content/drive')
caltech_dir = './drive/MyDrive/Colab Notebooks/data/train'

categories = ["adidas", "converse", "nike"]

#caltech_dir = "./multi_img_data/imgs_others/train"

nb_classes = len(categories)

image_w = 240
image_h = 240

pixels = image_h * image_w * 3

X = []
y = []

for idx, cat in enumerate(categories):
    
    #one-hot 돌리기.
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg")
    print(cat, " 파일 길이 : ", len(files))




    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X.append(data)
        y.append(label)

        if i % 700 == 0:
            print(cat, " : ", f)

X = np.array(X) #데이터 쌓기
y = np.array(y) # 라벨링 쌓기


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = True)
print("ok", len(y))

##########################################

drive.mount('/content/drive')
caltech_dir = './drive/MyDrive/Colab Notebooks/data/test'

categories = ["adidas", "converse", "nike"]

#caltech_dir = "./multi_img_data/imgs_others/train"

nb_classes = len(categories)

image_w = 240
image_h = 240

pixels = image_h * image_w * 3

X1 = []
y1 = []

for idx, cat in enumerate(categories):
    
    #one-hot 돌리기.
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg")
    print(cat, " 파일 길이 : ", len(files))




    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X1.append(data)
        y1.append(label)

        if i % 700 == 0:
            print(cat, " : ", f)


X_test2 = np.array(X1)
y_test2 = np.array(y1)


# xy = (X_train, X_test, y_train, y_test)
# np.save("./drive/MyDrive/Colab Notebooks/data/multi_image_data.npy", xy)

print("ok", len(y_test2))

# X_train, X_test, y_train, y_test = np.load('./drive/MyDrive/Colab Notebooks/data/multi_image_data.npy')
#print(X_train)
#print(X_train.shape[0])


# plt.imshow(files[1])

# print(X_test2)

categories = ["adidas", "converse", "nike"]
nb_classes = len(categories)

#일반화
X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255

X_test2 = X_test2.astype(float) / 255

# print(X_test2)

model = Sequential()
model.add(Conv2D(16, (3,3), padding="same", input_shape=X_train.shape[1:], activation='relu')) # 커널의 개수 32개, 커널의 크기 3*3, 입력의 크기 : 행, 열, 흑백 
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
    
model.add(Conv2D(32, (3,3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3,3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
    
model.add(Flatten()) # 1차원 백터로 변경경
model.add(Dense(512, activation='relu')) # dense 1
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax')) # dense 2

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) # 손실함수 : categorical_crossentropy, 옵티마이저 : 아담, 메트릭스 

model_dir = './drive/MyDrive/Colab Notebooks/data'

model_path = model_dir + '/multi_img_classification.model'
checkpoint = ModelCheckpoint(filepath=model_path , monitor='val_loss', verbose=0, save_best_only=True)




early_stopping = EarlyStopping(monitor='val_loss', patience=10) # 얼리 스타핑핑

model.summary() #썸머리 

history = model.fit(X_train, y_train, batch_size=10, epochs=50, validation_split= 0.25, callbacks=[checkpoint, early_stopping])

# validation_data=(X_test, y_test)

# score = model.evaluate(X_test2,y_test2)
# print(score)

# print("정확도 : %.4f" % (model.evaluate(X_test, y_test)[1]))

real_prices = []
pred_prices = []
X_num = []
n_iter=0

filenames = []

Y_prediction = model.predict(X_test2)

# print(Y_prediction) 


for i in range(len(X_test2)):
  real = y_test[i]
  prediction = Y_prediction[i]
  # print('Real price : {}, Expected price : {}'.format(real,prediction))
  real_prices.append(real)
  pred_prices.append(prediction)
  n_iter = n_iter +1
  X_num.append(n_iter)

# print(type(real_prices))
# print(type(pred_prices))

# print(real_prices)
# print(pred_prices)


# confusion_matrix(real_prices, pred_prices)

# print(pred_prices)

pred = []

for i in pred_prices:
  if(i.argmax()== 0):
    pred.append(0)
  elif(i.argmax()== 1):
    pred.append(1)
  elif(i.argmax()== 2):
    pred.append(2)

Y_test = []

for i in y_test2:
  if(i.argmax()== 0):
    Y_test.append(0)
  elif(i.argmax()== 1):
    Y_test.append(1)
  elif(i.argmax()== 2):
    Y_test.append(2)

test = confusion_matrix(Y_test, pred)

plt.figure(figsize = (3, 3))
plt.ylabel('True')
plt.xlabel('Predict')
sns.heatmap(test, linewidth = 30, vmax = 30, cmap = 'Reds', annot = True)


plt.show()