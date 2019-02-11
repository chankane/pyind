def roulette(pop, sel_rate, eval_func):
    ftns = _calc_ftns(pop, eval_func)
    sel_num = _calc_sel_num(pop, sel_rate)
    r = np.random.rand(sel_num) * ftns.sum()
    return pop[(ftns.cumsum()[:, np.newaxis] < r).sum(axis=0)]


def swap_idx(pop, mut_pb):
    #r = np.random.ranf(pop.shape)
    r = np.array([
        [3, 1, 6, 2, 4, 5],
        [4, 1, 2, 3, 5, 6],
    ]) * 0.1 - 0.01
    a = np.argsort(r, axis=1)
    #print(a)
    for j, row in enumerate(a):
        for i, col in enumerate(row):
            #print(r[j, col])
            if r[j, col] >= mut_pb:
                break
            #print("x")
            #print(col)
            #print("y")
            #print(a[j, -i-1])
            o = a[j, -i-1]
            pop[j, col], pop[j, o] = pop[j, o], pop[j, col]
    print(pop)

    @staticmethod
    def _get_args(conf):
        fnc = conf["func"]
        if fnc == elite or func == roulette:
            return int(pop_len * conf["rate"])
