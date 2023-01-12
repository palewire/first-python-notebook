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

# Totals

In some ways, your database is no different from a human source. Getting a good story requires careful, thorough questioning.

In this section we will use pandas to interview our data as we continue our quest to find out the biggest donors for and against Proposition 64.

## Sum a column

Using tricks we learned as far back as [chapter two](pandas.md), we can start off by answering a simple question: What is the total sum of Proposition 64 contributions that have been reported?

To answer that let’s start by getting our hands on `amount`, the column from the contributions DataFrame with numbers in it. We can do that just as we did with other columns earlier.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
```

```{code-cell}
merged_prop.amount
```

Now we can add up the column's total using the pandas method [sum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sum.html), just as we did when we were first getting started.

```{code-cell}
merged_prop.amount.sum()
```

We've completed our first piece of analysis and discovered the total amount spent on this proposition. Time to run off to Twitter and publish our results to the world, right?

Wrong.

## How to not be wrong

The total we generated is not the overall total raised in the campaign, and it is guaranteed to be lower than the totals reported in the media and by the campaigns.

Why?

In California, campaigns are [only required](http://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p10) to disclose the names of donors who give over \$100, so our data is missing all of the donors who gave less than that amount.

The cutoff varies, and there are some exceptions, but the same thing is true in other states and also at the federal level in races for Congress and the White House.

The overall totals are instead reported on cover sheets included with disclosure reports that lump together all the smaller contributions as part of a grand total. Those are the records most commonly cited to total up a campaign's fundraising.

The result is that an itemized list of contributions, like the one we have, cannot be used to calculate a grand total. That's true in California and virtually anywhere else you work with campaign data. Overlooking that limitation is a rookie mistake routinely made by analysts new to this field.

But that doesn't mean our data are worthless. We just have to use our list responsibly. In many cases, professional campaign reporters will refer to an analysis like ours as applying only to "large donors."

Since large donors typically account for most of the money, the results are still significant. And the high level of detail included in each record — like the donor's name, employer and occupation — makes the limitations worth working through.

## Which side raised more?

Adding up a big total is all well and good. But we're aiming for something more nuanced.

We want to separate the money spent supporting the proposition from the money opposing it. Then we want to find out which side raised more.

To answer that question, let's return to the filtering technique we learned in [chapter seven](filters.md). Let's look at the column we're going to filter by, `committee_position`.

```{code-cell}
merged_prop.committee_position.value_counts()
```

Filter our `merged_prop` table down using that column and the pandas filtering method that combines a column, an operator and the value we want to filter by. Let's stick the result in a variable.

```{code-cell}
support = merged_prop[merged_prop.committee_position == 'SUPPORT']
```

Repeat all that for opposing contributions. First the filter into a new variable.

```{code-cell}
oppose = merged_prop[merged_prop.committee_position == 'OPPOSE']
```

Sum up the total disclosed contributions to each for comparison. First the opposition.

```{code-cell}
oppose.amount.sum()
```

Then the supporters.

```{code-cell}
support.amount.sum()
```

The support is clearly larger. But what percent is it of the overall disclosed total? We can find out by combining two `sum` calculations using Python’s built-in division operator.

```{code-cell}
support.amount.sum() / merged_prop.amount.sum()
```
