###REGRESSION Of Real against reference Permuted Data

all_assoc$Season.Start <- as.numeric(rownames(all_assoc))
all_assoc[68:75, 7] <- c(as.numeric(1967:1974))
all_assoc[79:100,7] <- c(as.numeric(1997:2018))

all_assoc$NBA <- ifelse(all_assoc$Assoc == 'NBA', 1, 0)
all_assoc$ABA <- ifelse(all_assoc$Assoc == 'ABA', 1, 0)
all_assoc$BAA <- ifelse(all_assoc$Assoc == 'BAA', 1, 0)
all_assoc$WNBA <- ifelse(all_assoc$Assoc == 'WNBA', 1, 0)
summary(all_assoc)


#Is there a stastically significant difference between the real and permuted data?
regress_control <- function(league){
  ## Set up variables
  Diff <- league$TVR.Diff
  Season <- league$Season.num
  NBA <- league$NBA
  ABA <- league$ABA
  BAA <- league$BAA
  WNBA <- league$WNBA

  ##Run linear regression models and summarize
  ##NBA as reference
  lm.TVRs <- lm(Diff ~ Season + ABA + BAA + WNBA)
  summary(lm.TVRs)

}
##Apply model
regress_control(all_assoc)
