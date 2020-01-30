library(ggplot2)
library(reshape2)


### PLOT RESULTS ###

###Create plotting function with trendline
Assoc_plot <- function(league){
  ggplot(league, aes(x = Season.Start, y = Transitivity.Rate)) +
    geom_point() +
    scale_y_continuous(limits = c(0.0, 0.4)) +
    geom_smooth(method = 'lm')}

#Plot each association
Assoc_plot(out_NBA)
Assoc_plot(out_ABA)
Assoc_plot(out_BAA)


###PLOT ALL ASSOCIATIONS TOGETHER###

##Merge the separate dataframe##
NBA_BAA <- merge(out_NBA, out_ABA, by = "Season.Start", all.x = TRUE)
names(NBA_ABA)[2] <- "NBA"
names(NBA_ABA)[3] <- "ABA"
all_assoc <- merge(NBA_ABA, out_BAA, by = "Season.Start", all = TRUE)
names(all_assoc)[4] <- "BAA"

##Melt the dataframe##
molten_assoc <- melt(all_assoc, id.vars = "Season.Start", 
                     variable.name = 'Association', value.name = "Transitivity.Rate")

##PLOT##
all_assoc_plot <- ggplot(molten_assoc, aes(x=Season.Start, y = Transitivity.Rate, 
                                        shape = Association, color = Association))+
  geom_point()+
  scale_color_manual(values = c("BAA" = "#fec524", "ABA" = "#8b0000", "NBA" = "#0e2240"))+
  scale_shape_manual(values = c("BAA" = 15, "ABA" = 17, "NBA" = 19))+
  scale_size_manual(values = c("BAA" = 8, "ABA" = 8, "NBA" = 8)) +
  geom_smooth(method = "lm")+
  xlab('Season') +
  ylab('Transitivity Rate') +
  theme_bw()
all_assoc_plot
