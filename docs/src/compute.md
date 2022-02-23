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

```{code-cell}
:tags: [hide-cell]

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

Let's say we wanted to take an extra step to learn whether these top contributors donate from inside the state or outside of it.

We could just add "contributor_state" to the ``groupby`` statement. 

```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname","contributor_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

But we might want to quickly sort in-state vs. out-of-state donors, or perform similar calculations, and just adding the contributor state doesn't allow us to quickly evaluate trends. Plus, adding the "state" adds two more rows to our ranking list, probably because a donor within the same organization reported their location differently across multiple donations.

We could try grouping by state alone instead, to get a better sense of it.

```{code-cell}
merged_prop.groupby(["contributor_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Or we could filter to calculate just to California, and then filter again to not California. The filter lets us check whether a statement is true (in this case, does ``contributor_state`` equal ``'CA'``). Then it performs an operation on the results.

```{code-cell}
merged_prop[merged_prop["contributor_state"] == "CA"]["amount"].sum()
```

```{code-cell}
merged_prop[merged_prop["contributor_state"] != "CA"]["amount"].sum()
```

But what if we want a quick way to group by "California" vs. "not-California," and we want to be able to refer to that later? Instead, we can use conditionals to create a new column based on whether or not a candidate is in-state. Then we can group by that column. 

There are a few ways to achieve this. We're going to use a filter to create a True/False flag, which is a Boolean data type.

```{code-cell}
merged_prop["in_state"] = merged_prop["contributor_state"] == "CA"
```

This basically says, "create a new column in merged called ``in_state``. Use ``contributor_state`` as the basis. When a row in ``contributor`` state equals the string ``CA``, that means ``in_state`` should be set to equal ``True``. In all other circumstances, ``in_state`` will equal ``False``."

Now, we can see our new column in the dataframe. It will show up on the far right if you don't specify a location.

```{code-cell}
merged_prop.head()
```

## Analyze with groupby

Let's use our earlier groupby and sum code, but group by the ``in_state`` flag instead of by the contributor's state.

```{code-cell}
merged_prop.groupby(["in_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Notice that these totals match our "California" vs. "not-California" sum totals that we calculated with the filtered calculations up above. That's good! This is one way to QA your new column. If your totals didn't match, it means you should go back and double-check the logic in your conditional statement that's creating the new column.

We can also create a new dataframe for just in-state donors.

```{code-cell}
in_state = merged_prop[merged_prop.in_state == True]
out_state = merged_prop[merged_prop.in_state == False]
```

And check what proportion of the funding came from in-state, overall.

```{code-cell}
in_state.amount.sum() / merged_prop.amount.sum()
```

We can also easily create ranked lists of the top donors from within the state and outside of the state.

```{code-cell}
in_state.groupby(["contributor_firstname", "contributor_lastname"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

```{code-cell}
out_state.groupby(["contributor_firstname", "contributor_lastname"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

You can use conditionals to create any number of similar flags, which will let you slice and dice your contributor lists to your heart's content. This can be a powerful tool to look at data from different angles, narrow an existing analysis, or answer specific reporting questions.