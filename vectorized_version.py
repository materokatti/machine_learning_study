import time
import numpy as np

def vectorized_operation(size):
    arr = np.arange(size)
    return arr * 2 + 1

if __name__ == "__main__":
    size = 1000000
    
    start_time = time.time()
    result_vec = vectorized_operation(size)
    end_time = time.time()
    
    print(f"Vectorized version execution time: {end_time - start_time:.6f} seconds") 