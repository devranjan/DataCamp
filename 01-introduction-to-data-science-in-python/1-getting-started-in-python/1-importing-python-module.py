"""Modules (sometimes called packages or libraries) help group together related sets of tools in Python.
In this exercise, we'll examine two modules that are frequently used by Data Scientists:

    statsmodels: used in machine learning; usually aliased as sm
    seaborn: a visualization library; usually aliased as sns

Note that each module has a standard alias, which allows you to access the tools inside of the module without typing as many characters.
For example, aliasing lets us shorten seaborn.scatterplot() to sns.scatterplot().

Instructions

In the script editor, use an import statement to import statsmodels.

Add an as statement to alias statsmodels to sm.

Add an as statement to alias seaborn to sns.
"""

# Use an import statement to import statsmodels
import statsmodels

# Import statsmodels under the alias sm
import statsmodels as sm

# Use an import statement to import seaborn with alias sns
import seaborn as sns
