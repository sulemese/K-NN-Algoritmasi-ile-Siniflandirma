# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#iris datasetin sklearn kütüphanesinden hazır olarak getirilmesi
from sklearn.datasets import load_iris
iris_dataset=load_iris()   
print(iris_dataset) 


#verinin ikiye bölünmesi (öğrenme ve test)
from sklearn.model_selection import  train_test_split
x_ogren, x_test, y_ogren, y_test = train_test_split(iris_dataset['data'], iris_dataset['target']) #burada x:çiçek  y:tür verileri
print(x_ogren.shape) #shape boyutu döndürür 
print(x_test.shape)


#uygun modeli seçme
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)

#öğrenme
knn.fit(x_ogren,y_ogren)

#tahmin
x_yeni=[[3.5,2.1,3.4,1.2]]
tahmin=knn.predict(x_yeni)
print(tahmin) #tahmin 1 ise bu çiçek versicolor türünde diyor. peki bu ne kadar doğru?

#doğruluk & test verisi 
dogruluk=knn.predict(x_test)
print(dogruluk)
import numpy as np
print(np.mean(dogruluk == y_test)*100) #burada doğruluk ve y_test verileri karşılaştırılır. ortalama ne kadar birbirine yakın oldukları bulunur