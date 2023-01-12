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

# Filter

The most common way to filter a DataFrame is to pass an expression as an “index” that can be used to decide which records should be kept and which discarded. You write the expression by combining a column on your DataFrame with an “operator” like `==` or `>` or `<` and a value to compare against each row.

```{note}
If you are familiar with writing [SQL](https://en.wikipedia.org/wiki/SQL) to manipulate databases, pandas’ filtering system is somewhat similar to a WHERE query. The [official pandas documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where) offers direct translations between the two.
```

Let's try filtering against the `state` field. Save a postal code into a variable. This will allow us to reuse it later.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
```

```{code-cell}
:tags: [hide-output,show-input]
my_state = "IA"
```

In the next cell we will ask pandas to narrow down our list of accidents to just those in the state we’re interested in. We will create a filter expression and place it between two flat brackets following the DataFrame we wish to filter.

```{code-cell}
:tags: [hide-output,show-input]
accident_list[accident_list.state == my_state]
```

Now we should save the results of that filter into a new variable separate from the full list we imported from the CSV file. Since it includes only the sites for the state we want, let’s call it `my_accidents`.

```{code-cell}
:tags: [hide-output,show-input]
my_accidents = accident_list[accident_list.state == my_state]
```

To check our work and find out how many committees are left after the filter, let's run the DataFrame inspection commands we learned earlier.

First `head`.

```{code-cell}
:tags: [hide-output,show-input]
my_accidents.head()
```

Then `info`.

```{code-cell}
:tags: [hide-output,show-input]
my_accidents.info()
```

Now pick another state and try running the code again. See if you can write filters that will answer the following questions:

1. Which state recorded more accidents, Iowa or Missouri?
2. How many accidents reported more than one fatality?
3. How many accidents happened in California in 2015?
