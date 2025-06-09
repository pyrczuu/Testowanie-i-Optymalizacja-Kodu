# Klasyfikacja obrazów raka mózgu
**Cel**: Uzyskanie najwyższej dokładności klasyfikacji stosując różne techniki optymalizacji modelu.
**Zbiór danych**: 2004 skany MRI glejaka oraz 2004 skany MRI oponiaka, oryginalny zbiór został pozbawiony niezidentyfikowanej klasy 'tumor'. Zbiór został pobrany z [Kaggle](https://www.kaggle.com/datasets/orvile/brain-cancer-mri-dataset).
**Parametry**:
Oto standardowe parametry, których wartości były optymalizowane podczas badań. 
- Aktywacja: softmax
- Seria: 32
- Epoki: 10
- Wymiary zdjęć: 128x128
 
**Przetestowane modele**: ResNet50, VGG16, ResNet101, Inception, MobileNet
Każdy z powyższych modeli został przetestowany zarówno z użyciem uczenia transferowego jak i bez. 

## Optymalizacja szybkości

### 1. CPU vs GPU
Jako pierwszy zbadany został czas pracy modelu. Porównywano te same modele, jeden z nich pracował na jednostce CPU, drugi korzystał z T4 GPU. Zostały one zapewnione przez Google Colab. 
**Czas pracy**:
- CPU = 1 godzina 42 minuty
- GPU = 5 minut

Z powodu drastycznej różnicy w czasie pracy, do końca badania wykorzystywana była jednostka T4 GPU. 

### 2.  Transfer learning
W celu zoptymalizowania czasu pracy oraz dokładności w modelu ResNet50 zastosowane zostało uczenie transferowe. Zabieg ten pozwolił skrócić czas działania o 20% oraz znacznie poprawić dokładność modelu.
Wyniki bez uczenia transferowego:
![image](https://github.com/user-attachments/assets/ba6cfc7c-4981-4881-97e8-be340523a4c3)

Wyniki z uczeniem transferowym:

![image](https://github.com/user-attachments/assets/440614bb-1f87-408b-bd35-4d901720a7d7)

## Dalsza optymalizacja dokładności
### 1. Normalizacja danych
W tym celu skala pikseli została zmieniona z 0-255 na 0-1. Oto porównanie wyników działania modelu z zastosowaniem normalizacji oraz bez niej. 

![image](https://github.com/user-attachments/assets/745785fc-3f9d-4ce7-96f1-058e514e243f)

![image](https://github.com/user-attachments/assets/763c83b0-dd30-40a9-a626-d82eae95859e)

Z niezrozumiałego mi powodu po normalizacji danych model zaczął ignorować jedną z klas. 
### 2. Augmentacja danych
W tym kroku różnorodność danych została sztucznie zwiększona poprzez operacje na obrazach.

```python
data_augmentation = keras.Sequential([
    layers.Rescaling(1./255),
    layers.RandomRotation(0.083),
    layers.RandomTranslation(0.15, 0.15),
    layers.RandomZoom(0.15),
    layers.RandomFlip("horizontal"),
    layers.RandomContrast(0.1),
])
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y),
                        num_parallel_calls=AUTOTUNE)

val_ds = val_ds.map(lambda x, y: (layers.Rescaling(1./255)(x), y),
                    num_parallel_calls=AUTOTUNE)
```
Ten zabieg znacznie poprawił wyniki co można zobaczyć poniżej. 

![image](https://github.com/user-attachments/assets/fa1edf3f-9e0f-4542-83d8-6aa490527604)

![image](https://github.com/user-attachments/assets/73fd86ac-2edc-47bd-863d-c16366f30959)

### 3. Dropout
Na modelu ResNet50 (bez uczenia transferowego) został zastosowany dropout wysokości 0.5. 

![image](https://github.com/user-attachments/assets/3a1b2ccc-87c6-49d4-96c1-9cd1f5626efb)

![image](https://github.com/user-attachments/assets/97a6dc43-ed65-4a61-ae01-15bfeeeee272)

### 4. Rozmiar obrazu 
Przetestowano różne rozmiary danych wejściowych na modelu ResNet50: 96x96, 128x128, 160x160, 224x224. Warto zaznaczyć, iż w dalszej części niektóre operacje wymagały użycia innych niestandardowych rozmiarów.

![image](https://github.com/user-attachments/assets/fd4dc4a4-9b32-45c5-b58b-093e56ef1d74)

Rozmiar 96x96 uzyskał najlepsze wyniki w tym zestawieniu. 

### 5. Rozmiar serii
Porównano następujące rozmiary serii: 32, 64, 128.

Rozmiar 32:

![image](https://github.com/user-attachments/assets/0c3a7719-93aa-45c7-8b8c-b6c51fa49ee6)

Rozmiar 64:

![image](https://github.com/user-attachments/assets/d89bbc66-9e45-42df-9e91-9a1ada8715ae)

Rozmiar 128:

![image](https://github.com/user-attachments/assets/cb62e687-8e04-400f-8da2-7a1c7ae734cc)

W tym zestawieniu z minimalną przewagą wygrywa rozmiar 128 z accuracy na poziomie 0.67.

### 6. Różne modele
Na koniec porównano następujące modele: ResNet50, VGG16, ResNet101, InceptionV3 oraz MobileNet. Każdy z tych modelu został przetestowany zarówno z uczeniem transferowym jak i bez. Niektóre z modeli wymagały unikalnych rozmiarów obrazów. 

VGG16:

![image](https://github.com/user-attachments/assets/e76fe817-c49c-499a-a6cc-52e158f544a3)

Jak widać w obu modelach nie zastosowanie uczenia transferowego spowodowało faworyzację jednej z klas. W tym zestawieniu z dokładnością na poziomie 0.90 wygrywa VGG16 z uczeniem transferowym.

ResNet101:

![image](https://github.com/user-attachments/assets/e2fe1402-1da6-49b1-82cf-8ebaab9b5deb)

Najwyższą dokładność osiąga ResNet101 z uczeniem transferowym. Wynosi ona 0.92.

InceptionV3:

![image](https://github.com/user-attachments/assets/149d6ec0-57d6-4c42-b0fd-75edaac83c80)

Ten model bardzo słabo poradził sobie z zadaniem. Najlepiej w tym zestawieniu wypadł ResNet50 z uczeniem transferowym.

MobileNet:

![image](https://github.com/user-attachments/assets/d06fe190-3ca2-44a7-8bd6-cf45b97a74be)

ResNet50:

| Class         | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| brain_glioma  | 0.61      | 0.96   | 0.74     | 414     |
| brain_menin   | 0.88      | 0.34   | 0.49     | 387     |
| **Accuracy**  |           |        | **0.66** | 801     |


Resnet50 + uczenie transferowe:

| Class         | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| brain_glioma  | 0.85      | 0.91   | 0.88     | 414     |
| brain_menin   | 0.90      | 0.83   | 0.86     | 387     |
| **Accuracy**  |           |        | **0.87** | 801     |

MobileNet:

| Class         | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| brain_glioma  | 0.99      | 0.76   | 0.86     | 414     |
| brain_menin   | 0.80      | 0.99   | 0.88     | 387     |
| **Accuracy**  |           |        | **0.87** | 801     |

MobileNet + uczenie transferowe:

| Class         | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| brain_glioma  | 1.00      | 1.00   | 1.00     | 414     |
| brain_menin   | 1.00      | 1.00   | 1.00     | 387     |
| **Accuracy**  |           |        | **1.00** | 801     |

## Konkluzja
Po zbadaniu różnych wersji modelu klasyfikacji obrazów, można dojść do wniosku, iż model MobileNet z zastosowaniem uczenia transferowego, rozmiaru serii 32, rozmiaru zdjęcia 224x224, 10 epok oraz funkcji softmax uzyskuje niemal idealny wynik na tym zbiorze danych. 

















