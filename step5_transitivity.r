#read data from giant csv
total <- read.csv('total_data',.csv)

#convert points to numeric
as.numeric(total$visitor.pts)
as.numeric(total$home.pts)
head(total)


#Randomly pick year (this needs to be modified to reflect seasons instead of calendar years)
ran_year = sample(2000:2019, 1)
print(ran_year)

#create list of teams competing in one year
sample_year <- total[ which(total$Year == ran_year), ]
#sample_year
teams <- as.character(unique(sample_year$home))
teams


#pick three teams randomly
sample1 <- sample(teams, size = 1, replace = FALSE)
sample1
sample2 <- sample(teams, size = 1, replace = FALSE)
sample2
sample3 <- sample(teams, size = 1, replace = FALSE)
sample3

#Find the boxscore results from the first sampled team
sampled_games1 <- sample_year[ which(sample_year$home == sample1 | sample_year$visitor == sample1), ]
#sampled_games1

#Find the results from the first sampled team's schedule in which they faced team two
game1 <- sampled_games1[ which(sampled_games1$home == sample2 | sampled_games1$visitor == sample2), ]

#Find the boxscore results from the second sampled team
sampled_games2 <- sample_year[ which(sample_year$home == sample2 | sample_year$visitor == sample2), ]
#sampled_games2

#Find the results from the second sampled team's schedule in which they faced team three
game2 <- sampled_games2[ which(sampled_games2$home == sample3 | sampled_games2$visitor == sample3), ]
#game2

#Find the boxscore results from the first sampled team's schedule in which they faced team three
game3 <- sampled_games1[ which(sampled_games1$home == sample3 | sampled_games1$visitor == sample3), ]
#game3


#find random game involving two teams in same year
random_game1 <- game1[sample(nrow(game1), 1), ]
random_game1

####This is where it starts getting buggy...I think data format reasons

#Check to make sure the two teams competed (based on length of sample). If there was a game, print winner.
if (length(random_game1) < 12){
  print("No first game")
  if (random_game1$home.pts > random_game1$visitor.pts){
    winner1 <- random_game1$home
    winner1
  }else{
    winner1 <- random_game1$visitor
    winner1
  }
}

winner1

#find random other game involving second set of two, print winner
random_game2 <- game2[sample(nrow(game2), 1), ]


if (length(random_game2) < 12){
  print("No second game")
  if (random_game2$home.pts > random_game2$visitor.pts){
    winner2 <- random_game2$home
  }else{
    winner2 <- random_game2$visitor
  }
}
print(winner2)

#find random other game involving first and third team, print winner
random_game3 <- game3[sample(nrow(game3), 1), ]
length(random_game3)

if (length(random_game3) < 12){
  print("No third game")
}else {
  if (random_game3$home.pts > random_game3$visitor.pts){
    winner3 <- random_game3$home
    
  }else{
    winner3 <- random_game3$visitor
  }
}

#NEED PROTOCOL TO CHECK TRANSITIVITY VIOLATION, still trying to work this part out.

winner1
winner2
winner3

#as long as there is repetiton, success
#if no repetition, violates transitivity
#run again

