from tardis_dev import datasets
from tokens import token

datasets.download(
    exchange="binance-futures",
    data_types=[
            "book_snapshot_25"
    ],
    from_date="2023-05-01",
    to_date="2023-06-01",
    symbols=["BTCUSDT"],
    api_key=token,
)


