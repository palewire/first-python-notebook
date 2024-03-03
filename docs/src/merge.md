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

# Merge

Next we'll cover how to merge two DataFrames together into a combined table. Before we can do that, we need to read in a second file. We'll pull `faa-survey.csv`, which contains annual estimates of how many hours each type of helicopter was in the air. If we merge it with our accident totals, we will be able to calculate an accident rate.

We can read it in the same way as the NTSB accident list, with `read_csv`.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list['latimes_make_and_model'] = accident_list['latimes_make_and_model'].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
```

```{code-cell}
:tags: [show-input]
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
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

```{note}
You may notice something new with the `on="latimes_make_and_model"` bit above. It is what Python calls a [keyword argument](https://docs.python.org/3/glossary.html#term-argument). Keyword arguments are inputs passed to a function or method after explicitly specifying the name of the argument, followed by an equals sign.

Keyword arguments can be passed in any order, as long as the name of the argument is specified. When creating a function, they can be used to specify a default value for a parameter. For this reason, they are commonly to provide overrides of a method's out-of-the-box behavior.

The pandas documentation for [`merge`]([https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)) reveals all of the keyword options available, as well as their defaults.
```

That new DataFrame can be inspected like any other.

```{code-cell}
:tags: [show-input]
merged_list.head()
```

Gasp! There's nothing there! What happened? Let's go back and inspect the datasets we're trying to merge.

First, there were the accident counts.

```{code-cell}
:tags: [show-input]
accident_counts.head()
```

Then, there was the FAA survey dataset.

```{code-cell}
:tags: [show-input]
survey.head()
```

It looks like, even though the `latimes_make_and_model` column represents the same data in each dataset, the casing is messy in the FAA survey data. Raw data is usually messy (even if this particular example is a bit contrived). It's always important to inspect your data thoroughly and know how to clean it up before analyzing.

Since the accident counts data is more consistent (all the text is upper case), let's modify the FAA data to match. There are a handful of ways to do this, but perhaps the most straightforward is just replacing everything in the `latimes_make_and_model` column with an uppercase copy of itself.

```{code-cell}
:tags: [show-input]
survey['latimes_make_and_model'] = survey['latimes_make_and_model'].str.upper()
```

The `.str` bit casts the column values to a "string" (an object type in most coding languages that represents text), and then the `.upper()` function transforms the string to upper case.

Now, let's try merging our data again.

```{code-cell}
:tags: [show-input]
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
```

Take a peek:

```{code-cell}
:tags: [show-input]
merged_list.head()
```

By looking at the columns, you can check how many rows survived the merge, a precaution you should take every time you join two tables.

```{code-cell}
:tags: [show-input]
merged_list.info()
```

You can also verify that the DataFrame has the same number of records as there are values in `accident_totals` column. That's good; If there are no null values, that means that every record in each DataFrame found a match in the other.
