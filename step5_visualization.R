library(ggplot2)
library(reshape2)

### PLOT RESULTS ###
##Merge the separate real and permuted##
real_cont_NBA <- merge(out_NBA, control_out_NBA, by = "Season.Start", all.x = TRUE)
names(real_cont_NBA)[2] <- "real"
names(real_cont_NBA)[3] <- "permuted"
molten_NBA <- melt(real_cont_NBA, id.vars = "Season.Start", 
                     variable.name = 'Real.Permuted', value.name = 'Transitivity.Violation.Rate')
#ABA#
real_cont_ABA <- merge(out_ABA, control_out_ABA, by = "Season.Start", all.x = TRUE)
names(real_cont_ABA)[2] <- "real"
names(real_cont_ABA)[3] <- "permuted"
molten_ABA <- melt(real_cont_ABA, id.vars = "Season.Start", 
                     variable.name = 'Real.Permuted', value.name = 'Transitivity.Violation.Rate')
#BAA#
real_cont_BAA <- merge(out_BAA, control_out_BAA, by = "Season.Start", all.x = TRUE)
names(real_cont_BAA)[2] <- "real"
names(real_cont_BAA)[3] <- "permuted"
molten_BAA <- melt(real_cont_BAA, id.vars = "Season.Start", 
                     variable.name = 'Real.Permuted', value.name = 'Transitivity.Violation.Rate')

##PLOT##
###Create plotting function with trendline
molten_Assoc_plot <- function(league){
  ggplot(league, aes(x=Season.Start, y = Transitivity.Violation.Rate, color = Real.Permuted, shape = Real.Permuted))+
  geom_point()+
  scale_color_manual(values = c("real"= "black", "permuted" = "gray77"))+
  scale_shape_manual(values = c("real" = 15, "permuted" = 17))+
  scale_size_manual(values = c("real" = 8, "permuted" = 8)) +
  geom_smooth(method = "lm") +
  xlab('Season') +
  ylab('Transitivity Violation Rate') +
  theme_bw()
  }

#Plot each association
molten_Assoc_plot(molten_NBA)
molten_Assoc_plot(molten_ABA)
molten_Assoc_plot(molten_BAA)

###PLOT ALL ASSOCIATIONS TOGETHER###

##Merge the separate dataframes##
NBA_ABA <- merge(out_NBA, out_ABA, by = "Season.Start", all.x = TRUE)
names(NBA_ABA)[2] <- "NBA"
names(NBA_ABA)[3] <- "ABA"
all_assoc <- merge(NBA_ABA, out_BAA, by = "Season.Start", all = TRUE)
names(all_assoc)[4] <- "BAA"

##Melt the dataframe##
molten_assoc <- melt(all_assoc, id.vars = "Season.Start", 
                     variable.name = 'Association', value.name = 'Transitivity.Violation.Rate')


##PLOT##
all_assoc_plot <- ggplot(molten_assoc, aes(x=Season.Start, y = Transitivity.Violation.Rate, 
                                        shape = Association, color = Association))+
  geom_point()+
  scale_color_manual(values = c("BAA" = "#fec524", "ABA" = "#8b0000", "NBA" = "#0e2240"))+
  scale_shape_manual(values = c("BAA" = 15, "ABA" = 17, "NBA" = 19))+
  scale_size_manual(values = c("BAA" = 8, "ABA" = 8, "NBA" = 8)) +
  geom_smooth(method = "lm")+
  xlab('Season') +
  ylab('Transitivity Violation Rate') +
  theme_bw()
all_assoc_plot

