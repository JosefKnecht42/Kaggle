# makes the KNN submission

library(FNN)

train <- read.csv("data/train.csv", header=TRUE)
test <- read.csv("data/test.csv", header=TRUE)

# train.prep <- read.csv("data/train.prep.bal.csv", header=TRUE)
# test.prep <- read.csv("data/test.prep.bal.csv", header=TRUE)
# for (i in 2:57){
#       train[colnames(train.prep)[i]] <- train.prep[,i]
# }
# for (i in 1:56){
#       test[colnames(test.prep)[i]] <- test.prep[,i]
# }


labels <- train[,1]
train <- train[,-1]


results <- (0:9)[knn(train, test, labels, k = 10, algorithm="cover_tree")]

write(results, file="knn_benchmark.sub3.csv", ncolumns=1) 
