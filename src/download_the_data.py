
import os
import tarfile
import hashlib
import pandas as pd
import numpy as np
from six.moves import urllib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.base import BaseEstimator, TransformerMixin

import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    ``` Takes a pandas dataframe, select desired attributes, convert to numpy array ```
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio, seed=42):
    np.random.seed(seed)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]


rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):

    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


if __name__ == '__main__':
    # fetch_housing_data()
    housing = load_housing_data()
    print(housing.head())
    print(housing.info())
    print(housing["ocean_proximity"].value_counts())

    print(housing.describe())

    # housing.hist(bins=50, figsize=(20, 15))
    # plt.show()
    housing_with_id = housing.reset_index()
    # train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
    # train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
    housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
        for set in (strat_train_set, strat_test_set):
            set.drop(["income_cat"], axis=1, inplace=True)


    print(housing["income_cat"].value_counts() / len(housing))
    # train_set, test_set = split_train_test(housing, 0.2)
    # housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1, s=housing["population"]/100, label="population", c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )
    # plt.legend()
    # plt.show()

    from pandas.tools.plotting import scatter_matrix
    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
    # scatter_matrix(housing[attributes], figsize=(12, 8))
    # plt.show()

    housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
    housing["population_per_household"]=housing["population"]/housing["households"]

    housing_num = housing.drop("ocean_proximity", axis=1)

    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)

    housing_tr = pd.DataFrame(X, columns=housing_num.columns)

    # from sklearn.preprocessing import LabelEncoder
    # encoder = LabelEncoder()
    housing_cat = housing["ocean_proximity"]
    # housing_cat_encoded = encoder.fit_transform(housing_cat)

    # from sklearn.preprocessing import OneHotEncoder
    # encoder = OneHotEncoder()
    # housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))

    from sklearn.preprocessing import LabelBinarizer
    encoder = LabelBinarizer()
    housing_cat_1hot = encoder.fit_transform(housing_cat)
