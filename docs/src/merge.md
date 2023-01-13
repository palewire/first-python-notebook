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

```{include} ./_templates/nav.html
```

# Merge

Next we'll cover how to merge two DataFrames together into a combined table. Before we can do that, we need to read in a second file. We'll pull `faa-survey.csv`, which contains annual estimates of how many hours each type of helicopter was in the air. If we merge it with our accident totals, we will be able to calculate an accident rate.

We can read it in the same way as the NTSB accident list, with `read_csv`.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
```

```{code-cell}
:tags: [show-input]
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/faa-survey.csv")
```

Before you do anything, take a peek at it with with the `head`.

```{code-cell}
:tags: [show-input]
survey.head()
```

When joining two tables together, the first step is to look carefully at the columns in each table to find a common column that can be joined. We can do that with the `info` command we learned earlier.

```{code-cell}
:tags: [show-input]
accident_counts.info()
```

```{code-cell}
:tags: [show-input]
survey.info()
```

You can see that each table contains the `latimes_make_and_model` column. We can therefore join the two files using that column with the pandas [`merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) method.

```{note}
If you are familar with traditional databases, you may recognize that the merge method in pandas is similar to [SQL’s JOIN statement](https://en.wikipedia.org/wiki/Join_(SQL)). If you dig into [merge’s documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) you will see it has many of the same options.
```

Merging two DataFrames is as simple as passing both to pandas built-in `merge` method and specifying which field we’d like to use to connect them together. We will save the result into another new variable, which I'm going to call `merged_list`.

```{code-cell}
:tags: [show-input]
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
```

That new DataFrame can be inspected like any other.

```{code-cell}
:tags: [show-input]
merged_list.head()
```

By looking at the columns you can check how many rows survived the merge, a precaution you should take every time you join two tables.

```{code-cell}
:tags: [show-input]
merged_list.info()
```

You can also verify that the DataFrame has the same number of records as there are values in `accident_totals` column. That's good; If there are no null values, that means that every record in each DataFrame found a match in the other.