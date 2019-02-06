import crossover as xovr
import mutation as mut
import selection as sel


# probability
XOVR_PB = 0.5
MUT_PB = 0.05 * 0.2

# func
SEL_FUNC = sel.elite
XOVR_FUNC = xovr.p2
MUT_FUNC = mut.flip_bit

# other
SEL_RATE = 0.01
END_GEN = 40
