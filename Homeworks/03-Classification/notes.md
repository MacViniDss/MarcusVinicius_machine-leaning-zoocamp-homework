

 Churn rate: Difference between global mean of the target variable and mean of the target variable for categories of a feature. If this difference is greater than 0, it means that the category is less likely to churn, and if the difference is lower than 0, the group is more likely to churn. The larger differences are indicators that a variable is more important than others.
 
 Risk ratio: Ratio between mean of the target variable for categories of a feature and global mean of the target variable. If this ratio is greater than 1, the category is more likely to churn, and if the ratio is lower than 1, the category is less likely to churn. It expresses the feature importance in relative terms.

 Mutual information: Concept from information theory, wich measure how much we can learn about one variable if we know the value of other one. It's a measure of the importance of a categorical variable.

 Correlation: Measures the degree of dependency between two variables.

 One-Hot Encoding allows encoding categorical variables in numerical ones. This method represents each category of a variable as one column, and a 1 is assigned if the value belongs to the category or 0 otherwise.


    df[x].to_dict(orient='records') - convert x series to dictionaries, oriented by rows.
    DictVectorizer().fit_transform(x) - Scikit-Learn class for one-hot encoding by converting x dictionaries into a sparse matrix. It does not affect the numerical variables.
    DictVectorizer().get_feature_names() - return the names of the columns in the sparse matrix.

Logistic regression is similar to linear regression because both models take into account the bias term and weighted sum of features. The difference between these models is that the output of linear regression is a real number, while logistic regression outputs a value between zero and one, applying the sigmoid function to the linear regression formula.

g ( x i ) = S i g m o i d ( w 0 + w 1 x 1 + w 2 x 2 + . . . + w n x n )

S i g m o i d ( z ) = 1 1 + e x p ( − z )

In this way, the sigmoid function allows transforming a score into a probability.

