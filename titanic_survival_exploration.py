# -*- coding:utf-8 -*-

import pandas as pd
from IPython.display import display  # Allows the use of display() for DataFrames


# Import supplementary visualizations code visuals.py
# import visuals as vs


def get_data(show=False):
    # Pretty display for notebooks
    # matplotlib  inline

    # Load the dataset
    in_file = 'titanic_data.csv'
    full_data = pd.read_csv(in_file)

    # Print the first few entries of the RMS Titanic data
    if show:
        display(full_data.head())

    outcomes = full_data['Survived']
    data = full_data.drop('Survived', axis=1)

    # Show the new dataset with 'Survived' removed
    if show:
        display(data.head())

    return [outcomes, data]


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"


# predictions function list
def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """
    predictions = []
    for _, passenger in data.iterrows():
        # Predict the survival of 'passenger'
        predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


def predictions_1(data):
    """ Model with one feature:
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here

        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


def predictions_2(data):
    """ Model with two features:
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here

        if passenger['Sex'] == 'female' or (passenger['Sex'] == 'male' and float(passenger['Age']) <= 10):
            predictions.append(1)
        else:
            predictions.append(0)

    print len(predictions)
    # Return our predictions
    return pd.Series(predictions)


def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """

    predictions = []
    for _, passenger in data.iterrows():
        # Remove the 'pass' statement below
        # and write your prediction conditions here

        if (passenger['Fare'] >= 500 or
                (passenger['Sex'] == 'female' and passenger['SibSp'] < 3) or \
                    (passenger['Sex'] == 'male' and float(passenger['Age']) <= 10) or \
                    (passenger['Sex'] == 'male' and float(passenger['Age']) > 10 and float(passenger['Age']) < 20 and int(
                        passenger['Pclass']) == 1)):

            predictions.append(1)
        else:
            predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)


def test_predictions_0():
    outcomes, data = get_data(True)
    predictions = predictions_0(data)
    print accuracy_score(outcomes, predictions)


def test_predictions_1():
    outcomes, data = get_data()
    predictions = predictions_1(data)
    # vs.survival_stats(data, outcomes, 'Sex')

    print accuracy_score(outcomes, predictions)


def test_predictions_2():
    outcomes, data = get_data()
    predictions = predictions_2(data)
    # survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])

    print accuracy_score(outcomes, predictions)


def test_predictions_3():
    outcomes, data = get_data()
    predictions = predictions_3(data)
    # vs.survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Age < 18"])
    print accuracy_score(outcomes, predictions)


def main():
    # Make the predictions
    test_predictions_3()


if __name__ == '__main__':
    main()

'''

针对日益严重的空气污染问题，可以从肺癌患者样本集进行分析，其中有影响的数据集有
1. 是否吸烟
2. 居住城市
3. 性别
4. 年龄

结合各大城市环境污染情况，推测居住城市和肺癌关联较大
'''
