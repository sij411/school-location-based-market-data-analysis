"""
    draw bar, pie charts
"""
import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

def bar_plot(df, var_name):
    """
        input: df(dataframe), var_name ex: "Sex", rotation: rotate x ticks
        output: bar plot & value count
    """
    # get feature
    # var_name = 'Sex'
    var = df[var_name]
    var_val = var.value_counts()
    
    # visualize
    plt.figure(figsize = (9,3))
    plt.bar(var_val.index, var_val)
    plt.xticks(var_val.index, var_val.index.values)
    
    plt.xticks(rotation=45, ha="right")
        
    plt.ylabel("Frequency")
    plt.title(var_name)
    plt.show()
    print("{}: \n {}".format(var_name,var_val))


def pie_plot(df, var_name):
    """
           input: df(dataframe), var_name ex: "Sex", rotation: rotate x ticks
           output: bar plot & value count
    """
    col_sums = df[var_name].sum(axis=0)  # column sum
    print(f"Column sum of {var_name}")
    print(col_sums)
    col_sums.plot(labels=col_sums.index, autopct='%1.1f%%', kind='pie')

def barh_plot(df, var_name):
    col_sums = df[var_name].value_counts()  # column sum
    print("Value counts examples")
    display(col_sums)
    col_sums.plot(kind="barh", figsize=(20, 20))
