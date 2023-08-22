import pandas as pd
import polars as pl

filename = "datasets/binance_snapshot_till_2025-05-02.csv"
data = pd.read_csv(filename)
data_p = pl.read_csv(filename)
data_p = data_p.with_columns((data_p['timestamp'] / 1e3).cast(pl.Datetime).dt.hour().alias("hour"))
data['hour'] = pd.to_datetime(data['timestamp'] / 1e3, unit='ns').dt.hour

def group_by_time():
    return data.groupby('hour').apply(lambda x: (x['asks[0].price'] * x['asks[0].amount']).sum() / x['asks[0].amount'].sum()).reset_index(name='weighted_avg')

def group_by_time_polars():
    return (data_p.groupby('hour')
            .agg(weighted_avg = 
                (pl.col('asks[0].price') * pl.col('asks[0].amount')).sum() / pl.col('asks[0].amount').sum())
            )

if __name__ == "__main__":
    import timeit
    num = 10
    funcs = ['group_by_time']
    res = pd.DataFrame(columns=funcs, index=['pandas', 'polars'])
    res.loc['pandas', funcs[0]] =  f"{timeit.timeit(f'{funcs[0]}()', f'from __main__ import {funcs[0]}',  number=num)/num:.3f}"
    res.loc['polars', funcs[0]] = f"{timeit.timeit(f'{funcs[0]}_polars()', f'from __main__ import {funcs[0]}_polars', number=num)/num:.3f}"
    print(res)


"""
       group_by_time
pandas         3.860
polars         0.221
data.table     0.144
"""