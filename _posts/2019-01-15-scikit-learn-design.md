---
layout: post
title: Scikit-Learn Design
date: 2019-01-15 00:12 +0800
---

Scikit-Learn’s API is remarkably well designed. The main design principles are:

# Consistency

All objects share a consistent and simple interface:

## Estimators

Any object that can estimate some parameters based on a dataset is called an *estimator* (e.g., an `imputer` is an *estimator*). The estimation itself is performed by the `fit()` method, and it takes only a dataset as a parameter (or two for supervised learning algorithms; the second dataset contains the labels). Any other parameter needed to guide the estimation process is con‐ sidered a hyperparameter (such as an imputer’s strategy), and it must be set as an instance variable (generally via a constructor parameter).

## Transformers

Some estimators (such as an *imputer*) can also transform a dataset; these are called *transformers*. Once again, the API is quite simple: the transformation is performed by the transform() method with the dataset to transform as a parameter. It returns the transformed dataset. This transforma‐ tion generally relies on the learned parameters, as is the case for an imputer. All transformers also have a convenience method called `fit_transform()` that is equivalent to calling `fit()` and then `transform()` (but sometimes `fit_transform()` is optimized and runs much faster).

## Predictors

Finally, some *estimators* are capable of making predictions given a dataset; they are called predictors. For example, the `LinearRegression` model in the previous chapter was a predictor: it predicted life satisfaction given a country’s GDP per capita. A predictor has a `predict()` method that takes a dataset of new instances and returns a dataset of corresponding predictions. It also has a `score()` method that measures the quality of the predictions given a test set (and the corresponding labels in the case of supervised learning algorithms).

# Inspection

All the estimator’s hyperparameters are accessible directly via public instance variables (e.g., `imputer.strategy`), and all the estimator’s learned parameters are also accessible via public instance variables with an underscore suffix (e.g., `imputer.statistics_`).

# Nonproliferation of classes

Datasets are represented as *NumPy* arrays or *SciPy* sparse matrices, instead of homemade classes. Hyperparameters are just regular Python strings or numbers.

# Composition

Existing building blocks are reused as much as possible. For example, it is easy to create a `Pipeline` estimator from an arbitrary sequence of transformers followed by a final estimator, as we will see.

# Sensible defaults

Scikit-Learn provides reasonable default values for most parameters, making it easy to create a baseline working system quickly.