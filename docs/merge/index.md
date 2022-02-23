---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{include} _templates/nav.html
```

# Merge

Our next job is to filter down the contributions list, which includes all disclosed contributions to all proposition campaigns, to just those linked to Proposition 64.

When joining two tables together, the first step is to look carefully at the columns in each table. We can do that with the `info` command we learned earlier.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
```

First the contributions.

```{code-cell}
contrib_list.info()
```

Now compare that to the committee file.

```{code-cell}
committee_list.info()
```

You will notice that each file contains a field called `calaccess_committee_id` . That’s because these two files are drawn from a ["relational database"](https://en.wikipedia.org/wiki/Relational_database) that stores data in an array of tables linked together by common identifiers. In this case, the unique identifying codes of committees in one table can be expected to match those found in another.

We can therefore safely join the two files using the pandas [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) method.

```{note}
If you are familar with traditional databases, you may recognize that the merge method in pandas is similar to SQL's `JOIN` statement. If you dig into [merge's documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) you will see it has many of the same options.
```

## Merging DataFrames

That's exactly what we want to do. So let’s try it.

Merging two DataFrames is as simple as passing both to pandas built-in merge method and specifying which field we'd like to use to connect them together. We will save the result into another new variable, `merge_everything`.

```{code-cell}
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
```

That new DataFrame variable can be inspected like any other.

```{code-cell}
merged_everything.head()
```

By looking at the columns you can check how many rows survived the merge.

```{code-cell}
merged_everything.info()
```

You can also see that the DataFrame now contains all of the columns in both tables. Columns with the same name have had a suffix automatically appended to indicate whether they came from the first or second DataFrame submitted to the merge.

## Filtering to a single proposition

The combined table now joins all contributions to all committees. To zero on just the contributions to committees in the contest over Proposition 64, we’ll need to filter out data, much like we did in the last chapter. Only this time, we'll filter our new `merged` DataFrame instead.

```{code-cell}
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
```

We have now created a new dataset that includes only contributions supporting and opposing Proposition 64.

```{code-cell}
merged_prop.info()
```

We're ready to move on from preparing our data. It's time to interview it.
