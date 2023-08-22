import pandas as pd
import polars as pl

filename = "datasets/binance_snapshot_till_2025-05-02.csv"
data = pd.read_csv(filename)
data_p = pl.read_csv(filename)

def grt_filtering():
    return data[data['asks[0].price'] >= data['asks[0].price'].mean()]

def grt_filtering_polars():
    return data_p.filter(pl.col('asks[0].price') >= data_p.select(pl.mean('asks[0].price'))[0][0])


if __name__ == "__main__":
    import timeit

    res = pd.DataFrame(columns=['grt_filtering'], index=['pandas', 'polars'])
    res.loc['pandas', 'grt_filtering'] =  f"{timeit.timeit('grt_filtering()', 'from __main__ import grt_filtering',  number=10)/10:.3f}"
    res.loc['polars', 'grt_filtering'] = f"{timeit.timeit('grt_filtering_polars()', 'from __main__ import grt_filtering_polars', number=10)/10:.3f}"
    print(res)


'''
       grt_filtering
pandas         2.125
polars         0.665
data.table     1.578
'''