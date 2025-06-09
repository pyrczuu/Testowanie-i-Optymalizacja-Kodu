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











