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

# Sort

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/LN_P0qT5adY?si=xIG9OccCQvM2nxRw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Another simple but common technique for analyzing data is sorting. This can be useful for ranking the DataFrame to show the first and last members of the table according to a particular column.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list["per_hour"] = merged_list.accidents / merged_list.total_hours
merged_list["per_100k_hours"] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

The [`sort_values`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) method is how pandas does it. It expects you to provide it with the name of the column to sort by in quotes. Try sorting by our computed field.

```{code-cell}
:tags: [show-input]
merged_list.sort_values("per_100k_hours")
```

Note that by default `sort_values` returns the DataFrame sorted in ascending order from lowest to highest. You can show the largest values first by passing in an optional keyword argument called `ascending`. When it is set to `False`, the DataFrame is sorted in descending order.

```{code-cell}
:tags: [show-input]
merged_list.sort_values("per_100k_hours", ascending=False)
```

Congratulations. With that, you've re-created the heart of the analysis published in the Los Angeles Times and covered most of the basic skills necessary to access and analyze data with pandas.

Before we move on, here's another quiz for you. You can answer all of these questions using only tricks we've learned thus far.

1. What’s the date of the most recent fatal helicopter accident in Texas? 
2. How many fatalities occurred in Texas accidents?
3. What helicopter model logged the most flight hours? 
4. Where did the accident with the NTSB number `ERA13LA057` occur?