---
layout: post
title: Hands on Machine Learning
---

# Preface

"Deep Learning" is a technique abandoned on 1990s.

## Objective and Approach

Use production-ready python frameworks:

* Scikit-Learn
* TensorFlow

## Prerequisites

1. Programing skills: python and main scientific libraries:
    * Numpy
    * Pandas
    * Matplotlib
2. Mathematics of collage level
    * calculus
    * linear algebra
    * probabilities
    * statistics

## Other resources

1. Online courses
    * [ML course on Coursera](https://www.coursera.org/learn/machine-learning/)
    * [Course on neural networks and Deep Learning](https://www.coursera.org/course/neuralnets)
2. Websites
    * [Scikit-Learn’s exceptional User Guide](http://scikit-learn.org/stable/user_guide.html)
    * [dataquest](https://www.dataquest.io/)
    * [deeplearning.net](http://deeplearning.net/)
3. Books
    * Joel Grus, Data Science from Scratch
    * Stephen Marsland, Machine Learning: An Algorithmic Perspective (Chapman and Hall)
    * Sebastian Raschka, Python Machine Learning (Packt Publishing)
    * Yaser S. Abu-Mostafa, Malik Magdon-Ismail, and Hsuan-Tien Lin, Learning from Data (AMLBook)
    * Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 3rd Edition (Pearson)
4. [Kaggle.com](https://www.kaggle.com/)

------------

# The Machine Learning Landscape -- CH01

## What Is Machine Learning

With training data $E$, and the task $T$, with good enough performancd $P$.

## Why Use Machine Learning

Replace manually managed *Rules* with *Model* learnd from data.

## Types of Machine Learning Systems

### Supervised/Unsupervised Learning

If the training data set is tagged.

* Tagged: Supervised learning
* Untagged: Unsupervised learning
* A little subset of the data is tagged: Semisupervised learning
* With out tagged data, but with policy to get the most reward

### Batch and Online Learning

* Batch learning
    1. the system not support incremental learning
* Online learning
    1. can learn from streaming data

### Instance-Based Versus Model-Based Learning

Machine Learning models are different by the way of *generalize*

#### Instance-based learning

Learn from similarity from *tagged data*

#### Model-based learning

Predict result by the trained model

Simple linear model:

$\text{life_satisfaction} = \theta_0 + \theta_1 \mul \text{GDP_per_capita}$

Train and predict with Linear Regression model:

``` python
model = LinearRegression()
model.fit(X_train, y)
model.predict(X_test)
```

The working process of a machine learning:

* You study the data
* You select a model
* Train the model with training data
* Test the model with test data

## Main Challenges of Machine Learning

* Insufficient Quantity of Training Data
  * You need a lot of data on problems, even the problem is simple
  * Models works identically well if there are enough data, Data set size is so important
* Nonrepresentative Training Data
  * Data sample is very important when you need for the model to generalize to other data
* Poor-Quality Data
  * errors
  * outliers
  * noise
* Irrelevant Features
  * garbage in, garbage out
  * feature engineering
    * feature selection: select relevant feature
    * feature extraction: create new feature from exists one
    * gather data to create new features
* Overfitting the Training Data
  * data set is too sample, and the model overfit to the training data and can't generalize to other data
  * overfiting happens when the model is too complex to the noise and the amount of data
  * Constraining a model to make it simpler and reduce the risk of overfitting is called *regularization*, reduce the degrees of freedom
* Underfitting the Training Data
  * model is too simple to learn the data set

## Testing and Validating

The most important of a model training is to generalize to other data than the training data.

Seprate your data into training and testing data.

Compare the training error and test error, you can decide that if the model is overfitting.

Then you may optimize the model by choose best hyperparameters to reduce the testing error. But you may get a higher error on product, because your model is in a way trained for the testdata.

Then you need a validation set, for validate the model.

Or you can train and validate the model on the same test data set seprate into two pieces. when the model and hyperparameters is selected, train the model on the test data set, and test on the test data.

*A model is a simplified version of the observations. The simplifications are meant to discard the superfluous details that are unlikely to generalize to new instances.*

model parameter: properites of data passed to the model
hyperparameter: the properties about the model

# End-to-End Machine Learning Project -- CH02

The process of real learning project.

1. Frame the problem and look at the big picture.
2. Get the data.
3. Explore the data to gain insights.
4. Prepare the data to better expose the underlying data patterns to Machine Learning algorithms.
5. Explore many different models and short-list the best ones.
6. Fine-tune your models and combine them into a great solution.
7. Present your solution.
8. Launch, monitor, and maintain your system.

## Working with Real Data

it is best to actually experiment with real-world data, not just artificial datasets.

## Look at the Big Picture

Get the basic information of problem, data, task.

### Frame the Problem

* The first question is the task, for a company: the bussiness objective.
    1. A sequence of data processing components is called a data pipeline. Components typically run asynchronously. The interface between components is simply the data store.
* The next question to ask is what the current solution looks like.
    1. How the task is processed.

### Select a Performance Measure

*RMSE* measures the standard deviation4 of the errors the system makes in its predictions.

$$\mathbf{RMSE}(\mathbf{X},h) = \sqrt{ {1 \over m} \sum_{i=1}^m \left( h \left( \mathbf{X} ^ {(i)} \right) - y ^{(i)} \right) }$$

*Mean Absolute Error* (also called the Average Absolute Deviation:

$$\mathbf{MAE}(\mathbf{X},h) = { {1 \over m} \sum_{i=1}^m \lvert h \left( \mathbf{x} ^ {(i)} \right) - y ^{(i)} \rvert }$$

Various distance measures, or norms, are possible:

* Computing the root of a sum of squares (*RMSE*) corresponds to the *Euclidian norm*
    1. $\ell_2 \text{norm}$
    1. $\left\lVert \cdot \right\rVert_2$ or just $\left\lVert \cdot \right\rVert$
* Computing the sum of absolutes (MAE), Manhattan norm
    1. $\ell_1 \text{norm}$
    1. $\left\lVert \cdot \right\rVert_1$
* $\ell_k \text{norm}$ for a vector $\mathbf{v}$ contains n elements is defined as:
    1. $$ \left\lVert \mathbf{v} \right\rVert_k = \left( {\lvert v_0 \rvert}^k + {\lvert v_1 \rvert}^k + \cdots + {\lvert v_n \rvert}^k \right) ^{1 \over k} $$ 
* The higher the norm index, the more it focuses on large values and neglects small ones.

### Check the Assumptions

Lastly, it is good practice to list and verify the assumptions that were made so far

## Get the Data

### Create the Workspace

Install python and other libs:

``` bash
pip3 install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn
```

### Download the Data

Create a function for fetch the data, and a function to load the data as a pandas dataframe.

### Take a Quick Look at the Data Structure

View the data set with: head(), info(), describe(). and plot the data with pandas.hist().

### Create a Test Set

Split the data into two parts: train(80%) & test(20%).

``` python
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
```

Your sampling may introduce a a significant sampling bias when the size of your data set is small. And you may want to perform a stratified sampling.

If one feature of your data set is really important, you can create a category by the feature. You can use the `StratifiedShuffleSplit` class to split the dataset.

## Discover and Visualize the Data to Gain Insights

Get more information about the *training* data.

### Visualizing Geographical Data

You can plot the geographical as a scatterplot:

`housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)`

### Looking for Correlations

Since the dataset is not too large, you can easily compute the *standard correlation coefficient*

`corr_matrix = housing.corr()`

correlation coefficient ranges from –1 to 1:

    *  1: strong positive correlation
    * -1: strong negative correlation
    *  0: no linear correlation

Another way to check for correlation between attributes is to use Pandas’ `scatter_matrix` function.

### Experimenting with Attribute Combinations

Features may have a tail-heavy distribution, and can be transform with the logarithm.

And combine features to get more reasonable feature is also a good practice.

``` python
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]
```

## Prepare the Data for Machine Learning Algorithms

Seprate the label with the rest of the dataset.

### Data Cleaning

There may be some missing values, and we can:

* drop the corresponding sample: `dropna()`
* drop the feature: `drop()`
* set the missing value to some default values: `fillna()`

Or you can use a `imputer` to fit and transform the data:

``` python
imputer.fit(housing_num)
X = imputer.transform(housing_num)
```

### Handling Text and Categorical Attributes

Machine Learning algorithms prefer to work with numbers. Scikit-Learn provides a transformer for this task called `LabelEncoder`:

`LabelEncoder` convert these text labels to numbers, but categories are not closer to near label than to remote label.

Scikit-Learn provides a `OneHotEncoder` encoder to convert integer categorical values into one-hot vectors.

### Custom Transformers

You can inherit `BaseEstimator` and implement: `fit()`, `transform()` and `fit_transform()` function, and you get two extra methods: `get_params()` and `set_params()`.

### Feature Scaling

Machine Learning algorithms don’t perform well when the input numerical attributes have very different scales.

There are two common ways to get all attributes to have the same scale:

* min-max scaling: `MinMaxScaler` and
* standardization: `StandardScaler`

### Transformation Pipelines

Scikit-Learn provides the `Pipeline` class to help with such sequences of transformations.

The Pipeline constructor takes a list of *name*/*estimator* pairs defining a sequence of steps. *All but the last* estimator must be *transformers* (i.e., they must have a `fit_transform()` method)

`FeatureUnion` combine two pipeline deal with different type of features together, features can select with `DataFrameSelector`

``` python
from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    ``` Takes a pandas dataframe, select desired attributes, convert to numpy array ```
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values
```

## Select and Train a Model

After you:

* framed the problem,
* got the data and explored it,
* sampled a training set and a test set,
* wrote a transformation pipelines to clean up and prepare data.

You are ready to select and train a Machine Learning model.

### Training and Evaluating on the Training Set

``` python
from sklearn.linear_model import LinearRegression lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
```

`LinearRegression` model generate result with great *MSE*, and `DecisionTreeRegressor` overfit badly to the traning data set.

### Better Evaluation Using Cross-Validation

``` python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)
```

### Fine-Tune Your Model

#### Grid Search

*Scikit-Learn*’s `GridSearchCV` to search for you. You can find hyperparameters combination automatically.

``` python
from sklearn.model_selection import GridSearchCV
param_grid = [
  {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
  {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(housing_prepared, housing_labels)
```

`GridSearchCV` will try every combination and get the best: `grid_search.best_params_`.

#### Randomized Search

If the hyperparameter *search space* is large, you may want use `RandomizedSearchCV`.

#### Ensemble Methods

Another way to fine-tune your system is to try to combine the models that perform best.

#### Analyze the Best Models and Their Errors

You will often gain good insights on the problem by inspecting the best models.

`RandomForestRegressor` can indicate the relative importance of each attribute for making accurate predictions:

``` python
grid_search.best_estimator_.feature_importances_
```

#### Evaluate Your System on the Test Set

After you get a sufficiently good model, you may evaluate the final model on the test set.

``` python
final_model = grid_search.best_estimator_
X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()
X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)
    final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
```

After a lot of tuning of cross validation, the performance of the model will be slightly worse than what you measured using cross- validation.

The project then come to the pre-launch phase. You need to present your solution:

1. Highlight what you have learned.
1. What worked, and what not.
1. What assumptions have been make.
1. What your system's limitations are.

Document everything, create nice presentations with clear visualizations and easy-to-remember statements.

### Launch, Monitor, and Maintain Your System

1. Plug the production input data sources to you system, and write the test.
1. Write code to monitor the system, trigger alert when the system drops.
1. Evaluate your system's performance by sampling the predict and evaluate them.
1. Evaluate and monitor the input data quality.
1. Generally refresh the model on a regular basis using fresh data.

## Try it out

The process of the machine learning project need a lot of work: prepare, monitor, evaluate, automating the model training.


# Classification

## MNIST

70,000 labeled image of handwriting digitals.

``` python
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
X, y = mnist["data"], mnist["target"]

```



