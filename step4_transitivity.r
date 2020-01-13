library(dplyr)
library(here)
library(ggplot2)
library(reshape2)

here()
#read data from giant csv
total <- read.csv(here('total_data.csv'))

#Separates calendar year from season year. If month number is less than 10 (October, then subtract one from given year)
total <- total %>%
  mutate(SeasonStart = if_else(total$Month < 10, -1, 0))

total$SeasonStart <- total$Year + total$SeasonStart

total$Association <- as.character(total$Association)

#Creates Season string to represent the whole season
total$Season <- paste(total$SeasonStart, "-", total$SeasonStart+1)

#Drop id columns and adjust column names
total <- total[ -c(1,2) ]
names(total)[2] <- 'Visitors'
names(total)[3] <- 'Vis.Pts'
names(total)[4] <- 'Home'
names(total)[5] <- 'Home.Pts'
names(total)[6] <- 'Box Score'
names(total)[7] <- 'URL'

#convert points to numeric
total$Vis.Pts <- as.numeric(total$Vis.Pts)
total$Home.Pts <- as.numeric(total$Home.Pts)
tail(total)

#Create a list from the separate Associations
Association <- as.character(unique(total$Association))
Association

#Set counter for transitivity
transitivity <- 0
no_transitivity <- 0

#Create transitivity function to create iterability for each association. Here, I picked 50.
transitivity_test <- function(Association, year){
  for(i in seq(1,50,1)) {
    #Counts iteration
    #print(i)
    
    #Subsets the games for the particular association passed in the function's argument
    total <- total[ which(total$Association == Association), ]
    
    #create list of teams competing in one year
    season_year <- total[ which(total$SeasonStart == year), ]
    teams <- as.character(unique(season_year$Visitors))
    
    #pick three teams randomly
    sample <- sample(teams, size = 3, replace = FALSE)
    sample1 <- sample[1]
    sample2 <- sample[2]
    sample3 <- sample[3]
    
    ###OBTAIN BOXSCORES OF SAMPLED TEAMS###
    
    #Find the boxscore results from the first sampled team
    sampled_games1 <- season_year[ which(season_year$Home == sample1 | season_year$Visitors == sample1), ]
    
    #Find the results from the first sampled team's schedule in which they faced team two
    game1 <- sampled_games1[ which(sampled_games1$Home == sample2 | sampled_games1$Visitors == sample2), ]
    
    #Find the boxscore results from the second sampled team
    sampled_games2 <- season_year[ which(season_year$Home == sample2 | season_year$Visitors == sample2), ]
    
    #Find the results from the second sampled team's schedule in which they faced team three
    game2 <- sampled_games2[ which(sampled_games2$Home == sample3 | sampled_games2$Visitors == sample3), ]
    
    #Find the boxscore results from the first sampled team's schedule in which they faced team three
    game3 <- sampled_games1[ which(sampled_games1$Home == sample3 | sampled_games1$Visitors == sample3), ]
    
    ###FIND RANDOM GAME AMONG BOXSCORES AND DETERMINE WINNER###
    
    ##GAME 1##
    #find random game involving two teams in same year
    random_game1 <- game1[sample(nrow(game1), 1), ]
    
    #determine which points total is greater
    won1 <- pmax(random_game1$Vis.Pts, random_game1$Home.Pts)
    
    #Identify winner and convert to character
    winner1 <- if_else(won1 == random_game1$Vis.Pts, random_game1$Visitors, random_game1$Home)
    winner1 <- as.character(winner1)  
    
    ##Game 2##
    #find random other game involving second set of two, print winner
    random_game2 <- game2[sample(nrow(game2), 1), ]
    
    #determine which points total is greater
    won2 <- pmax(random_game2$Vis.Pts, random_game2$Home.Pts)
    
    #Identify winner and convert to character
    winner2 <- if_else(won2 == random_game2$Vis.Pts, random_game2$Visitors, random_game2$Home)
    winner2 <- as.character(winner2)  
    
    ##Game 3##
    #find random other game involving first and third team, print winner
    random_game3 <- game3[sample(nrow(game3), 1), ]
    
    #determine which points total is greater
    won3 <- pmax(random_game3$Vis.Pts, random_game3$Home.Pts)
    
    #Identify winner and convert to character
    winner3 <- if_else(won3 == random_game3$Vis.Pts, random_game3$Visitors, random_game3$Home)
    winner3 <- as.character(winner3)
    
    ###DETERMINE TRANSITIVITY AMONG GAME WINNERS###
    
    #Check to ensure at least one game between three teams
    if (length(winner1) == 0 | length(winner2) == 0 | length(winner3) == 0 )
      next
    
    #Print winners to show evidence of transitivity
    #print(winner1)
    #print(winner2)
    #print(winner3)
    
    if (length(unique(c(winner1,winner2,winner3))) != 3){
      #print('Transitivity violation')
      ##Count transitivity violation
      no_transitivity <- no_transitivity + 1
    } else{
      #print('Transitivity')
      ##Count no transitivity violation
      transitivity <- transitivity + 1
    }
    ###Calculate transitivity rate as transitivity divided by total tests
    rate <- transitivity/(transitivity + no_transitivity)
    #print(rate)
  }
#Return the rate to the overall matrix
return(rate)
}

### APPLYING THE FUNCTION AND EXTRACTION OF TRANSITIVITY RATES ###

#Create empty matrix, then cycle through season and apply transitivity function, before binding return into data frame

##NBA##

out_NBA <- data.frame('Rate' = numeric())
for (i in seq(1949,2018,1)){
  NBA <- transitivity_test('NBA', i)
  out_NBA <- rbind(out_NBA, NBA)
}
#Adjust column names on new data frame
names(out_NBA)[1] <- "Transitivity.Rate"
out_NBA <- cbind(out_NBA, Season.Start = c(seq(1949,2018,1)))
out_NBA <- out_NBA[, c(2,1)]
out_NBA

##ABA##

out_ABA <- data.frame('Rate' = numeric())
for (i in seq(1967,1975,1)){
  ABA <- transitivity_test('ABA', i)
  out_ABA <- rbind(out_ABA, ABA)
}
#Adjust column names on new data frame
names(out_ABA)[1] <- "Transitivity.Rate"
out_ABA <- cbind(out_ABA, Season.Start = c(seq(1967,1975,1)))
out_ABA <- out_ABA[, c(2,1)]
out_ABA

##BAA##

out_BAA <- data.frame('Rate' = numeric())
for (i in seq(1946,1948,1)){
  BAA <- transitivity_test('BAA', i)
  out_BAA <- rbind(out_BAA, BAA)
}
#Adjust column names on new data frame
names(out_BAA)[1] <- "Transitivity.Rate"
out_BAA <- cbind(out_BAA, Season.Start = c(seq(1946,1948,1)))
out_BAA <- out_BAA[, c(2,1)]
out_BAA
