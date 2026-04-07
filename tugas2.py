import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
EXCEL_PATH = BASE_DIR / "Data" / "dataset_font2.xlsx"

LEARNING_RATE = 1
EPOCHS = 100
LABELS = ["A", "B", "C", "D", "E", "J", "K"]


# LOAD DATA
def load_data():
    df = pd.read_excel(EXCEL_PATH, header=None)

    header_row = None
    for i in range(len(df)):
        row = df.iloc[i].astype(str).str.strip().tolist()
        if "X1" in row:
            header_row = i
            break

    if header_row is None:
        raise ValueError("Header X1 tidak ditemukan di Excel")

    header = df.iloc[header_row].tolist()
    df = df[(header_row + 1) :].copy()
    df.columns = [str(col).strip() for col in header]

    rename_map = {f"X{d}-1": f"X{d}0" for d in range(1, 7)}
    df.rename(columns=rename_map, inplace=True)

    x_cols = [f"X{i}" for i in range(1, 64)]
    y_cols = [f"Y{i}" for i in range(1, 8)]
    needed = x_cols + y_cols

    has_char = "Char" in df.columns
    if has_char:
        df["Char"] = df["Char"].astype(str).str.strip()

    missing = [c for c in needed if c not in df.columns]
    if missing:
        raise ValueError(f"Kolom tidak ditemukan: {missing}")

    for col in needed:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=needed)

    if len(df) == 0:
        raise ValueError("Tidak ada data valid di Excel")

    for col in needed:
        nilai_unik = set(df[col].astype(int).unique())
        if not nilai_unik.issubset({-1, 1}):
            raise ValueError(
                f"Kolom {col} mengandung nilai selain -1 dan 1: {nilai_unik}"
            )

    X = df[x_cols].astype(int).values
    Y = df[y_cols].astype(int).values
    chars = df["Char"].tolist() if has_char else [None] * len(df)

    print("Data training:", len(X))
    print("Shape X:", X.shape)
    print("Shape Y:", Y.shape)

    return X, Y, chars


# TRAIN PERCEPTRON
def train_perceptron(X, Y):
    n_samples, n_features = X.shape
    n_classes = Y.shape[1]

    W = np.zeros((n_classes, n_features))
    b = np.zeros(n_classes)

    for _ in range(EPOCHS):
        for i in range(n_samples):
            x = X[i]
            y = Y[i]

            for k in range(n_classes):
                net = np.dot(W[k], x) + b[k]
                y_pred = 1 if net >= 0 else -1

                if y_pred != y[k]:
                    W[k] += LEARNING_RATE * y[k] * x
                    b[k] += LEARNING_RATE * y[k]

    return W, b


# PREDICT
def predict(W, b, x_input):
    scores = []
    for k in range(len(W)):
        net = np.dot(W[k], x_input) + b[k]
        scores.append(net)

    scores = np.array(scores)

    if np.isnan(scores).any():
        raise ValueError("Skor mengandung NaN. Cek data training.")

    idx = int(np.argmax(scores))
    return idx, scores


# CETAK POLA
def print_pattern(x):
    print("\nPola input 9 x 7:")
    for i in range(9):
        row = x[i * 7 : (i + 1) * 7]
        print(" ".join("#" if v == 1 else "." for v in row))


# INPUT DATA UJI
def input_test_data(X_train, Y_train, chars):
    while True:
        print(f"\nMasukkan huruf ({', '.join(LABELS)}) untuk ambil dari dataset,")
        print("atau ketik 'manual' untuk input 63 angka sendiri.")
        raw = input("Input: ").strip()

        if raw.upper() in LABELS:
            letter = raw.upper()
            indices = [i for i, c in enumerate(chars) if c == letter]
            if not indices:
                print(f"Huruf {letter} tidak ditemukan di dataset. Coba lagi.")
                continue
            results = []
            for idx in indices:
                results.append((X_train[idx], Y_train[idx]))
            return results

        tokens = raw.split()
        is_numbers = all(t.lstrip("-").isdigit() for t in tokens) if tokens else False

        if raw.lower() == "manual" or is_numbers:
            if is_numbers:
                raw_x = tokens
            else:
                print("\nMasukkan 63 angka untuk X, hanya 1 atau -1")
                print("Pisahkan dengan spasi")
                raw_x = input("X: ").strip().split()

            if len(raw_x) != 63:
                print(
                    f"Input X harus tepat 63 angka (diterima {len(raw_x)}). Coba lagi."
                )
                continue

            try:
                x = np.array([int(v) for v in raw_x])
            except ValueError:
                print("Input X mengandung karakter bukan angka. Coba lagi.")
                continue

            if not np.all(np.isin(x, [-1, 1])):
                print("Input X hanya boleh berisi 1 dan -1. Coba lagi.")
                continue

            return [(x, None)]

        print(f"Input tidak dikenali: '{raw}'. Coba lagi.")


# =========================
# KONVERSI VEKTOR Y KE HURUF
# =========================
def y_vector_to_label(y_vector):
    for i, val in enumerate(y_vector):
        if val == 1:
            return LABELS[i]
    return "Tidak diketahui"


# =========================
# MAIN
# =========================
def main():
    print("=== TRAINING MODEL ===")
    X, Y, chars = load_data()
    W, b = train_perceptron(X, Y)

    if np.isnan(W).any() or np.isnan(b).any():
        raise ValueError("Bobot atau bias mengandung NaN")

    print("Training selesai")

    print("\n=== INPUT DATA UJI ===")
    test_data = input_test_data(X, Y, chars)

    for i, (x, y_target_vector) in enumerate(test_data):
        print(f"\n--- Data uji {i + 1}/{len(test_data)} ---")
        print(f"\nNilai X: {' '.join(map(str, x))}")
        print_pattern(x)

        idx, scores = predict(W, b, x)
        pred_label = LABELS[idx]

        print("\nSkor tiap huruf:")
        for huruf, skor in zip(LABELS, scores):
            print(f"  {huruf} = {int(skor)}")

        print(f"\nPrediksi huruf: {pred_label}")

        if y_target_vector is not None:
            target_label = y_vector_to_label(y_target_vector)
            print(f"Target Y      : {' '.join(map(str, y_target_vector))}")
            print(f"Target huruf  : {target_label}")
            if pred_label == target_label:
                print("Status        : BENAR")
            else:
                print("Status        : SALAH")


if __name__ == "__main__":
    main()
