library(mclust)
library(ggplot2)
library(dplyr)
library(HistogramTools)
library(boot)
library(ggplot2)
library(GGally)

data <- read.csv("10bar_DATA_NODIM.csv", header = T) # nolint
X <- data[1:6]
# plot.new()
# pairs(X[c(2, 4, 8)], main = "original")
varmax <- 0
tt <- 0
nr <- nrow(X)
#y1 <- X[4]
#y2 <- X[8]
maxlim <- 1
rand <- 1000
noise <- 0.5
groups <- 15
ucol <- 6
lcol <- 1
for (i in seq(1, maxlim)) {
    var <- rand * i
    print(var)
    set.seed(var)

    BIC <- mclustBIC(X[2:ucol], G = 1:groups)
    varmax[i] <- max(BIC, na.rm = T)
    tt[i] <- varmax[i]
    print(tt[i])
}
finmax <- max(tt, na.rm = T)
for (i in seq(1, maxlim)) {
    if (finmax == tt[i]) {
        print(tt[i])
        print(finmax)
        var <- rand * i
        print(var)
        set.seed(var)

        BIC <- mclustBIC(X[2:ucol], G = 1:groups)
        mod1 <- Mclust(X[2:ucol], x = BIC)
        print(summary(mod1))
        drmod <- MclustDR(mod1, lambda = 1)
        print(summary(drmod))

        plot.MclustDR(drmod, what = "boundaries", ngrid = 200)
        # Data write to get LDA analysis
        resout <- cbind(X[1], mod1$classification, mod1$data)
        write.csv(x = resout, file = "C:\\Users\\satya\\Desktop\\HBKU_IT_LAPTOP_BACKUP\\COREMOF_DATABASE\\DATA_REPOSITORY\\MCLUST\\CLASSCOMBINE_10bar_repeat.csv", row.names = FALSE) # nolint
        # Finish data writing for LDA
        Y <- table(data[, 1], mod1$classification)
        print(head(Y))
        name <- rownames(Y)
        finit <- 0
        numclass <- sum(table(unique(mod1$classification)))
        print(numclass)
        for (j in 1:numclass) {
            
            for (i in 1:nr) {
                if (Y[i, j] == 1) {
                    outnamecsv <- sprintf("C:\\Users\\satya\\Desktop\\HBKU_IT_LAPTOP_BACKUP\\COREMOF_DATABASE\\DATA_REPOSITORY\\MCLUST\\10bar_mofname_%s_original.csv", j) # nolint
                    # write.table(name[i],
                    write.table(data[i, 1:ucol],
                        file = outnamecsv, row.names = FALSE,
                        append = TRUE, col.names = FALSE, sep = " "
                    )
                    
                }
            }

        }
        break
    }
}