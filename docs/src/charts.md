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

# Charts

Python has a number of charting tools that can work hand-in-hand with pandas. While [Altair](https://altair-viz.github.io/) is a relatively new package compared to classics like [matplotlib](https://matplotlib.org/), it has great documentation and is easy to configure. Let’s take it for a spin.

## Make a basic bar chart

The first thing we need to do is import Altair. In the tradition of pandas, we'll import it with the alias `alt` to reduce how much we need to type later on. 

```{code-cell}
:tags: [hide-cell]

import warnings
warnings.simplefilter("ignore")
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().rename("accidents").reset_index()
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list["per_hour"] = merged_list.accidents / merged_list.total_hours
merged_list["per_100k_hours"] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

```{code-cell}
import altair as alt
```

```{note}
If the import triggers an error that says your notebook doesn't have Altair, you can install it by running `%pip install altair` in a cell. This will download and install the library using the [pip](https://pip.pypa.io/en/stable/) package manager and Jupyter's built-in [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
```

In a typical analysis, you'd import all of your libraries in one cell at the top of the file. That way, if you need to install or make changes to the packages a notebook uses, you know where to find them and you won't hit errors importing a package midway through running a file.

With Altair imported, we can now feed it our DataFrame to make a simple bar chart. Let's take a look at the basic building block of an Altair chart: the `Chart` object. We'll tell it that we want to create a chart from `merged_list` by passing the DataFrame in, like so:

```{code-cell}
alt.Chart(merged_list)
```

OK! We got an error, but don't panic. The error says that Altair needs a "mark" — that is to say, it needs to know not only what data we want to visualize, but also _how_ to represent that data visually. There are lots of different marks that Altair can use (you can [check them all out here](https://altair-viz.github.io/user_guide/marks.html)). But let's try out the most versatile mark in our visualization toolbox: the bar.

```{code-cell}
alt.Chart(merged_list).mark_bar()
```

That's an improvement, but we've got a new error: Altair doesn't know which columns of our DataFrame to look at! At a minimum, we also need to define the column to use for the x- and y-axes. We can do that by chaining in the `encode` method.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="latimes_make_and_model",
    y="per_100k_hours"
)
```

That’s more like it!

Here's an idea — maybe we do horizontal bars instead of vertical. How would you rewrite this chart code to reverse those bars?

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y="latimes_make_and_model"
)
```

This chart is an okay start, but it's sorted alphabetically by y-axis value, which is pretty sloppy and hard to visually parse. Let's fix that.

We want to sort the y-axis values by their corresponding x values. We know how to do that in Pandas, but Altair has its own opinions about how to sort a DataFrame, so it will override any sort order on the DataFrame we pass in.

Until now, we've been using the shorthand syntax to create our axes, but to add more customization to our chart we'll have to switch to the longform way of defining the y-axis.

To do that, we'll use a syntax like this: `alt.Y(column_name)`. Instead of passing a string to `y` and letting Altair do the rest, this lets us create a y-axis object and then give it additional instructions.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model")
)
```
This chart should look identical to our previous attempt when we created the y-axis the simpler way, but it opens up new options! Now we can instruct Altair to sort the y-axis by the x-axis values.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("x")
)
```

That's looking a lot neater! By default, the sort order will be small to large. Visually, if we want to feature the highest accident rates, it probably makes sense to reverse that order. We can do that by adding a minus before the axis name.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x")
)
```

And we can't have a chart without context. Let's throw in a title for good measure.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x")
).properties(
    title="Helicopter accident rates"
)
```

Yay, we made a chart!

## Other marks

What if we wanted to switch it up and show this data in a slightly different form? For example, in the [Los Angeles Times story](https://www.latimes.com/projects/la-me-robinson-helicopters/), the fatal accident rate is shown as a scaled circle.

We can try that out with just a few small tweaks, using Altair's `mark_circle` option. We'll keep the `y` encoding, since we still want to split out our chart by make and model. Instead of an `x` encoding, though, we'll pass in a `size` encoding, which will pin the radius of each circle to that rate calculation. And hey, while we're at it, let's throw in an interactive tooltip that displays the accident rate when users hover over a mark.

```{code-cell}
alt.Chart(merged_list).mark_circle().encode(
    size="per_100k_hours",
    y="latimes_make_and_model",
    tooltip="per_100k_hours"
)
```
A nice little change from all the bar charts! But once again, the default sorting alphabetical by name. Instead, it would be really nice to sort this by rate, as we did with the bar chart. How would we go about that?

```{code-cell}
alt.Chart(merged_list).mark_circle().encode(
    size="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-size"),
    tooltip="per_100k_hours"
)
```

## `datetime` data

One thing you'll almost certainly find yourself grappling with time and time again is date (and time) fields, so let's talk about how to handle them.

Let’s see if we can do that with our original DataFrame, the `accident_list` that contains one record for every helicopter accident. We can remind ourselves what it contains with the `info` command.

```{code-cell}
accident_list.info()
```

When you import a CSV file with `read_csv` it will take a guess at column types — for example, `integer`, `float`, `boolean`, `datetime` or `string` — but it will default to a generic `object` type, which will generally behave like a string, or text, field. You can see the data types that pandas assigned to the accident list on the right hand side of the `info` table.

Take a look above and you'll see that pandas is treating the `date` column as an object. That means we can't chart it using Python's system for working with dates.

But we can fix that. The [`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) method included with `pandas` can handle the conversion. Here's how to reassign the `date` column after making the change.

```{code-cell}
accident_list["date"] = pd.to_datetime(accident_list["date"])
```

This redefines each object in that column as a date. If your dates are in an unusual or ambiguous format, you may have to [pass in a specific formatter](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html), but in this case pandas should be able to guess correctly.

Run `info` again and you'll notice a change. The data type for `date` has changed.

```{code-cell}
accident_list.info()
```

Now that we've got that out of the way, let’s see if we can chart with it, tracking fatalities over time.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="date",
  y="total_fatalities"
)
```

This is great on the x-axis, but it's not quite accurate on the y. To make sure this chart is accurate, we'll need to aggregate the y-axis in some way.

## Aggregate with Altair

We could back out and create a new dataset grouped by date, but Altair actually lets us do some of that grouping on the fly. We want to add everything that happens on the same date, so we'll pop in a `sum` function on our y column.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="date",
  y="sum(total_fatalities)"
)
```

This is getting there. But sometimes plotting on a day-by-day basis isn't all that useful — especially over a long period of time like we have here.

Again, we could back out and create a new DataFrame grouping by month, but we don't have to — in addition to standard operations (sum, mean, median, etc.), Altair gives us some handy datetime aggregation options. You can find a list of options in the [library documentation](https://altair-viz.github.io/user_guide/transform/timeunit.html).

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="yearmonth(date)",
  y="sum(total_fatalities)",
)
```

This is great for showing the pattern of fatalities over time, but it doesn't give us additional information that might be useful. For example, we almost certainly want to investigate the trend for each manufacturer.

What can do is facet, which will create separate charts, one for each helicopter maker.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="yearmonth(date)",
  y="sum(total_fatalities)",
  facet="latimes_make"
)
```

## Add a `color`

What important fact in the data is this chart *not* showing? There are _two_ Robinson models in the ranking. It might be nice to emphasize them.

We have that `latimes_make` column in our original DataFrame, but it got lost when we created our ranking because we didn't include it in our `groupby` command. We can fix that by scrolling back up our notebook and adding it to the command. You will need to replace what's there with a list containing both columns we want to keep.

Make note that because we're listing more than one column in the `groupby` call now, we'll need to surround those column names in a pair of square brackets like so:

```{code-cell}
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().rename("accidents").reset_index()
```

Rerun __all__ of the cells after that one to update everything you're working with and add the new column.

```{note}
Remember: If we change a variable, future cells that use that variable won't change unless we run them again. When you go back and make these changes, make sure to run all of the cells that come after them as well, otherwise you may not get the results you're expecting.

This is one reason that it can be good to clear cell outputs and rerun your analysis every so often. If you've been going back and forth editing cells and tweaking your analysis, you may have saved variables in memory that are no longer accurate. One way to do that is to clear your "kernel" and rerun the whole notebook to make sure everything still runs as you expect it to (In the Jupyter menu, `Kernel` > `Restart Kernel and Clear All Outputs`, or `Restart Kernel and Run Up to Selected Cell`).
```

Now, when you inspect your `merged_list` variable, you should see the `latimes_make` column included.

```{code-cell}
merged_list.info()
```

Let's put that to use with an Altair option that we haven't toyed with yet: `color`.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color="latimes_make"
).properties(
    title="Helicopter accident rates"
)
```

Hey now! That wasn't too hard, was it? But now there are too many colors. It would be easier to read this chart and highlight information we want readers to notice if we used one color for the Robinson bars and made everything else a different color.

The simplest way to do this is to hand Altair a DataFrame with a column that has the values we want to color-code on. We already have the `latimes_make` columns, but in this case we don't want that many values; we just want that column to contain one value for the Robinson rows, and another value for all the non-Robinson rows. It doesn't really matter what those two values are! 

How might we go about creating that column? (Hint: We can adapt the technique we learned about in the Filters chapter!)

One way to do this is to create a test for rows with an `latimes_make` value equal to "ROBINSON", like so:

```{code-cell}
merged_list["latimes_make"] == "ROBINSON"
```
That will give us a true/false list. In the Filters chapter, we used that list to filter the DataFrame to only rows that matched this test. But we can also simply define a new column and save that list to it. Let's call the new column `robinson`.

```{code-cell}
merged_list["robinson"] = merged_list["latimes_make"] == "ROBINSON"
```
If you take a look at our `merged_list` DataFrame, you should now see that new column.

```{code-cell}
merged_list.head()
```
Now, we can alter our chart to use that new column.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color="robinson"
).properties(
    title="Helicopter accident rates"
)
```

_Bonus: This is fine for exploratory use, but we don't really need that legend, since it's adding a highlight to information that's already included in the names of the helicopters. To hide it, we can use that more advanced syntax and instruct Altair to skip creating a legend._

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color=alt.Color("robinson", legend=None)
).properties(
    title="Helicopter accident rates"
)
```

## Polishing your chart

These charts give us plenty of areas where we might want to dig in and ask more questions, but none are polished enough to pop into a news story quite yet. But there *are* lots of additional labeling, formatting and design options that you can dig into in the [Altair docs](https://altair-viz.github.io/index.html) — you can even create Altair themes to specify default color schemes and fonts.

But you may not want to do all that tweaking in Altair, especially if you're just working on a one-off graphic. If you wanted to hand this chart off to a graphics department, all you'd have to do is head to the top right corner of your chart.

See those three dots? Click on that, and you'll see lots of options. Downloading the file as an SVG will let anyone with graphics software like Adobe Illustrator take this file and tweak the design.

To get the raw data out, you'll need to learn one last pandas trick. It's covered in our final chapter.