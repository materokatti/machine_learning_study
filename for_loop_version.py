import time
import numpy as np

def for_loop_operation(size):
    result = np.zeros(size)
    for i in range(size):
        result[i] = i * 2 + 1
    return result

if __name__ == "__main__":
    size = 1000000
    
    start_time = time.time()
    result_for = for_loop_operation(size)
    end_time = time.time()
    
    print(f"For loop version execution time: {end_time - start_time:.6f} seconds") 