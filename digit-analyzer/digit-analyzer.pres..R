
train.complete <- read.csv("data/train.prep.bal.csv", header=TRUE)

pdf("Row_Column_Distribution_digits.bal.pdf",paper="a4",width=7,height=11)
for (i in 0:9)
{
      par(mfrow=c(2,1))
      data <- train.complete[train.complete$label == i,]
      boxplot(data[,29:2],main="Distribution Density ~ Row No.",horizontal=TRUE, outline=FALSE, ylab="Row No.", xlab = "Accumlated Density")
      mtext(paste("Digit: ",i), outer=TRUE,side = 3, line = -1, cex=1.2)
      boxplot(data[,30:57],main="Distribution Column No. ~ Density",outline=FALSE, xlab="Column No.", ylab = "Accumlated Density")
}
dev.off()

