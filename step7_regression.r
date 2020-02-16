###REGRESSION Of Real against reference Permuted Data

out_NBA$Season.Start <- as.numeric(rownames(out_NBA))
out_ABA$Season.Start <- as.numeric(rownames(out_ABA))
out_BAA$Season.Start <- as.numeric(rownames(out_BAA))
all_assoc$Season.Start <- as.numeric(rownames(all_assoc))
all_assoc[69:76, 6] <- c(as.numeric(1967:1974))

#Is there a stastically significant difference between the real and permuted data?
regress_control <- function(league){
  ## Set up real and control variables of means
  Real <- league$TVR
  Permuted <- league$NULL.TVR
  Season <- league$Season.Start

  ##Run linear regression models and summarize
  ##Permuted as reference. Real + Season
  lm.TVRs <- lm(Permuted ~ Real)
  summary(lm.TVRs)

}
##Apply model
regress_control(all_assoc)
regress_control(out_NBA)
regress_control(out_ABA)
regress_control(out_BAA)
