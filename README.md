# Örnek 1 : İris Dataset ile sınıflandırma örneği
# Örnek 2 : Boy,Kilo,Yaş verilerinden Cinsiyet Sınıflandırması Örneği

<hr>
# Bağımsız Değişkenlerimiz
iris.feature_names
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']

 # Bağımlı Değişkenlerimiz
 iris.target_names
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

Çiçeğimizin 4 bağımsız özelliği ve bunlara bağlı alabileceği 3 bağımlı tür özelliği vardır.

# Kodun Açıklanması 
1. Aşama olarak iris dataset kütüphaneden hazır olarak getirilir.
2. Aşama olarak veri öğrenme ve test şeklinde ikiye bölünür. Varsayılan %75 öğrenme , %25 testtir.
3. Aşama olarak uygun algoritma seçilir . burada sınıflandırma ile bir tür seçimi yapılacağından KNeighborsClassifier algoritması seçildi.
4. Aşama olarak model öğrenme aşamasından geçirilir.
5. Aşama olarak bir veri üzerinde tahmin yaptırılır.
6. Aşama olarak tahmin verileri test için verilen değerlerle karşılaştırılarak modelin doğruluk yüzdesi hesaplanır. 
