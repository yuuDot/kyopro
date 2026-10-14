class Manacher:
    def __init__(self, s):
        n = len(s)
        self.n = n

        # d1[i]: i を中心とする奇数長回文の半径（中心を含む）
        self.d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(self.d1[l + r - i], r - i + 1)

            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1

            self.d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # d2[i]: i-1 と i の間を中心とする偶数長回文の半径
        self.d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(self.d2[l + r - i + 1], r - i + 1)

            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1

            self.d2[i] = k
            if i + k - 1 > r:
                l, r = i - k, i + k - 1

    def judge(self, l, r):
        """s[l:r] が回文かどうかを判定する。r は含まない。"""
        length = r - l

        if length <= 1:
            return True

        if length % 2 == 1:
            # 奇数長：中央の文字を中心とする
            return self.d1[(l + r) // 2] >= (length + 1) // 2
        else:
            # 偶数長：中央の文字間を中心とする
            return self.d2[(l + r) // 2] >= length // 2
