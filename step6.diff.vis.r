library(ggplot2)
library(reshape2)
library(stringr)
library(magrittr)

##Force numeric and add association column
out_NBA$Season.Start <- as.numeric(rownames(out_NBA))
out_NBA$Assoc <- 'NBA'
out_ABA$Season.Start <- as.numeric(rownames(out_ABA))
out_ABA$Assoc <- 'ABA'
out_BAA$Season.Start <- as.numeric(rownames(out_BAA))
out_BAA$Assoc <- 'BAA'

##stack dataframes
NBA_ABA <- rbind(out_NBA, out_ABA)
all_assoc <- rbind(NBA_ABA, out_BAA)



### PLOT RESULTS ###

###Create plotting function with trendline
Assoc_plot <- function(league){
  ggplot(league, aes(x=Season.Start, y = TVR.Diff))+
    geom_point()+
    geom_errorbar(aes(ymin=TVR.Diff-(TVR.Diff-Min.95), ymax=TVR.Diff+(Max.95-TVR.Diff)))+
    geom_smooth(method = 'lm', se = FALSE)+
    xlab('Season') +
    ylab('Difference in Transitivity Violation Rate') +
    theme_bw()
}

#Plot each association
Assoc_plot(out_NBA)
Assoc_plot(out_ABA)
Assoc_plot(out_BAA)
Assoc_plot(all_assoc)
