# Data training AND
data = [(0, 0, -1), (0, 1, -1), (1, 0, -1), (1, 1, 1)]

# Parameter
alpha = 0.8
theta = 0.5

# Bobot awal
w1 = 0
w2 = 0
b = 0

epoch = 0
converged = False


def activation(y_in):
    if y_in > theta:
        return 1
    elif y_in < -theta:
        return -1
    else:
        return 0


while not converged:
    epoch += 1
    print(f"\nEpoch {epoch}")
    converged = True

    for x1, x2, t in data:
        # hitung yin
        y_in = b + x1 * w1 + x2 * w2

        # fungsi aktivasi
        y = activation(y_in)

        print(f"x1={x1} x2={x2} yin={y_in:.2f} y={y} target={t}")

        # jika salah update bobot
        if y != t:
            w1 = w1 + alpha * t * x1
            w2 = w2 + alpha * t * x2
            b = b + alpha * t

            converged = False

            print("Update bobot:")
            print("w1 =", w1)
            print("w2 =", w2)
            print("b  =", b)

print("\nTraining selesai")
print("Total epoch:", epoch)
print("Bobot akhir:")
print("w1 =", w1)
print("w2 =", w2)
print("b =", b)

print("\nTesting model:")

for x1, x2, t in data:
    y_in = b + x1 * w1 + x2 * w2
    y = activation(y_in)
    print(x1, x2, "->", y)
