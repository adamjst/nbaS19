library(ggplot2)

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