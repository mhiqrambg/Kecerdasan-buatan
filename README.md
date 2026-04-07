# Output Tugas 2 — Perceptron Pengenalan Huruf (3 Data Uji)

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
uv run tugas2.py
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

**Nilai X:**

```
-1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1 1 1 1 -1 1 1 1
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
# # # . # # #
```

**Skor tiap huruf:**

| Huruf | Skor |
| ----- | ---- |
| A     | 8    |
| B     | -88  |
| C     | -76  |
| D     | -76  |
| E     | -46  |
| J     | -62  |
| K     | -56  |

| Keterangan     | Nilai                  |
| -------------- | ---------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                      |
| Prediksi huruf | A                      |
| **Status**     | **BENAR**              |

---

### Data Uji 2/3

**Nilai X:**

```
-1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 1 1 1 1 1 -1 -1 1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1
```

**Pola input 9 x 7:**

```
. . . # . . .
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # . . . # .
. # # # # # .
. # . . . # .
. # . . . # .
```

**Skor tiap huruf:**

| Huruf | Skor |
| ----- | ---- |
| A     | 32   |
| B     | -52  |
| C     | -60  |
| D     | -44  |
| E     | -50  |
| J     | -22  |
| K     | -16  |

| Keterangan     | Nilai                  |
| -------------- | ---------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                      |
| Prediksi huruf | A                      |
| **Status**     | **BENAR**              |

---

### Data Uji 3/3

**Nilai X:**

```
-1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 1 1 1 1 1 -1 1 -1 -1 -1 -1 -1 1 1 -1 -1 -1 -1 -1 1 1 1 -1 -1 -1 1 1
```

**Pola input 9 x 7:**

```
. . . # . . .
. . . # . . .
. . # . # . .
. . # . # . .
. # . . . # .
. # # # # # .
# . . . . . #
# . . . . . #
# # . . . # #
```

**Skor tiap huruf:**

| Huruf | Skor |
| ----- | ---- |
| A     | 0    |
| B     | -28  |
| C     | -38  |
| D     | -36  |
| E     | -28  |
| J     | -30  |
| K     | -18  |

| Keterangan     | Nilai                  |
| -------------- | ---------------------- |
| Target Y       | `1 -1 -1 -1 -1 -1 -1` |
| Target huruf   | A                      |
| Prediksi huruf | A                      |
| **Status**     | **BENAR**              |

---

## Input Manual

```
Input: -1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1
       -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1
       1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1 1 1 1 -1 1 -1 -1
```

**Nilai X:**

```
-1 -1 1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 -1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 1 -1 -1 1 -1 -1 -1 1 -1 1 1 1 -1 1 -1 -1
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
