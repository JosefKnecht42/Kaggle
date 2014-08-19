
train.complete <- read.csv("data/train.prep.csv", header=TRUE)

# split training data into train batch and test batch
library(caret)
library(FNN)
filename <- "knn_benchmark.eva.bal.csv"
set.seed(23)

training.rows <- createDataPartition(train.complete$label, 
                               p = 0.8, list = FALSE)
train.batch <- train.complete[training.rows, ]
test.batch <- train.complete[-training.rows, ]
trainlabels <- train.batch[,1]
traindata <- train.batch[,-1]
testdata <- test.batch[,-1]
testlabels <- test.batch[,1]
results <- (0:9)[knn(traindata, testdata, trainlabels, k = 10, algorithm="cover_tree")]

accuracy <- sum(results == testlabels)/length(testlabels)
print(accuracy)


output <- list()
output<-c(output,"Method;K Value; Iteration; Accuracy") 
for (a in c("kd_tree", "cover_tree","brute")){
      for (i in 1:3){
            for (k in 5:15){
                  print(paste("Starting Iteration:",a,i,k))
                  training.rows <- createDataPartition(train.complete$label, 
                                                       p = 0.8, list = FALSE)
                  train.batch <- train.complete[training.rows, ]
                  test.batch <- train.complete[-training.rows, ]
                  
                  trainlabels <- train.batch[,1]
                  traindata <- train.batch[,-1]
                  testdata <- test.batch[,-1]
                  testlabels <- test.batch[,1]
                  
                  results <- (0:9)[knn(traindata, testdata, trainlabels, k = k, algorithm=a)]
                  
                  accuracy <- sum(results == testlabels)/length(testlabels)
                  output<-c(output,paste(a,k,i,accuracy,sep=";"))
            }
      }
}
writeLines(as.character(output),filename)
