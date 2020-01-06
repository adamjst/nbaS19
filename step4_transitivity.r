library(dplyr)
library(here)
library(ggplot2)

#read data from giant csv
total <- read.csv(file.path('data', 'total_data.csv'))

#Separates calendar year from season year. If month number is less than 10 (October, then subtract one from given year)
total <- total %>%
  mutate(SeasonStart = if_else(total$Month < 10, -1, 0))

total$SeasonStart <- total$Year + total$SeasonStart

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
Association <- (unique(total$Association))

#Set counter for transitivity
transitivity <- 0
no_transitivity <- 0

#Create transitivity function to create iterability for each association. Here, I picked 50.
transitivity_test <- function(Association, year){
  for(i in seq(1,50,1)) {
    #Counts iteration
    print(i)
    
    #Subsets the games for the particular association passed in the function's argument
    total <- total[ which(total$Association == Association), ]
    
    #create list of teams competing in one year
    season_year <- total[ which(total$SeasonStart == year), ]
    teams <- as.character(unique(season_year$Visitor.Neutral))
    
    #pick three teams randomly
    sample <- sample(teams, size = 3, replace = FALSE)
    sample1 <- sample[1]
    sample2 <- sample[2]
    sample3 <- sample[3]
    
    ###OBTAIN BOXSCORES OF SAMPLED TEAMS###
    
    #Find the boxscore results from the first sampled team
    sampled_games1 <- season_year[ which(season_year$Home.Neutral == sample1 | season_year$Visitor.Neutral == sample1), ]
    
    #Find the results from the first sampled team's schedule in which they faced team two
    game1 <- sampled_games1[ which(sampled_games1$Home.Neutral == sample2 | sampled_games1$Visitor.Neutral == sample2), ]
    
    #Find the boxscore results from the second sampled team
    sampled_games2 <- season_year[ which(season_year$Home.Neutral == sample2 | season_year$Visitor.Neutral == sample2), ]
    
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
    print(rate)
  }
#Return the rate to the overall matrix
return(rate)
}

### APPLYING THE FUNCTION AND EXTRACTION OF TRANSITIVITY RATES ###

#Create empty matrix, then cycle through season and apply transitivity function, before binding return into data frame

###ISSUE: The function seems to retain only the last returned "rate"
#NBA

NBA <- matrix(byrow = TRUE)
for (i in seq(1949,2018,1)){
  print(i)
  NBA <- lapply(NBA, function(x)transitivity_test('NBA', i))
  out_NBA <- data.frame(seq(1949,2018,1), cbind(NBA))}
#Adjust column names on new data frame
names(out_NBA)[1] <- "Season.Start"
names(out_NBA)[2] <- "Transitivity.Rate"
out_NBA

#ABA

ABA <- matrix(byrow=TRUE)
for (i in seq(1967,1975,1)){
  print(i)
  ABA <- lapply(ABA, function(x)transitivity_test('ABA', i))
  out_ABA <- data.frame(seq(1967,1975,1), cbind(ABA))}
#Adjust column names on new data frame
names(out_ABA)[1] <- "Season.Start"
names(out_ABA)[2] <- "Transitivity.Rate"
out_ABA

#BAA

BAA <- matrix(byrow=TRUE)
for (i in seq(1946,1948,1)){
  print(i)
  BAA <- sapply(BAA, function(x)transitivity_test('BAA', i))
  out_BAA <- data.frame(seq(1946,1948,1), cbind(BAA))}
#Adjust column names on new data frame
names(out_BAA)[1] <- "Season.Start"
names(out_BAA)[2] <- "Transitivity.Rate"
out_BAA

### PLOT RESULTS ###

###Create plotting function with trendline
Assoc_plot <- function(league){
  ggplot(league, aes(x = Season.Start, y = Transitivity.Rate)) +
  geom_point() +
  scale_y_continuous(limits = c(0.0, 0.3)) +
  geom_smooth(method = 'lm')}

#Plot each association
Assoc_plot(out_NBA)
Assoc_plot(out_ABA)
Assoc_plot(out_BAA)
