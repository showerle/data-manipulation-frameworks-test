library(data.table)
library(microbenchmark)

filename <- "datasets/binance_snapshot_till_2025-05-02.csv"
data <- fread(filename)

grt_filtering <- function(){
  filtered_dt <- data[`asks[0].price` >= mean(data$`asks[0].price`)] # nolint
  return(filtered_dt)
}

microbenchmark(grt_filtering(), times = 10)