from multiprocessing import Pool, cpu_count

def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize(*numbers):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(find_factors, numbers)
    return results
if __name__ == '__main__':

    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'{a}\n{b}\n{c}\n{d}')