

#2.1.veri yukleme
import pandas as pd
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)


#verilerin tanımlanması
x = veriler.iloc[:,1:4].values #bağımsız değişkenler boy,kilo,yaş
y = veriler.iloc[:,4:].values #bağımlı değişkenler cinsiyet
print(x)
print(y)



#verinin ikiye bölünmesi (%67 öğrenme %33 test)
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0) # %33ü test için ayrılacak




#modelin uygulanması
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')

#öğrenme
knn.fit(x_train,y_train)

#tahmin
y_pred = knn.predict(x_test)


#confusion matrix ile accuracy değerinin belirlenmesi 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)






























