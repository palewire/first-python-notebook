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

# Charts

Python has a number of charting tools that can work hand-in-hand with pandas. [Altair](https://altair-viz.github.io/) is a relative newbie, but it's got good documentation and can display charts right in your Jupyter Notebook — plus it can export to lots of other formats.

Let’s take it for a spin.

## Make a basic bar chart

Head back to the import cell at the top of your notebook and add Altair. We'll usually import it with the alias `alt` so we don't have to type out the whole thing every time we make a chart.

```{code-cell}
:tags: [hide-cell]

import warnings
warnings.simplefilter("ignore")
import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
support = merged_prop[merged_prop.committee_position == 'SUPPORT']
oppose = merged_prop[merged_prop.committee_position == 'OPPOSE']
merged_prop["in_state"] = merged_prop["contributor_state"] == "CA"
```

```{code-cell}
import altair as alt
```

Once that’s run, we can pick up where we last left off at the bottom of the notebook. If we want to chart out how much the top supporters of the proposition spent, we first need to select them from the dataset. Using the grouping and sorting tricks we learned earlier, the top 10 can be returned like this:

```{code-cell}
top_supporters = support.groupby(
    ["contributor_firstname", "contributor_lastname"],
    dropna=False
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)
```

Now that we have `altair` imported, we can pop that dataframe into a quick chart. Let’s step through the building blocks of a chart.

First feed the data to Altair.

```{code-cell}
alt.Chart(top_supporters)
```

From that error, it looks like Altair wants a little more. Let’s tell it we want it to draw bars, which is Altair calls a “mark.”

```{code-cell}
alt.Chart(top_supporters).mark_bar()
```

An improvement, but we’re not there yet. At a minimum, we also need to tell Altair what to put on the x- and y-axes.

```{code-cell}
alt.Chart(top_supporters).mark_bar().encode(
    x="contributor_lastname",
    y="amount"
)
```

Look at that chart! That’s more like it.

Here's an idea — maybe we want to do horizontal, not vertical bars. How would you rewrite this chart code to reverse those bars?

```{code-cell}
alt.Chart(top_supporters).mark_bar().encode(
    x="amount",
    y="contributor_lastname"
)
```

What if we wanted to focus on the top five records? We can use that `head` command we already know.

```{code-cell}
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y="contributor_lastname"
)
```

This chart is an okay start, but it's sorted alphabetically by y-axis value, which is pretty sloppy and hard to visually parse. Let's fix that.

We want to sort the y-axis values by their corresponding x values. We've been using the shorthand syntax to pass in our axis columns so far, but to add more customization to our chart we'll have to switch to the longform way of defining the y axis.

To do that, we'll use a syntax like this: `alt.Y(column_name, arg="value")`. There are lots more arguments that you might want to pass in, like ones that will sum or average your data on the fly or limit the number range you want your axis to display. In this case, we'll stick to using the `sort` command.

```{code-cell}
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_lastname", sort="-x")
)
```

And we can't have a chart without context. Let's throw in a title for good measure.

```{code-cell}
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_lastname", sort="-x")
).properties(
    title="Top Spenders in Support of Proposition 64"
)
```

Yay, we made a chart!

Now, we have a good idea of who spent the most in support of Prop. 64. What if we wanted to see who spent money on both sides? To do that, we’ll need to get a little fancier.

## Add a `color`

Add a new cell and a new dataframe, `top_contributors`, summing up the top contributors in our whole `merged_prop` dataframe. We're going to repeat a lot of the pandas functions we've stepped through before, all in one go this time.

```{code-cell}
top_contributors = merged_prop.groupby(
    ["contributor_firstname", "contributor_lastname","committee_position"],
    dropna=True
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)
```

Now pop `top_contributors` into a chart, just like we did before. Remember that sort function!

```{code-cell}
alt.Chart(top_contributors).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_lastname",sort="-x"),
)
```

What facet of the data is this chart *not* showing? How might we add additional context?

We have that `committee_position` column in our dataframe now. Let's try an altair option that we haven't used yet: `color`. Can you guess where we should add that in?

```{code-cell}
alt.Chart(top_contributors).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_lastname",sort="-x"),
    color="committee_position"
)
```

Hey now! That wasn't too hard, was it?

## Chart `datetime` data

One thing you'll almost certainly find yourself grappling with time and time again is date (and time) fields, so let's talk about how to handle them.

With campaign finance data, looking at contributions over time can be a very useful way to find patterns. Let's make ourselves a slightly smaller version of the `merged_prop` dataframe so we're not dealing with too many columns.

```{code-cell}
merged_small = merged_prop[[
  "date_received",
  "committee_position",
  "contributor_lastname",
  "contributor_firstname",
  "in_state",
  "amount"
]]
```
Now, let's just check to see what data types pandas has assigned to each column. On import, it will take a guess at column types — for example, `integer`, `float`, `boolean`, `datetime` or `string` — but it will default to a generic `object` type, which will generally behave like a string, or text, field.

To do that, we can print out a list of `dtypes`, or data types, for each column. This is a good habit to get into — often when a column isn't behaving as you expect it to, it's because pandas did not guess the data type correctly.

```{code-cell}
merged_small.dtypes
```

So, you'll notice there that pandas isn't treating our `date_received` column as a date column, but we can fix that. The [`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) method can get the job done.

```{code-cell}
merged_small['date_received'] = pd.to_datetime(merged_small['date_received'])
```

This redefines each object in that column as a date. If your dates are in an unusual or ambiguous format, you may have to [pass in a specific formatter](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html), but in this case pandas should be able to guess correctly.

Now that we've got that out of the way, let’s see what it looks like. You know how to make a bar chart now, so which columns should we visualize here? If we want a timeseries, we've got to look to `date_received`.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="date_received",
  y="amount"
)
```

## Aggregate with Altair

This is great on the x axis, but it's not quite accurate on the y. What do you think happens here if there are multiple donations on the same day?

Altair doesnt know what to do with multiple amounts on the same day, so it’ll just stack them all on top of each other. To make sure this chart is accurate, we'll need to aggregate the y axis in some way.

We could back out and create a new dataset grouped by date, but Altair actually lets us do some of that grouping on the fly. We want to add everything that happens on the same date, so we'll pop in a `sum` function on that column.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="date_received",
  y="sum(amount)"
)

```
This is getting there. But sometimes plotting on a day-by-day basis isn't all that useful — especially over a long period of time, like we have here.

Again, we could back out and create a new dataframe grouping by month, but we don't have to — in addition to standard operations (sum, mean, median, etc.), Altair gives us some handy datetime aggregation options. You can find a list of options in the library documentation [here](https://altair-viz.github.io/user_guide/transform/timeunit.html).

In this case, we have a multi-year time span, so let's try grouping by `yearmonth`.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="yearmonth(date_received)",
  y="sum(amount)"
)
```

```{note}
We can't just use `month` because that will group all January dates together regardless of what year they occurred in.
```

This is great for showing the pattern of donations over time, but it doesn't give us a whole lot of additional information that might be useful. For example, we almost certainly want to break these numbers down by whether they were in support of or against our proposition.

We could do that by adding a color encoding, like we did on the last chart. Remember how you'd do that?

In this case, though, stacking those bars makes it a little hard to focus on amounts individually. What can do instead is to facet, which will create two separate chart, one for the supporting side and another for the opposition.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
    x=alt.X("yearmonth(date_received)"),
    y=alt.Y("sum(amount)"),
    facet="committee_position"
)
```
Interesting! And heck, let's throw in a color encoding for our `in_state` column to see the breakdown of in-state vs. out-of-state money coming in by month.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
    x=alt.X("yearmonth(date_received)"),
    y=alt.Y("sum(amount)"),
    facet="committee_position",
    color="in_state",
)
```

This gives us some new things to dig in on. If we were producing this chart for publication, we'd want to do some filtering — for example, this is showing contributions that came in well after November 2016, which probably wouldn't be relevant to a story about how money shaped this particular election.

For now, though, let's take an easier route and just make this chart interactive, which will let us zoom the x axis in and out so we can explore areas of interest.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
    x=alt.X("yearmonth(date_received)"),
    y=alt.Y("sum(amount)"),
    facet="committee_position",
    color="in_state",
).interactive()
```

Hey, we did it!

## Do it live

These charts give us plenty of areas where we might want to dig in and ask more questions, but none are polished enough to pop into a news story quite yet. But there *are* lots of additional labeling, formatting and design options that you can dig into in the [Altair docs](https://altair-viz.github.io/index.html) — you can even create Altair themes to specify default color schemes and fonts.

But you may not want to do all that tweaking in Altair, especially if you're just working on a one-off graphic. If you wanted to hand this chart off to a graphics department, all you'd have to do is head to the top right corner of your chart.

See those three dots? Click on that, and you'll see lots of options. Downloading the file as an SVG will let anyone with graphics software like Adobe Illustrator take this file and tweak the design.

Want to recreate a chart you make in a tool like [Datawrapper](https://www.datawrapper.de/)?  In that case, you'll want to export the relevant dataframe to a spreadsheet.

Guess what? It's this easy.

```{code-cell}
top_supporters.to_csv("top_supporters.csv")
```
