# Telecom_Analytics
The data provided here is from a Telecom's company assets and customer usage of those assets. The task is to determine whether this company should be bought or sold. 

The first step was to clean the data by replacing missing values and removing outliers. Univariate and multivariate analysis are done on the variables. Clustering techniques are used to group the customers into groups and the characteristics of each of the groups are studied with regard to experience and usage.

The clusters for both experience and engagement are used to calculate a satisfaction score using the euclidean distance from a given point to the cluster with the worst experience and engagement respectively. The average of the experience and engagement scores indicates the satisfaction level of a customer.

The data with the calculated satisfaction score is used to predict the level of satisfaction for customers.
