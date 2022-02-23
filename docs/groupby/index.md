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

```{include} _templates/nav.html
```

# Groupby

To take the next step towards ranking the top contributors, we'll need to learn a new trick.
It's called [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html).

It's a pandas method that allows you to group a DataFrame by a column and then calculate a sum, or any other statistic, for each unique value. This is necessary when you want to rack up statistics on a long list of values, or about a combination of fields.

```{note}
If you're into databases and SQL, [groupby](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#group-by)
may sound familiar.
```

## Grouping by one field

As we've been digging through the data, I'm sure a few questions have popped into mind. One interesting field in the contributions list is the home state of the contributor. A natural question follows: How much of the money came from outside of California?

If you scroll back up and look carefully as the info command we ran after merging out data, you will noticed it includes a column named `contributor_state`.

That's the field we want to group with here. Here's how you do it.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
my_committees = committee_list[committee_list.prop_name == my_prop]
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
support = merged_prop[merged_prop.committee_position == 'SUPPORT']
oppose = merged_prop[merged_prop.committee_position == 'OPPOSE']
```

```{code-cell}
merged_prop.groupby("contributor_state")
```

A nice start. But you'll notice you don't get much back. The data's been grouped by state, but we haven't chosen what to do with it yet. We want totals by state, so we can sum the `amount` field the same way we did earlier for the entire DataFrame.

```{code-cell}
merged_prop.groupby("contributor_state").amount.sum()
```

Again our data has come back as an ugly Series. To reformat it as a pretty DataFrame use the reset_index method again.

```{code-cell}
merged_prop.groupby("contributor_state").amount.sum().reset_index()
```

Sorting totals from highest to lowest is easy. Remember the {doc}`sort values trick </sort_values/index>` we learned earlier? Voila! Here's our answer:

```{code-cell}
merged_prop.groupby("contributor_state").amount.sum().reset_index().sort_values("amount", ascending=False)
```

## Grouping by multiple fields

Finding the top contributors is almost as easy, but since the first and last names are spread between two fields we'll need to submit them to groupby as a list. Copy the last line above, and replace "contributor_state" with a list like the one here:

```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)
```

You should be noticing that several of the top contributors appear to be the same person with their name entered in slightly different ways. This is another important lesson of campaign contributions data. Virtually none of the data is standardized by the campaigns or the government. The onus is on the analyst to show caution and responsibly combine records where the name fields refer to the same person.

To find out if each contributor supported or opposed the measure, you simply add that field to our groupby method.

```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)
```

If you want the top supporters or opponents alone, run those same commands with the `support` and `oppose` datasets we {doc}`filtered down to earlier </filter/index>`. Everything else about the commands would be the same as the first one above.

For the supporters:

```{code-cell}
support.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)
```

For the opponents:

```{code-cell}
oppose.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)
```

## How to not be wrong

You've done it. Our brief interview is complete and you've answered the big question that started our inquiry.

Or so you think! Look again at our rankings above. Now compare them against the ranking we looked at earlier in our {doc}`sorting lesson </sort_values/index>`.

Study it closely and you'll see an important difference. All of the contributors without a first name are dropped from our groupby lists. And some of them gave a lot of money.

This is happening because of another pandas quirk. Empty fields are read in by pandas as [null values](<https://en.wikipedia.org/wiki/Null_(mathematics)>), which is a mathematical representation of nothing. In pandas a null is called a [NaN](https://en.wikipedia.org/wiki/NaN), an abbreviation for "not a number" commonly used in computer programming.

And, bad news, pandas' ``groupby`` method will drop any rows with nulls in the grouping fields. So all those records without a first name were silently excluded from our analysis. Yikes!

Whatever our opinion of pandas' default behavior, it's something we need to account for, and a reminder that we should never assume we know what computer programming tools are doing under the hood. As with human sources, everything your code tells you should be viewed skeptically and verified.

The solution to this problem is easy. We need to instruct pandas not to drop the null values by adding an extra option to ``groupby``.


```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Now we've finally got a ranking we can work with. Congratulations, you've finished our analysis.


## Bonus: Creating a New Column

Let's say we wanted to take an extra step to learn whether these top contributors are from inside the state or outside of it.

We could just add "contributor_state" to the ``groupby`` statement. 

```{code-cell}
merged_prop.groupby(["contributor_firstname", "contributor_lastname","contributor_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

But we might want to quickly sort in-state vs. out-of-state donors, or perform similar calculations, and just adding the contributor state doesn't allow us to quickly evaluate trends. Plus, adding the "state" adds two more rows to our ranking list, probably because a donor with the same name reported their location differently across multiple donations.

Well, we could also group by state alone, to get a better sense of it.

```{code-cell}
merged_prop.groupby(["contributor_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Or we could filter to calculate just to California, and then filter again to not California. The query function lets us check whether a statement is true (in this case, does ``contributor_state`` equal ``'CA'``). Then it performs an operation on the results.

```{code-cell}
merged_prop.query("contributor_state == 'CA'")['amount'].sum()
```

```{code-cell}
merged_prop.query("contributor_state != 'CA'")['amount'].sum()
```

But what if we want a quick way to group by "California" vs. "not-California," and we want to be able to refer to that later? Instead, we can use conditionals to create a new column based on whether or not a candidate is in-state. Then we can group by that column. 

There are a few ways to achieve this. We're going to write a conditional directly into our Pandas statement. We'll create a True/False flag, which is a Boolean data type.

```{code-cell}
mermerged_propged["in_state"] = merged_prop["contributor_state"] == "CA"
```

This basically says, "create a new column in merged called ``in_state``. Use ``contributor_state`` as the basis. When a row in ``contributor`` state equals the string ``CA``, that means ``in_state`` should be set to equal ``True``. In all other circumstances, ``in_state`` will equal ``False``."

Now, we can see our new column in the dataframe. It will show up on the far right if you don't specify a location.

```{code-cell}
merged_prop.head()
```

Let's use our earlier groupby and sum code, but group by the ``in_state`` flag instead of by the contributor's state.

```{code-cell}
merged_prop.groupby(["in_state"], dropna=False).amount.sum().reset_index().sort_values("amount", ascending=False)
```

Notice that these totals match our "California" vs. "not-California" sum totals that we calculated with the query function up above. That's good! This is one way to QA your new column. If your totals didn't match, it means you should go back and double-check the logic in your conditional statement that's creating the new column.

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