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

# Compute

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/faa-survey.csv")
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
```

The calculate an accident rate, we'll need to create a new column based on the data in other columns, a process sometimes known as “computing.”

In many cases, it’s no more complicated than combining two series using a mathematical operator. That's true in this case, where our goal is to divide the total number of accidents in each row into the total hours. That can accomplished with the following:

```{code-cell}
:tags: [hide-output,show-input]
merged_list.accidents / merged_list.total_hours
```

The resulting series can be added to your dataframe by assigning it to a new column. You name your column by providing it as a quoted string inside of flat brackets. Let's call this column something brief and clear like `per_hour`.

```{code-cell}
:tags: [hide-output,show-input]
merged_list['per_hour'] = merged_list.accidents / merged_list.total_hours
```

Which, like everything else, you can inspect with the `head` command.

```{code-cell}
:tags: [hide-output,show-input]
merged_list.head()
```

You can see that the result is in [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation). As is common when calculating per capita statistics, you can multiple all results by a common number to make the numbers more legible. That's as easy as tacking on the multiplication at the end of a computation. Here we'll use 100,000.

```{code-cell}
:tags: [hide-output,show-input]
merged_list['per_100k_hours'] = (merged_list.accidents / merged_list.total_hours) * 100_000
```