library(data.table)
library(microbenchmark)

filename <- "datasets/binance_snapshot_till_2025-05-02.csv"
data <- fread(filename)

sort_by_float <- function(){
#   class(data$`asks[0].amount`) # numeric # nolint
  setorder(data, -`asks[0].amount`)
}

microbenchmark(sort_by_float(), times = 10)