# pyind
遺伝的アルゴリズムライブラリ

**pyindはndarray (numpy) のみをサポートします**

## インストール
``pip install pyind``

## `conf`について
`conf`の形式は以下のとおりです
```python
conf_format = {
    "eval": {
        "func": evaluation_function
    },
    "sel": {
        "func": selection_function,
        # Some parameters..
    },
    "xovr": {
        "func": crossover_function,
        # Some parameters..
    },
    "mut": {
        "func": mutation_function,
        # Some parameters..
    },
    "goal_ind": goal_individual
}
```
関数とパラメータの対応は以下の通りです

選択関数

関数 \ パラメータ (既定値) | num (10)
-- | :--:
elite | :heavy_check_mark:
roulette | :heavy_check_mark:

交叉関数

関数 \ パラメータ (既定値) | pb (0.875)
-- | :--:
p2 | :heavy_check_mark:
uniform | :heavy_check_mark:
ox | :heavy_check_mark:

突然変異関数

関数 \ パラメータ (既定値) | pb (0.0075)| delta (1)
-- | :--: | :--:
flip_bit | :heavy_check_mark:
boundary | :heavy_check_mark: | :heavy_check_mark:
swap_idx | :heavy_check_mark:

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
    conf["goal_ind"] = np.ones(IND_LEN)

    best = pi.Pyind(pop, conf).start()

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


CITIES_LEN = 15
POP_LEN = 200
END_GEN = 500

cities = np.random.rand(CITIES_LEN * 2).reshape((-1, 2))


def evl(ind):
    total = 0
    for i in range(1, ind.shape[0]):
        total += np.linalg.norm(cities[ind[i]] - cities[ind[i - 1]])
    return -total


def solve(pop):
    conf = df.CONF
    conf["eval"]["func"] = evl
    conf["xovr"]["func"] = xovr.ox
    conf["mut"]["func"] = mut.swap_idx
    conf["mut"]["pb"] = 0.05
    return pi.Pyind(pop, conf).start(END_GEN)


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
