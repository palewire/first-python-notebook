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

This chapter will show how you can create a new column based on the data in other columns, a process sometimes known as "computing."

```{contents} Sections
  :depth: 1
  :local:
```

```{code-cell}
:tags: [hide-cell]

import warnings
warnings.simplefilter("ignore")
import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
my_committees = committee_list[committee_list.prop_name == my_prop]
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
support = merged_prop[merged_prop.committee_position == 'SUPPORT']
oppose = merged_prop[merged_prop.committee_position == 'OPPOSE']
```

## Create a column

Let's say we wanted to take an extra step beyond last chapter to learn which side got more money from outside of California.

As before, we could start by adding the `contributor_state` column to the `groupby` statement.

```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname", "contributor_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

We could try grouping by state alone instead, to get a better sense of it.

```{code-cell}
merged_prop.groupby("contributor_state", dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Or we could filter to just California donors.

```{code-cell}
merged_prop[merged_prop["contributor_state"] == "CA"]["amount"].sum()
```

And then filter again to those outside of California.

```{code-cell}
merged_prop[merged_prop["contributor_state"] != "CA"]["amount"].sum()
```

Each one of these methods has its place. But to advance to another level of sophistication, and to simplify our code, it’s often helpful to create a new column that stores values calculated off other fields. Then we can group by the new column to get the answers we’re after.

There are a few ways to achieve this. We're going to start with an expression that tests the `contributor_state` field and returns true or false, much like the ones we’ve used before in filters.

```{code-cell}
merged_prop["in_state"] = merged_prop.contributor_state == "CA"
```

This basically says, "Create a new column name `in_state` using `contributor_state` as the basis. When a row in `contributor_state` equals `CA`, that means `in_state` should be `True`. In all other circumstances, `in_state` will equal `False`."

Now, we can see our new column in the DataFrame. It will show up on the far right of the table.

```{code-cell}
merged_prop.head()
```

## Analyze with `groupby`

Let’s use our `groupby` and `sum` method on the `in_state` flag.

```{code-cell}
merged_prop.groupby("in_state", dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

```{note}
Notice that these totals match the totals that we calculated with the filtered calculations above. That's good! This is one way to verify your new column. If your totals don’t match, it means you should go back and doublecheck your conditional statement that’s creating the new column.
```

Let’s do a little more. We can now create a new DataFrame for just in-state donors.

```{code-cell}
in_state = merged_prop[merged_prop.in_state == True]
```

And check the overall proportion of funding that came from inside the state.

```{code-cell}
in_state.amount.sum() / merged_prop.amount.sum()
```

We can also easily create ranked lists of the top donors from within the state.

```{code-cell}
in_state.groupby(["contributor_firstname", "contributor_lastname"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

And do the same the for those outside the state. First by making a DataFrame.

```{code-cell}
out_state = merged_prop[merged_prop.in_state == False]
```

Then by swapping our new variable into the line of code above.

```{code-cell}
out_state.groupby(["contributor_firstname", "contributor_lastname"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```
