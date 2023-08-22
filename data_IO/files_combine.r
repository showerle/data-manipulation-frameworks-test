library(data.table)
library(microbenchmark)

combine_files <- function(num = 2) {
  path <- "./datasets"
  list_of_dt <- vector('list', num)  # nolint

  for (i in 1:num){
    filename <- sprintf('%s/binance-futures_book_snapshot_25_2023-05-%02d_BTCUSDT.csv', path, i) # nolint
    list_of_dt[[i]] <- fread(filename)
  }

  cat("preparing writing....\n")
  res <- rbindlist(list_of_dt)
  fwrite(res, sprintf('%s/binance_snapshot_till_2025-05-%02d.csv', path, num)) # nolint

}

microbenchmark(combine_files(), times = 1) # 106.1216