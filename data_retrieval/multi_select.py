import pandas as pd
import polars as pl

filename = "datasets/binance_snapshot_till_2025-05-02.csv"
data = pd.read_csv(filename)
data_p = pl.read_csv(filename)
cols = data_p.columns
cols_selected = cols[int(len(cols)/2 -1):int(len(cols)-2)]
rows_selected_start, rows_selected_end = int(data_p.shape[0]/2 -1), int(data_p.shape[0]/4)

def col_select():
    res = data[cols_selected]

def col_select_polars():
    res = data_p.select(cols_selected)

def row_select():
    res = data.iloc[rows_selected_start:rows_selected_end,:]

def row_select_polars():
    res = data_p[rows_selected_start:rows_selected_end]

if __name__ == "__main__":
    import timeit

    res = pd.DataFrame(columns=['row', 'col'], index=['pandas', 'polars'])
    res.loc['pandas', 'col'] =  f"{timeit.timeit('col_select()', 'from __main__ import col_select',  number=100)/100:.3f}"
    res.loc['pandas', 'row'] = f"{timeit.timeit('row_select()', 'from __main__ import row_select', number=100)/100:.3f}"
    res.loc['polars', 'col'] =  f"{timeit.timeit('col_select_polars()', 'from __main__ import col_select_polars', number=100)/100:.3f}"
    res.loc['polars', 'row'] = f"{timeit.timeit('row_select_polars()', 'from __main__ import row_select_polars', number=100)/100:.3f}"
    print(res)


'''
            row      col
pandas      0.000    1.327
polars      0.000    0.000
data.table  0.670    1.182
'''
