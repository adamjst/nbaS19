library(ggplot2)
library(reshape2)
library(stringr)
library(magrittr)

##Force numeric and add association column
out_NBA$Season.Start <- as.numeric(rownames(out_NBA))
out_NBA$Season.num <- c(as.numeric(1:67))
out_ABA$Season.Start <- as.numeric(rownames(out_ABA))
out_ABA$Season.num <- c(as.numeric(1:8))
out_BAA$Season.Start <- as.numeric(rownames(out_BAA))
out_BAA$Season.num <- c(as.numeric(1:3))
out_WNBA$Season.Start <- as.numeric(rownames(out_WNBA))
out_WNBA$Season.num <- c(as.numeric(1:22))

##stack dataframes
BAA_WNBA <- rbind(out_BAA, out_WNBA)
NBA_ABA <- rbind(out_NBA, out_ABA)
all_assoc <- rbind(NBA_ABA, BAA_WNBA)



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
Assoc_plot(out_WNBA)
Assoc_plot(all_assoc)

all_plot <- function(league){
  ggplot(league, aes(x=Season.Start, y = TVR.Diff, shape = Assoc, color = Assoc))+
    geom_point()+
    geom_errorbar(aes(ymin=TVR.Diff-(TVR.Diff-Min.95), ymax=TVR.Diff+(Max.95-TVR.Diff)))+
    scale_color_manual(values = c("BAA" = "#fec524", "ABA" = "#8b0000", "NBA" = "#0e2240", "WNBA" = '#244289'))+
    scale_shape_manual(values = c("BAA" = 15, "ABA" = 17, "NBA" = 19, 'WNBA' = 21))+
    scale_size_manual(values = c("BAA" = 8, "ABA" = 8, "NBA" = 8, "WNBA" = 8)) +
    geom_smooth(method = 'lm', se = FALSE)+
    xlab('Season') +
    ylab('Difference in Transitivity Violation Rate') +
    theme_bw()
}
all_plot(all_assoc)

