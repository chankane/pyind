# pyind
遺伝的アルゴリズムライブラリ (Python3)

**pyindはndarray (numpy) のみをサポートします**

## インストール
Coming soon...
~~``pip install pyind``~~

## 評価関数について
評価関数の形式は以下のとおりです
```python
def 評価関数(個体):  # 個体は遺伝子の配列
    return この個体の適応度

```

## `conf`について
`conf`の形式は以下のとおりです
```python
conf_format = {
    "eval": {
        "func": 評価関数  # 必須項目　既定値なし
    },
    "sel": {
        # 以下の「テーブルSel」を参照ください
    },
    "xovr": {
        # 以下の「テーブルXovr」を参照ください
    },
    "mut": {
        # 以下の「テーブルMut」を参照ください
    },
}
```

`conf["sel"]` に設定できる値は表に示すとおりです

カッコの中はデフォルト値

テーブル Sel

"sel" (elitism) | "num" (10)
-- | :--:
elitism | 0&ndash;size of poplation
roulette | 0&ndash;size of poplation

`conf["xovr"]` に設定できる値は表に示すとおりです

カッコの中はデフォルト値

テーブル Xovr

"xovr" (p2) | "pb" (0.875)
-- | :--:
p2 | 0&ndash;1
uniform | 0&ndash;1
ox | 0&ndash;1

`conf["mut"]` に設定できる値は表に示すとおりです

カッコの中はデフォルト値

テーブル Mut

"mut" (flip_bit) | "pb" (0.0075)| "delta" (1)
-- | :--: | :--:
flip_bit | 0&ndash;1
boundary | 0&ndash;1 | 0&ndash;&infin;
swap_idx | 0&ndash;1

## 今後の予定
1. バグを直す
1. 選択、交差、突然変異の関数を追加する
1. もっとはやくする

## ライセンス
MIT

## サンプルコード
### Onemax 問題
```python
# Onemax Problem
import numpy as np

from pyind import pyind as pi
from pyind import defaults as df


IND_LEN = 100
POP_LEN = 100


def evl(ind):
    return ind.sum()


if __name__ == "__main__":
    pop = np.random.randint(2, size=(POP_LEN, IND_LEN))

    conf = df.CONF
    conf["eval"]["func"] = evl

    best = pi.Pyind(pop, conf).run()

    print("best ind: ")
    print(best)

```
### 巡回セールスマン問題 (TSP)
```python
# Traveling salesman problem

import numpy as np
import matplotlib.pyplot as plt

from pyind import pyind as pi
from pyind import crossover as xovr
from pyind import mutation as mut
from pyind import defaults as df


CITIES_LEN = 30
POP_LEN = 300
END_GEN = 500

cities = np.random.rand(CITIES_LEN * 2).reshape((-1, 2))


def evl(ind):
    total = 0
    for i in range(1, len(ind)):
        total += np.linalg.norm(cities[ind[i]] - cities[ind[i - 1]])
    return -total


def solve(pop):
    conf = df.CONF
    conf["eval"]["func"] = evl
    conf["xovr"]["func"] = xovr.ox
    conf["mut"]["func"] = mut.swap_idx
    conf["mut"]["pb"] = 0.10
    return pi.Pyind(pop, conf).run(END_GEN)


if __name__ == "__main__":
    t = cities.T

    # Create pop
    pop = np.tile(np.arange(CITIES_LEN), (POP_LEN, 1))
    for e in pop:
        np.random.shuffle(e)

    # Plot gen 0
    idx = pop[0]
    plt.plot(t[0, idx], t[1, idx], label="gen 0", marker="o")

    best = solve(pop)
    print("best ind: ")
    print(best)

    # Plot gen END_GEN
    idx = best
    plt.plot(t[0, idx], t[1, idx], label="gen " + str(END_GEN), marker="o")

    plt.legend()
    plt.show()

```
