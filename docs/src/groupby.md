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

# Group

The [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) method allows you to group a DataFrame by a column and then calculate a sum, or any other statistic, for each unique value. This functions much like the ["pivot table"](https://en.wikipedia.org/wiki/Pivot_table) feature found in most spreadsheets.

Let's use it to total up the accidents by make and model. You start by passing the field you want to group on to the function.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
```

```{code-cell}
:tags: [hide-output,show-input]
accident_list.groupby("latimes_make_and_model")
```

A nice start but you’ll notice you don’t get much back. The data’s been grouped, but we haven’t chosen what to do with it yet. If we wanted the total by model, we would use the `size` method.

```{code-cell}
:tags: [hide-output,show-input]
accident_list.groupby("latimes_make_and_model").size()
```

The result is much like `value_counts`, but we're allowed run to all kinds of statistical operations on the group, like `sum`, `mean` and `std`. For instance, we could sum the total number of fatalities for each maker by string that field on the end followed by the statistical method.

```{code-cell}
:tags: [hide-output,show-input]
accident_list.groupby("latimes_make_and_model").total_fatalities.sum()
```

Again our data has come back as an ugly Series. To reformat it as a pretty DataFrame use the `reset_index` method again.

```{code-cell}
:tags: [hide-output,show-input]
accident_list.groupby("latimes_make_and_model").size().reset_index()
```

Now save that as a variable.

```{code-cell}
:tags: [hide-output,show-input]
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index()
```

You can clean up the `0` column name assigned by pandas with the `rename` method. The `inplace` option, found on many pandas methods, will save the change to your variable automatically.

```{code-cell}
:tags: [hide-output,show-input]
accident_counts.rename(columns={0: "accidents"}, inplace=True)
```

The result is a DataFrame with the accident totals we'll want to merge with the FAA survey data to calculate rates.

```{code-cell}
:tags: [hide-output,show-input]
accident_counts.head()
```

Now we‘ve got a ranking we can work with.