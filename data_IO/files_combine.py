import pandas as pd
import polars as pl

path = './datasets'

def combine_files(num=2):
    dfs = []  
    for i in range(1, num+1):
        filename = f'{path}/binance-futures_book_snapshot_25_2023-05-{i:02}_BTCUSDT.csv'
        file = pd.read_csv(filename)
        dfs.append(file)
    
    print("preparing writing....")
    res = pd.concat(dfs, axis=0)  
    res.to_csv(f'{path}/binance_snapshot_till_2025-05-{num:02}.csv', index=False)

def combine_files_polars(num=2):
    res = None
    for i in range(1, num+1):
        filename = f'{path}/binance-futures_book_snapshot_25_2023-05-{i:02}_BTCUSDT.csv'
        file = pl.read_csv(filename)
        if res is None:
            res = file
        else:
            res = res.vstack(file)
            
    print("preparing writing....")
    res.write_csv(f'{path}/binance_snapshot_till_2025-05-{num:02}.csv')

if __name__ == "__main__":
    import timeit

    elapsed_time = timeit.timeit('combine_files()', "from __main__ import combine_files", number=1)
    print(f'pandas conbine 2 files in : {elapsed_time:.3f}s')     # 367.282s

    elapsed_time_polars = timeit.timeit('combine_files_polars()', "from __main__ import combine_files_polars", number=1)
    print(f'polars conbine 2 files in : {elapsed_time_polars:.3f}s') # 16.932s

    