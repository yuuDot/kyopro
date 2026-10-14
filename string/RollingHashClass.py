class RollingHash:
    """
    文字列の長さをxとして、左から base^(x-1)*ord() + ... + base^0*ord() のhashを計算する
    """

    import random

    _mod = (1 << 61) - 1
    _base = random.randint(2, _mod - 2)
    _inv_base = pow(_base, -1, _mod)
    # 求める長さによって必要な長さが変わる
    _base_table = [1] * (10**6 + 1)
    for i in range(len(_base_table) - 1):
        _base_table[i + 1] = _base_table[i] * _base % _mod

    def __init__(self, string: str | list[str]):
        """
        ord()に入るイテラブルなやつをhashにする。文字列全てをhashにするので注意。
        """
        from collections import deque

        self.string = deque(string)
        self.hash_val = 0
        ln = len(string)
        for idx, s in enumerate(string):
            self.hash_val += ord(s) * RollingHash._base_table[ln - idx - 1]
            self.hash_val %= RollingHash._mod

    def add_right(self, x: str) -> None:
        """
        右側にxを追加する
        """
        self.hash_val *= RollingHash._base
        self.hash_val += ord(x)
        self.hash_val %= RollingHash._mod
        self.string.append(x)

    def add_left(self, x: str) -> None:
        """
        左側にxを追加する
        """
        self.hash_val += ord(x) * RollingHash._base_table[len(self.string)]
        self.hash_val %= RollingHash._mod
        self.string.appendleft(x)

    def pop_right(self) -> str:
        """
        右側の文字を削除する。削除した文字を返す。
        """
        rem = self.string.pop()
        self.hash_val -= ord(rem)
        self.hash_val *= RollingHash._inv_base
        self.hash_val %= RollingHash._mod

        return rem

    def pop_left(self) -> str:
        """
        左側の文字を削除する。削除した文字を返す。
        """
        rem = self.string.popleft()
        self.hash_val -= ord(rem) * RollingHash._base_table[len(self.string)]
        self.hash_val %= RollingHash._mod

        return rem

    def __str__(self):
        return f"RollingHash {{hash_val: {self.hash_val}, string: {''.join(self.string)}}}"

    def __eq__(self, other):
        if type(other) is not RollingHash:
            raise TypeError(f"{type(self)}と{type(other)}は比較できません")
        return self.hash_val == other.hash_val and len(self.string) == len(other.string)

    def __ne__(self, other):
        if type(other) is not RollingHash:
            raise TypeError(f"{type(self)}と{type(other)}は比較できません")
        return self.hash_val != other.hash_val or len(self.string) != len(other.string)
