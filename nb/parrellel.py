import numpy as np
from concurrent.futures import ProcessPoolExecutor

# function to apply vectorized function in parallel
def apply_func_in_parallel(func, data, num_workers):
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        result = list(executor.map(lambda x: func(*x), data))
    return np.array(result)