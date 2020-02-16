library(dplyr)                                            ####KEY####
library(here)                                             ###Three pound signs = a new section.###
library(ggplot2)                                          ##Two pound signs = explanatory statement of code##       
library(reshape2)                                         #One pound sign = optional print point. Take off to see what is happening under the hood.#
?sd
here()
##read data from giant csv.##
tables <- data.frame(read.csv(here('win.pct.csv')))

core_df <- tables[-c(2,5:7,9:31)]
names(core_df)[1] <- "Season.Start"

pct_test <- function(Association, year){

  ##Subsets the games for the particular association passed in the function's argument.##
  core_df <- core_df[ which(core_df$League == Association), ]

  #create list of teams competing in one year.##
  season_year <- core_df[ which(core_df$Season.Start == year), ]
  print(season_year)
  sd <- sd(season_year$Pct)
  print(sd)
  return(sd)
}

BAA_count <- 1
BAA_sd <- data.frame(matrix())
for(y in seq(1946,1948,1)){
  print(y)
  BAA_sd[BAA_count] <- pct_test("BAA", y)
  BAA_count <- BAA_count + 1
}
names(BAA_sd)[1:3] <- seq(1,3,1)
BAA_sd <- data.frame(t(BAA_sd))
BAA_sd$Season <- seq(1946,1948,1)
names(BAA_sd)[1] <- 'SD'
BAA_sd$Assoc <- "BAA"
View(BAA_sd)

ABA_count <- 1
ABA_sd <- data.frame(matrix())
for(y in seq(1967,1974,1)){
  print(y)
  ABA_sd[ABA_count] <- pct_test("ABA", y)
  ABA_count <- ABA_count + 1
}
names(ABA_sd)[1:3] <- seq(1,3,1)
ABA_sd <- data.frame(t(ABA_sd))
ABA_sd$Season <- seq(1967,1974,1)
names(ABA_sd)[1] <- 'SD'
ABA_sd$Assoc <- "ABA"
View(ABA_sd)

NBA_count <- 1
NBA_sd <- data.frame(matrix())
for(y in seq(1949,2018,1)){
  print(y)
  NBA_sd[NBA_count] <- pct_test("NBA", y)
  NBA_count <- NBA_count + 1
}
##Omit lockout years
names(NBA_sd)[1:70] <- seq(1949,2018,1)
NBA_sd <- data.frame(t(NBA_sd))
NBA_sd <- na.omit(NBA_sd)
NBA_sd$Season <- rownames(NBA_sd)
NBA_sd$Season <- as.numeric(NBA_sd$Season)
names(NBA_sd)[1] <- 'SD'
NBA_sd$Assoc <- "NBA"
View(NBA_sd)


##STACK Dataframes
NBA_ABA_sd <- rbind(NBA_sd, ABA_sd)
all_assoc_sd <- rbind(NBA_ABA_sd, BAA_sd)

###Visualize

sd_plot<- function(league){
  ggplot(league, aes(Season, SD))+
    geom_point()+
    geom_smooth(method = "lm")+
    ggtitle("Standard Deviation of Winning Pct")
}
sd_plot(all_assoc_sd)
sd_plot(NBA_sd)
sd_plot(ABA_sd)
sd_plot(BAA_sd)


