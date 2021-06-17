# spark.py
"""Data Science Essentials: Spark.
<Name>
<Class>
<Date>
"""


import pyspark
from pyspark.sql import SparkSession


def prob1():
    """Reads in a csv file of mathematicians and reduces it to the names
    of the female mathemticians born in the 19th century. Returns a list
    of the first 5 of these names.
    """


def prob2():
    """Reads in a csv file of mathematicians, groups the
    data by country of citizenship, counts the number of occurrences of each country,
    and returns a list of the top 5 countries and their counts.
    """


def prob3():
    """Simple sorted word count function.

    Parameters:
        file (str): text file

    Returns:
        output[:5] (list): the first five (word, count) pairs
    """


def prob4():
    """Simple Monte-Carlo routine to estimate the area of the
    unit circle (i.e. the value of pi).

    Parameters:
        partitions (int): number of partitions to run the calculation with
            (number of partitions specifies the number of nodes to use)

    Returns an estimated value of pi.
    """
