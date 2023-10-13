# Örnek 1 : İris Dataset çiçek taç ve çanak yaprak özelliklerinden çiçek türü sınıflandırma
# Örnek 2 : Boy,Kilo,Yaş verilerinden Cinsiyet Sınıflandırması

<hr>

# Örnek 1 İçin Bilgiler

Bağımsız Değişkenlerimiz
iris.feature_names
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']

Bağımlı Değişkenlerimiz
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

7. <hr>

# Örnek 2 için Bilgiler
veriler.csv dosyası verileri içermektedir. Bu veriler ile modelin eğitimi ve testi yapılacaktır.

# Kodun Açıklanması
1. veri yüklenir.
2. Veri seti ülke, boy, kilo, yaş verileri içerir fakat biz bu örnekte boy,kilo,yaş kullanacağımız için iloc komutu kullanarak sadece bu sütunlardan bağımsız değişkenler oluşturulur.
3. Bağımlı değişkenler cinsiyet verileridir. 
4. Veriler öğrenme ve test olarak bölünür.
5. K-NN modeli uygulanır.
6. Öğrenme gerçekleştirilir.
7. Tahmin elde edilir.
8. Confusion Matrix oluşturulur. 

