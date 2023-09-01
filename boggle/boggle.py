import numpy as np

rng = np.random.default_rng()


def random_letter() -> str:
    return chr(rng.integers(low=65, high=90, endpoint=True))


grid = np.full((4, 4), fill_value=" ", dtype=np.str_)

grid[0, 0] = "A"
grid[1, 1] = "B"

print(grid)
