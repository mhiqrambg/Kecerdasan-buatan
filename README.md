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

## Ringkasan


| Data Uji | Target | Prediksi | Status    |
| -------- | ------ | -------- | --------- |
| 1        | A      | A        | **BENAR** |
| 2        | A      | A        | **BENAR** |
| 3        | A      | A        | **BENAR** |


> Akurasi: **3/3 (100%)**

