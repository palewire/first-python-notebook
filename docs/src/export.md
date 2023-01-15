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

# Export

Saving the dataframes you’ve created to your computer requires one final pandas method. It’s [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html), an exporting companion to `read_csv`. Append it to any dataframe and provide a filepath. That's all it takes.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list['per_hour'] = merged_list.accidents / merged_list.total_hours
merged_list['per_100k_hours'] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

```{code-cell}
merged_list.to_csv("accident-rate-ranking.csv")
```

The `to_csv()` method takes several optional arguments, but the most important one is the filename argument, which is used to specify the path and name of the CSV file to be created. The `index=False` argument tells pandas to not write the index column of the DataFrame to the CSV file. You can also specify the separator used by the CSV file by passing the sep parameter. By default it's ",".


```{code-cell}
merged_list.to_csv("accident-rate-ranking.csv", index=False, sep=";")
```

This will create a CSV file without the index with semicolons as the separator between values.

And with that, you've completed “First Python Notebook.” If you have any questions or critiques, you can get involved on [our GitHub repository](https://github.com/palewire/first-python-notebook), where all of the code that powers this site is available as open source.
