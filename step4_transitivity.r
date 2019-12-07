library(dplyr)
library(here)

#read data from giant csv
total <- read.csv(file.path('data', 'total_data.csv'))

#Separates calendar year from season year. If month number is less than 10 (October, then subtract one from given year)
total <- total %>%
  mutate(SeasonStart = if_else(total$Month < 10, -1, 0))

total$SeasonStart <- total$Year + total$SeasonStart

#Adjust column names
names(total)[5]<-'Vis.Pts'
names(total)[7]<-'Home.Pts'

#convert points to numeric
total$Vis.Pts <- as.numeric(total$Vis.Pts)
total$Home.Pts <- as.numeric(total$Home.Pts)
tail(total)

#Create transitivity function to create iterability based on a given count
transitivity_test <- function(year){
  for(i in seq(1,50,1)) {
    print(i)
    
    #create list of teams competing in one year
    sample_year <- total[ which(total$SeasonStart == year), ]
    teams <- as.character(unique(sample_year$Visitor.Neutral))

    #pick three teams randomly
    sample <- sample(teams, size = 3, replace = FALSE)
    sample1 <- sample[1]
    sample2 <- sample[2]
    sample3 <- sample[3]
    
    ###OBTAIN BOXSCORES OF SAMPLED TEAMS###
    
    #Find the boxscore results from the first sampled team
    sampled_games1 <- sample_year[ which(sample_year$Home.Neutral == sample1 | sample_year$Visitor.Neutral == sample1), ]

    #Find the results from the first sampled team's schedule in which they faced team two
    game1 <- sampled_games1[ which(sampled_games1$Home.Neutral == sample2 | sampled_games1$Visitor.Neutral == sample2), ]
    
    #Find the boxscore results from the second sampled team
    sampled_games2 <- sample_year[ which(sample_year$Home.Neutral == sample2 | sample_year$Visitor.Neutral == sample2), ]

    #Find the results from the second sampled team's schedule in which they faced team three
    game2 <- sampled_games2[ which(sampled_games2$Home.Neutral == sample3 | sampled_games2$Visitor.Neutral == sample3), ]
    
    #Find the boxscore results from the first sampled team's schedule in which they faced team three
    game3 <- sampled_games1[ which(sampled_games1$Home.Neutral == sample3 | sampled_games1$Visitor.Neutral == sample3), ]
    
    ###FIND RANDOM GAME AMONG BOXSCORES AND DETERMINE WINNER###
    
    ##GAME 1##
    #find random game involving two teams in same year
    random_game1 <- game1[sample(nrow(game1), 1), ]
    
    #determine which points total is greater
    won1 <- pmax(random_game1$Vis.Pts, random_game1$Home.Pts)
    
    #Identify winner and convert to character
    winner1 <- if_else(won1 == random_game1$Vis.Pts, random_game1$Visitor.Neutral, random_game1$Home.Neutral)
    winner1 <- as.character(winner1)  
    
    ##Game 2##
    #find random other game involving second set of two, print winner
    random_game2 <- game2[sample(nrow(game2), 1), ]
    
    #determine which points total is greater
    won2 <- pmax(random_game2$Vis.Pts, random_game2$Home.Pts)
    
    #Identify winner and convert to character
    winner2 <- if_else(won2 == random_game2$Vis.Pts, random_game2$Visitor.Neutral, random_game2$Home.Neutral)
    winner2 <- as.character(winner2)  
    
    ##Game 3##
    #find random other game involving first and third team, print winner
    random_game3 <- game3[sample(nrow(game3), 1), ]
    
    #determine which points total is greater
    won3 <- pmax(random_game3$Vis.Pts, random_game3$Home.Pts)
    
    #Identify winner and convert to character
    winner3 <- if_else(won3 == random_game3$Vis.Pts, random_game3$Visitor.Neutral, random_game3$Home.Neutral)
    winner3 <- as.character(winner3)
    
    ###DETERMINE TRANSITIVITY AMONG GAME WINNERS###
    
    #Check to ensure at least one game between three teams
    if (length(winner1) == 0 | length(winner2) == 0 | length(winner3) == 0 )
      next
    
    #Print winners to show evidence of transitivity
    print(winner1)
    print(winner2)
    print(winner3)

    #Check to see if the winner of the first matchup also beat the third
    A <- winner1 != winner3
    #Check to see if the winner of the second matchup also beat the third
    B <- winner2 != winner3
    #Check to see if the winner of the first matchup also beat the third
    C <- winner1 != winner2
    
    if ((A == TRUE) & (B == TRUE) & (C == TRUE)){
      print('Transitivity violation')
    } else{
      print('Transitivity')
    }
    }
  }

#Cycle through each season and apply function
for (i in seq(1946,2018,1)){
  print(i)
  transitivity_test(i)}
