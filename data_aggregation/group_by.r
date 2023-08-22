library(data.table)
library(microbenchmark)

filename <- "datasets/binance_snapshot_till_2025-05-02.csv"
data <- fread(filename)
data[, timestamp := as.POSIXct(timestamp / 1000, origin = "1970-01-01")]
data[, hour := as.integer(format(timestamp, "%H"))]

group_by_time <- function(){
  return(data[, weighted_avg := sum(`asks[0].price` * `asks[0].amount`)
              / sum(`asks[0].amount`),
              by = hour])
}

microbenchmark(group_by_time())  # 0.144