# Load the dataset
library(readxl)
Airline <- read_excel(file.choose())
View(Airline)

# Removing unnecessary columns
Data <- Airline[2:12]
View(Data)
str(Data)


# Exploratory data analysis:
# 1. Measures of central tendency
# 2. Measures of dispersion
# 3. Third moment business decision
# 4. Fourth moment business decision
# 5. Probability distributions of variables 
# 6. Graphical representations (Histogram, Box plot, Dot plot, Stem & Leaf plot, Bar plot, etc.)

summary(Data)
attach(Data)

# Graphical representations (Histogram, Box plot, Dot plot, Stem & Leaf plot, Bar plot, etc.)

# Box plot Representation

boxplot(Balance, col = "orange",main = "Balance")
boxplot(Bonus_miles, col = "yellow",main = "Bonus Miles")
boxplot(Days_since_enroll, col = "dodgerblue4",main = "Days Since Enroll")
boxplot(Bonus_trans, col = "red", horizontal = T,main = "Bonus Trans")

# Histogram Representation

hist(Balance, col = "orange",main = "Balance")
hist(Bonus_miles, col = "yellow",main = "Bonus Miles")
hist(Days_since_enroll, col = "blue",main = "Days Since Enroll")
hist(Bonus_trans,col = "red", main = "Bonus Trans")


summary(Data)

# Normalize the data
normalized_data <- scale(Data[, 1:11]) # As we already removed ID column so all columns need to normalize

summary(normalized_data)

# Elbow curve to decide the k value
twss <- NULL
for (i in 2:12) {
  twss <- c(twss, kmeans(normalized_data, centers = i)$tot.withinss)
}
twss

# Look for an "elbow" in the scree plot
plot(2:12, twss, type = "b", xlab = "Number of Clusters", ylab = "Within groups sum of squares")
title(sub = "K-Means Clustering Scree-Plot")


# 3 Cluster Solution
fit <- kmeans(normalized_data, 3) 
str(fit)
fit$cluster
final <- data.frame(fit$cluster, Data) # Append cluster membership

aggregate(Data[, 1:11], by = list(fit$cluster), FUN = mean)
