library(ggplot2)
library(reshape2)
library(stringr)
library(magrittr)

##FROM https://onunicornsandgenes.blog/2017/04/23/using-r-a-function-that-adds-multiple-ggplot2-layers/
add_points <- function(df) {
  geom_point(aes(x = Season.Start, y = Mean), data = df)+
  geom_errorbar(aes(ymin='Min.95', ymax='Max.95'), data = df)
}

out_NBA$Season.Start <- as.numeric(rownames(out_NBA))
out_ABA$Season.Start <- as.numeric(rownames(out_ABA))
out_BAA$Season.Start <- as.numeric(rownames(out_BAA))
control_out_NBA$Season.Start <- as.numeric(rownames(control_out_NBA))
control_out_ABA$Season.Start <- as.numeric(rownames(control_out_ABA))
control_out_BAA$Season.Start <- as.numeric(rownames(control_out_BAA))

out_NBA$Real.Permuted <- "Real"
control_out_NBA$Real.Permuted <- "Permuted"
out_ABA$Real.Permuted <- "Real"
control_out_ABA$Real.Permuted <- "Permuted"
out_BAA$Real.Permuted <- "Real"
control_out_BAA$Real.Permuted <- "Permuted"

all_NBA <- rbind(out_NBA, control_out_NBA)
all_ABA <- rbind(out_ABA, control_out_ABA)
all_BAA <- rbind(out_BAA, control_out_BAA)

### PLOT RESULTS ###

###Create plotting function with trendline
Assoc_plot <- function(league){
  ggplot(league, aes(x=Season.Start, y = Mean, group=Real.Permuted, col=Real.Permuted, fill=Real.Permuted))+
    geom_point()+
    geom_errorbar(aes(ymin=Mean-(Mean-Min.95), ymax=Mean+(Max.95-Mean), group = Real.Permuted), width=.2,
                  position=position_dodge(.3))+
    geom_smooth(method = 'lm', se = FALSE)+
    scale_color_manual(values = c("Real"= "black", "Permuted" = "gray77"))+
    scale_shape_manual(values = c("Real" = 15, "Permuted" = 17))+
    scale_size_manual(values = c("Real" = 8, "Permuted" = 8)) +
    xlab('Season') +
    ylab('Transitivity Violation Rate') +
  theme_bw()
}

#Plot each association
Assoc_plot(all_NBA)
Assoc_plot(all_ABA)
Assoc_plot(all_BAA)
Assoc_plot(out_NBA, control_out_NBA)
Assoc_plot(out_ABA)
Assoc_plot(out_BAA)
Assoc_plot(control_out_NBA)
Assoc_plot(control_out_ABA)
Assoc_plot(control_out_BAA)

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

