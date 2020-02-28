========================
Chapter 15: Hello charts
========================

Python has a number of charting tools that can work hand-in-hand with ``pandas``. `Altair <https://altair-viz.github.io/>`_ is a relative newbie in that space, but it's got good documentation and can display charts right in your Jupyter Notebook — and export to lots of other formats.

Let's take it for a spin.

Let's pick up where we last left off in :doc:`the previous chapter </github/index>`. First, we'll want to import Altair. We'll usually import it as ``alt`` so we don't have to type out the whole thing every time we make a chart.

.. code-block:: python

    import altair as alt

Typically you'd import all the libraries you'll need at the top of the notebook, where you imported ``pandas``, but as long as this block appears above the code for your first chart, it'll work.

If we want to chart out the top supporters of the proposition, we first need to select them from the dataset. Using the grouping and sorting tricks we learned earlier, the top 10 can returned like this:

.. code-block:: python

    top_supporters = support.groupby(
        ["contributor_firstname", "contributor_lastname"]
    ).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

We can then view them with a trick I bet you remember by now.

.. code-block:: python

    top_supporters.head(10)

.. image:: /_static/top_supporters_df.png

Now that we have ``altair`` imported, we can pop that dataframe into a quick chart. Let's step through the building blocks of a chart.

.. code-block:: python

    alt.Chart(top_supporters).mark_bar().encode(
        x="contributor_lastname",
        y="amount"
    )

.. image:: /_static/bar_vertical.png

Look at that chart!

Here's an idea — maybe we want to do horizontal, not vertical bars. How would you rewrite this chart code to reverse those bars?

.. code-block:: python

    alt.Chart(top_supporters).mark_bar().encode(
        x="amount",
        y="contributor_lastname"
    )

.. image:: /_static/bar_horizontal.png

What if we wanted to focus on the top five records? We can use that ``head`` command we already know.

.. code-block:: python

    alt.Chart(top_supporters.head(5)).mark_bar().encode(
        x="amount",
        y="contributor_lastname"
    )

.. image:: /_static/bar_head.png

Okay, but what if I want to combine the first and last name? We have the data we need in two separate columns, which we can put together simply by inventing a new field on our data frame and, just like a variable, setting it equal to a combination of the other fields.

.. code-block:: python

    top_supporters['contributor_fullname'] = top_supporters.contributor_firstname + " " + top_supporters.contributor_lastname

Now we can use that column instead of``contributor_lastname`` in our chart.

.. code-block:: python

    alt.Chart(top_supporters.head(5)).mark_bar().encode(
        x="amount",
        y="contributor_fullname"
    )

.. image:: /_static/bar_fullname.png

Notice how the sort order changed when we changed the contributor column? This chart is sorted alphabetically by y-axis value, and it's making everything look pretty sloppy and hard to parse. Let's fix that.

We want to sort the y-axis values by their corresponding x values. We've been using the shorthand syntax to pass in our axis columns so far, but to add more customization to our chart we'll have to switch to the longform way of defining the y axis.

That will look something like the way we define the chart in the first place: ``alt.Y(column_name, arg="value")``. There are lots of options that you might want to pass in, like ones that will sum your data on the fly or define the number range you want your axis to display. In this case, we'll just be using the ``sort`` command.

.. code-block:: python

    alt.Chart(top_supporters.head(5)).mark_bar().encode(
        x="amount",
        y=alt.Y("contributor_fullname", sort="-x")
    )

.. image:: /_static/bar_sort.png

And we can't have a chart without context. Let's throw in a title for good measure.

.. code-block:: python

    alt.Chart(top_supporters.head(5)).mark_bar().encode(
        x="amount",
        y=alt.Y("contributor_fullname", sort="-x")
    ).properties(
        title="Top Contributors in Support of Proposition 64"
    )

.. image:: /_static/bar_title.png

Yay, we made a chart!

That's all well and good, but this isn't ready to pop into a news story quite yet. There are lots of additional formatting and design options that you can start digging into in the `Altair docs <https://altair-viz.github.io/index.html>`_ — you can even create Altair themes to specify default color schemes and fonts.

But you don't have to do all that in code. If you wanted to hand this chart off to a graphics department, all you'd have to do is head to the top right corner of your chart.

.. image:: TK

See those three dots? Click on that, and you'll see lots of options. Downloading the file as an SVG will let anyone with graphics software like Adobe Illustrator take this file and run with it.

Want to recreate this chart in a tool like `Chartbuilder <https://quartz.github.io/Chartbuilder/>`_ or `Datawrapper <https://www.datawrapper.de/>`_?  In that case, you'll want to export this data into a spreadsheet.

Guess what? It's this easy.

.. code-block:: python

    top_supporters.head(5).to_csv("top_supporters.csv")
