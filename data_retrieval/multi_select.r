library(data.table)
library(microbenchmark)

filename <- "datasets/binance_snapshot_till_2025-05-02.csv"
data <- fread(filename)

cols <- names(data)
cols_selected <- cols[(length(cols) / 2): (length(cols) - 2)]
rows_selected_start <- (nrow(data) / 2) - 1
rows_selected_end <- (nrow(data) / 4)

col_select <- function() {
  res <- data[, .SD, .SDcols = cols_selected]
  return(res)
}

row_select <- function(){
  res <- data[rows_selected_start:rows_selected_end]
  return(res)
}

microbenchmark(col_select(), row_select(), times = 100)

# col_select()  1.182 s
# row_select() 0.670 s