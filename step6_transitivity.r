library(dplyr)

#read data from giant csv
total <- read.csv('C:/Users/adamj/OneDrive/Documents/Writings/Work.w.Seth/data/total_data.csv')
total <- total[-c(1:5, 7:11)]


#convert points to numeric
total$vis.pts2 <- as.numeric(total$vis.pts2)
total$home.pts2 <- as.numeric(total$home.pts2)
tail(total)

#Create transitivity function to create iterability based on a given count
transitivity_test <- function(count){
  for(i in seq(1,500,1)) {
    print(i)
    if (i == count){
     break 
    }
  
  }
  
  #Separates calendar year from season year. If month number is less than 10 (October, then subtract one from given year)
  total <- total %>%
    mutate(SeasonStart = if_else(total$Month < 10, -1, 0))
    
  total$SeasonStart <- total$Year + total$SeasonStart
  
  #Randomly pick year (this needs to be modified to reflect seasons instead of calendar years)
  ran_year = sample(1946:2019, 1)
  print(ran_year)
  
  #create list of teams competing in one year
  sample_year <- total[ which(total$SeasonStart == ran_year), ]
  #sample_year
  teams <- as.character(unique(sample_year$home2))
  teams
  
  
  #pick three teams randomly
  sample1 <- sample(teams, size = 1, replace = FALSE)
  sample1
  sample2 <- sample(teams, size = 1, replace = FALSE)
  sample2
  sample3 <- sample(teams, size = 1, replace = FALSE)
  sample3
  
  #Find the boxscore results from the first sampled team
  sampled_games1 <- sample_year[ which(sample_year$home2 == sample1 | sample_year$vis2 == sample1), ]
  sampled_games1
  
  #Find the results from the first sampled team's schedule in which they faced team two
  game1 <- sampled_games1[ which(sampled_games1$home2 == sample2 | sampled_games1$vis2 == sample2), ]
  
  #Find the boxscore results from the second sampled team
  sampled_games2 <- sample_year[ which(sample_year$home2 == sample2 | sample_year$vis2 == sample2), ]
  sampled_games2
  
  #Find the results from the second sampled team's schedule in which they faced team three
  game2 <- sampled_games2[ which(sampled_games2$home2 == sample3 | sampled_games2$vis2 == sample3), ]
  game2
  
  #Find the boxscore results from the first sampled team's schedule in which they faced team three
  game3 <- sampled_games1[ which(sampled_games1$home2 == sample3 | sampled_games1$vis2 == sample3), ]
  game3
  
  
  #find random game involving two teams in same year
  random_game1 <- game1[sample(nrow(game1), 1), ]
  random_game1
  
  ####This is where it starts getting buggy...I think data format reasons
  
  #Check to make sure the two teams competed (based on length of sample). If there was a game, print winner.
  if (length(random_game1) < 12){
    print("No first game")
    if (random_game1$home > random_game1$vis2){
      winner1 <- random_game1$home
      winner1
    }else{
      winner1 <- random_game1$vis2
      winner1
    }
  }
  
  winner1
  
  #find random other game involving second set of two, print winner
  random_game2 <- game2[sample(nrow(game2), 1), ]
  
  
  if (length(random_game2) < 12){
    print("No second game")
    if (random_game2$home > random_game2$vis2){
      winner2 <- random_game2$home
    }else{
      winner2 <- random_game2$vis2
    }
  }
  print(winner2)
  
  #find random other game involving first and third team, print winner
  random_game3 <- game3[sample(nrow(game3), 1), ]
  length(random_game3)
  
  if (length(random_game3) < 12){
    print("No third game")
  }else {
    if (random_game3$home > random_game3$vis2){
      winner3 <- random_game3$home
      
    }else{
      winner3 <- random_game3$vis2
    }
  }
  
  
  winner1
  winner2
  winner3
  
  #Check to see if the winner of the first matchup also beat the third
  A <- winner1 != winner3
  #Check to see if the winner of the second matchup also beat the third
  B <- winner2 != winner3
  
  if ((A == TRUE) & (B == TRUE)){
    print('Transitivity violation')
  }
}

#Still working at making this into an iterable function
transitivity_test(500)


