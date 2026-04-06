# Output Tugas 3 — Perceptron Pengenalan Huruf (3 Data Uji)

## Instalasi

1. Install `uv` (package manager Python):

```bash
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

1. Install dependencies:

```bash
uv sync
```

## Menjalankan Program

```bash
uv run tugas3.py
```

---

## Training Model


| Parameter     | Nilai    |
| ------------- | -------- |
| Data training | 21       |
| Shape X       | (21, 63) |
| Shape Y       | (21, 7)  |
| Learning Rate | 1        |
| Epochs        | 100      |


## Input Data Uji

```
Input: A
Input manual : -1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1 1 1 1 -1 1 1 1
```

Terdapat **3 data** untuk huruf **A** dalam dataset.

---

## Hasil Deteksi

### Data Uji 1/3

**Pola input 9 x 7:**

```
. . # # . . .
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # # # # . .
. # . . . # .
. # . . . # .
# # # . # # #
```

**Skor tiap huruf:**


| Huruf | Skor |
| ----- | ---- |
| A     | 54   |
| B     | -84  |
| C     | -70  |
| D     | -70  |
| E     | -70  |
| J     | -80  |
| K     | -54  |



| Keterangan     | Nilai                 |
| -------------- | --------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                     |
| Prediksi huruf | A                     |
| **Status**     | **BENAR**             |


---

### Data Uji 2/3

**Pola input 9 x 7:**

```
. . # # . . .
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # # # # . .
. # . . . # .
. # . . . # .
# # # . # # #
```

**Skor tiap huruf:**


| Huruf | Skor |
| ----- | ---- |
| A     | 54   |
| B     | -84  |
| C     | -70  |
| D     | -70  |
| E     | -70  |
| J     | -80  |
| K     | -54  |



| Keterangan     | Nilai                 |
| -------------- | --------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                     |
| Prediksi huruf | A                     |
| **Status**     | **BENAR**             |


---

### Data Uji 3/3

**Pola input 9 x 7:**

```
. . # # . . .
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # # # # . .
. # . . . # .
. # . . . # .
# # # . # # #
```

**Skor tiap huruf:**


| Huruf | Skor |
| ----- | ---- |
| A     | 54   |
| B     | -84  |
| C     | -70  |
| D     | -70  |
| E     | -70  |
| J     | -80  |
| K     | -54  |



| Keterangan     | Nilai                 |
| -------------- | --------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                     |
| Prediksi huruf | A                     |
| **Status**     | **BENAR**             |


---

## Input Manual

```
Input: -1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1
       -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1
       1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1 1 1 1 -1 1 -1 -1
```

**Pola input 9 x 7:**

```
. . # # . . .
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # # # # . .
. # . . . # .
. # . . . # .
# # # . # . .
```

**Skor tiap huruf:**


| Huruf | Skor |
| ----- | ---- |
| A     | 50   |
| B     | -76  |
| C     | -74  |
| D     | -58  |
| E     | -74  |
| J     | -68  |
| K     | -54  |



| Keterangan     | Nilai |
| -------------- | ----- |
| Prediksi huruf | **A** |


---

## Ringkasan


| Data Uji        | Target | Prediksi | Status    |
| --------------- | ------ | -------- | --------- |
| Dataset A (1/3) | A      | A        | **BENAR** |
| Dataset A (2/3) | A      | A        | **BENAR** |
| Dataset A (3/3) | A      | A        | **BENAR** |
| Input Manual    | —      | A        |           |


> Akurasi dataset: **3/3 (100%)**

