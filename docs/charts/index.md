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

# Charts

Python has a number of charting tools that can work hand-in-hand with pandas. [Altair](https://altair-viz.github.io/) is a relative newbie, but it's got good documentation and can display charts right in your Jupyter Notebook — plus it can export to lots of other formats.

Let's take it for a spin.

## A Basic Bar Chart

Head back to the import cell at the top of your notebook and add Altair. We'll usually import it with the alias `alt` so we don't have to type out the whole thing every time we make a chart.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
merged_everything = pd.merge(committee_list, contrib_list, on="calaccess_committee_id")
merged_prop = merged_everything[merged_everything.prop_name == my_prop]
merged = pd.merge(my_committees, contrib_list, on="calaccess_committee_id")
support = merged_prop[merged_prop.committee_position == 'SUPPORT']
oppose = merged_prop[merged_prop.committee_position == 'OPPOSE']
```

```{code-cell}
import altair as alt
```

Now rerun the entire notebook, as we learned above. You will need to do this when you halt and restart your notebook on the command line. Reminder, you can do this by pulling down the `Cell` menu at the top of the notebook and selecting the `Run all` option.

Let's pick up where we last left off in {doc}`the groupby chapter </groupby/index>`. If we want to chart out how much the top supporters of the proposition spent, we first need to select them from the dataset. Using the grouping and sorting tricks we learned earlier, the top 10 can be returned like this:

```{code-cell}
top_supporters = support.groupby(
    ["contributor_firstname", "contributor_lastname"],
    dropna=False
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)
```

Now that we have `altair` imported, we can pop that dataframe into a quick chart. Let's step through the building blocks of a chart.

```{code-cell}
alt.Chart(top_supporters).mark_bar().encode(
    x="contributor_lastname",
    y="amount"
)
```

Look at that chart!

Here's an idea — maybe we want to do horizontal, not vertical bars. How would you rewrite this chart code to reverse those bars?

```{code-cell}
alt.Chart(top_supporters).mark_bar().encode(
    x="amount",
    y="contributor_lastname"
)
```

What if we wanted to focus on the top five records? We can use that ``head`` command we already know.

```{code-cell}
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y="contributor_lastname"
)
```

This chart is an okay start, but it's sorted alphabetically by y-axis value, which is pretty sloppy and hard to visually parse. Let's fix that.

We want to sort the y-axis values by their corresponding x values. We've been using the shorthand syntax to pass in our axis columns so far, but to add more customization to our chart we'll have to switch to the longform way of defining the y axis.

To do that, we'll use a syntax you may recognize from the way in the first place: `alt.Y(column_name, arg="value")`. There are lots of arguments that you might want to pass in, like ones that will sum or average your data on the fly or limit the number range you want your axis to display. In this case, we'll be using the `sort` command.

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

Now, we have a good idea of who spent the most in support of Prop. 64. What if we wanted to see who spent money on both sides?

## Adding visual complexity

Add a new cell and a new dataframe, `top_contributors`, summing up the top contributors in our whole `merged` dataframe. We're going to repeat a lot of the pandas functions we've stepped through before, all in one go this time.

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

We have that `committee_position` column in our dataframe now. Let's try an altair option that we haven't used yet: color. Can you guess where we should add that in?

```{code-cell}
alt.Chart(top_contributors).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_lastname",sort="-x"),
    color="committee_position"
)
```

Hey now! That wasn't too hard, was it?

## Tackling time scales

One thing you'll almost certainly find yourself grappling with time and time again is date (and time) fields, so let's talk about how to handle them.

Particularly with campaign finance data, looking at contributions over time can be a useful way to explore. Let's make ourselves a slightly smaller version of the `merged` dataframe so we're not dealing with too many columns.

```{code-cell}
merged_small = merged[[
  "date_received","committee_name_x","committee_position",
  "contributor_lastname","contributor_firstname",
  "contributor_state","amount"
]]
```
Now, let's just check to see what data types Pandas has assigned to each column. On import, it will take a guess at column types — for example, `integer`, `float`, `boolean`, `datetime` or `string` - but it will default to a generic `object` type, which will generally behave like a string, or text, field.

To do that, we can print out a list of `dtypes`, or data types, for each column. This is a good habit to get into — often when a column isn't behaving as you expect it to, it's because Pandas did not guess the data type correctly.

```{code-cell}
merged_small.dtypes
```

So, you'll notice there that Pandas isn't treating our `date_received` column as a date column. We'll talk about how to change the column type in a little bit, but we're in luck here — Altair can actually parse column types independently of Pandas.

Let's try that out with another simple bar chart, making sure to tell Altair that our x-axis column holds temporal data by adding `:T` after the column name. Try running the chart with and without that `:T` and see how that changes the chart.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="date_received:T",
  y="amount"
)
```
This is great on the x axis, but it's not quite accurate on the y. What do you think happens here if there are multiple donations on the same day?

Altair doesnt know what to do with multiple amounts on the same day, so it'll just stack them on top of each other. To make sure this chart is accurate, we'll need to aggregate the y axis in some way.

We could back out and create a new dataset grouped by date, but Altair actually lets us do some of that grouping on the fly. We want to add everything that happens on the same date, so we'll pop in a `sum` function on that column.

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="date_received:T",
  y="sum(amount)"
)
```
OK, this is getting there. But sometimes plotting on a day-by-day basis isn't all that useful — especially over a long period of time, like we have here.

Again, we could back out and create a new dataframe grouping by month, but we don't have to — in addition to standard operations (sum, mean, median, etc.), Altair gives us some handy datetime aggregation options. You can find a list of options in the library documentation [here](https://altair-viz.github.io/user_guide/transform/timeunit.html).

In this case, we have a multi-year time span, so let's try grouping by `yearmonth` (we can't just use `month`, because that will group all, say, January dates together regardless of what year they occurred in).

```{code-cell}
alt.Chart(merged_small).mark_bar().encode(
  x="yearmonth(date_received):T",
  y="sum(amount)"
)
```

## Taking it to production

None of these charts are ready to pop into a news story quite yet. But there *are* lots of additional formatting and design options that you can start digging into in the [Altair docs](https://altair-viz.github.io/index.html) — you can even create Altair themes to specify default color schemes and fonts.

But you may not want to do all that tweaking in code, especially if you're just working on a one-off graphic. If you wanted to hand this chart off to a graphics department, all you'd have to do is head to the top right corner of your chart.

See those three dots? Click on that, and you'll see lots of options. Downloading the file as an SVG will let anyone with graphics software like Adobe Illustrator take this file and tweak the design.

Want to recreate this chart in a tool like [Chartbuilder](https://quartz.github.io/Chartbuilder/) or [Datawrapper](https://www.datawrapper.de/)?  In that case, you'll want to export this data into a spreadsheet.

Guess what? It's this easy.

```{code-cell}
top_supporters.to_csv("top_supporters.csv")
```
