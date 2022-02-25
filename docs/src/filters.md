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

# Filters

```{contents} Sections
  :depth: 1
  :local:
```

## Our next mission

Until November 2016, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved Proposition 64, which asked if the practice ought to be legalized.

A yes vote supported legalization. A no vote opposed it. [In the final tally](http://elections.cdn.sos.ca.gov/sov/2016-general/sov/65-ballot-measures-formatted.pdf), 57% of voters said yes.

Our next mission is to use the DataFrames containing campaign committees and contributors to figure out the biggest donors both for and against the measure.

To do that, the first thing we need to do is isolate the fundraising committees active on Proposition 64, which are now buried among of the list of more than 100 groups active last November.

## Filter a DataFrame

The most common way to filter a DataFrame is to pass an expression as an "index" that can be used to decide which records should be kept and which discarded.

You write the expression by combining a column on your DataFrame with an ["operator"](https://en.wikipedia.org/wiki/Operator_(computer_programming)) like `==` or `>` or `<` and a value to compare against each row.

```{note}
If you are familiar with writing [SQL](https://en.wikipedia.org/wiki/SQL) to manipulate databases, pandas' filtering system is somewhat similar to a `WHERE` query. The [official pandas documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where) offers direct translations between the two.
```

In our case, the column we want to filter against is `prop_name`. We only want to keep those records where the value there matches the full name of Proposition 64.

Where do we get that? Our friend `value_counts`.

Running the ``value_counts`` method to spit out the full name of all 17 measures.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
```

```{code-cell}
committee_list.prop_name.value_counts()
```

From that result we can copy the full name of the proposition and place it between quotation marks in a variable in a new cell. This will allow us to reuse it later.

```{code-cell}
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
```

In the next cell we will ask pandas to narrow down our list of committees to just those that match the proposition we're interested in. We will create a filter expression and place it between two flat brackets following the DataFrame we wish to filter.

```{code-cell}
committee_list[committee_list.prop_name == my_prop]
```

Run it and it outputs the filtered dataset, just those committees active on Proposition 64.

## Inspect the results

Now we should save the results of that filter into a new variable separate from the full list we imported from the CSV file.

Since it includes only the committees for the proposition we’re interested in let’s call it `my_committees`.

```{code-cell}
my_committees = committee_list[committee_list.prop_name == my_prop]
```

To check our work and find out how many committees are left after the filter, let's run the DataFrame inspection commands we learned earlier.

First `head`.

```{code-cell}
my_committees.head()
```

Then `info`.

```{code-cell}
my_committees.info()
```