import pandas as pd
import polars as pl

filename = "datasets/binance_snapshot_till_2025-05-02.csv"
data = pd.read_csv(filename)
data_p = pl.read_csv(filename)

def sort_by_float():
    return data.sort_values('asks[0].amount', ascending=False, inplace=True)

def sort_by_float_polars():
    return data_p.sort('asks[0].amount', descending=True)

def sort_by_interger():
    pass

def sort_by_str():
    pass

if __name__ == "__main__":
    import timeit
    num = 10
    res = pd.DataFrame(columns=['sort_by_float'], index=['pandas', 'polars'])
    res.loc['pandas', 'sort_by_float'] =  f"{timeit.timeit('sort_by_float()', 'from __main__ import sort_by_float',  number=num)/num:.3f}"
    res.loc['polars', 'sort_by_float'] = f"{timeit.timeit('sort_by_float_polars()', 'from __main__ import sort_by_float_polars', number=num)/num:.3f}"
    print(res)

"""
       sort_by_float
pandas        4.777
polars        3.026
data.table    0.552
"""