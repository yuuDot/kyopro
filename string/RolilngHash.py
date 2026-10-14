# Rolling Hashで長さxの共通の文字列があるかどうか判定するコード例
# 区間演算とかもできるからセグ木に乗せられるらしい

n = int(input())
s = input()

mod = 2**61 - 1
base = 3491
b_table = [1] * (n + 1)
for i in range(n):
    b_table[i + 1] = (b_table[i] * base) % mod
o = [ord(i) for i in s]


def judge(x):
    before = set()
    crr = 0
    for i in range(x):
        crr += o[i] * b_table[x - i - 1]
        crr %= mod

    before.add(crr)
    for i in range(x, n):
        crr -= o[i - x] * b_table[x - 1]
        crr *= base
        crr += o[i]
        crr %= mod

        if crr in before:
            return True

        before.add(crr)

    return False
