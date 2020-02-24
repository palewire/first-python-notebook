========================
Chapter 15: Hello charts
========================

Python has a number of charting tools that can work hand-in-hand with ``pandas``. The most popular is `matplotlib <http://matplotlib.org/>`_. It isn't the prettiest thing in the world, but it offers straightfoward tools for exploring your data by making quick charts. And, best of all, it can display in your Jupyter Notebook.

Before we start, we'll need to make sure ``matplotlib`` is installed. Return to your terminal and try installing it with our buddy pip, as we installed other things before.

.. code-block:: bash

    $ pipenv install matplotlib

After that completes, once again restart your notebook.

.. code-block:: bash

    $ pipenv run jupyter notebook

Now you can open your notebook and add a new cell below the imports that lets the system know you plan to make some charts and that it's okay to surface them in the notebook. 

.. code-block:: python

    %matplotlib inline

.. image:: /_static/matplotlib_inline.png

Let's return to where we set our proposition filter at the top and restore it our initial interest, Proposition 64.

.. code-block:: python

    prop = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

Now rerun the entire notebook, as we learned above. You will need to do this when you halt and restart your notebook on the command line. Reminder, you can do this by pulling down the ``Cell`` menu at the top of the notebook and selecting the ``Run all`` option.

Then scroll down to the bottom of the notebook and pick up where we last left off in :doc:`the previous chapter </github/index>`.

If we want to chart out the top supporters of the proposition, we first need to select them from the dataset. Using the grouping and sorting tricks we learned earlier, the top 10 can returned like this:

.. code-block:: python

    top_supporters = support.groupby(
        ["contributor_firstname", "contributor_lastname"]
    ).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

We can then view them with a trick I bet you remember by now.

.. code-block:: python

    top_supporters.head(10)

.. image:: /_static/top_supporters_df.png

Now that matplotlib is installed, making a simple chart is as simple as stringing the ``plot`` method onto the end of your ``DataFrame``.

.. code-block:: python

    top_supporters.amount.plot.bar()

.. image:: /_static/bar.png

You can rotate the bar chart so that it is horizontal by subituting in the ``barh`` method.

.. code-block:: python

    top_supporters.amount.plot.barh()

.. image:: /_static/barh.png

The chart can be limited to the first five records by slipping in the ``head`` command.

.. code-block:: python

    top_supporters.head(5).amount.plot.barh()

.. image:: /_static/barh_head.png

What are those y axis labels? Those are the row number (pandas calls them indexes) of each row. We don't want that. We want the names. We can swap them in by saving our chart to a variable and then using another matplotlib option, ``set_yticklabels`` to instruct the system which field to use.

.. code-block:: python

    chart = top_supporters.head(5).amount.plot.barh()
    chart.set_yticklabels(top_supporters.contributor_lastname)

.. image:: /_static/barh_lastname.png

Okay, but what if I want to combine the first and last name? We have the data we need in two separate columns, which we can put together simply by inventing a new field on our data frame and, just like a variable, setting it equal to a combination of the other fields.

.. code-block:: python

    top_supporters['contributor_fullname'] = top_supporters.contributor_firstname + " " + top_supporters.contributor_lastname

We can see the results right here.

.. code-block:: python

    top_supporters.head()

Now using that in the chart is as simple as substituting in the ``set_yticklabels`` method we used above.

.. image:: /_static/fullname.png

.. code-block:: python

    chart = top_supporters.head(5).amount.plot.barh()
    chart.set_yticklabels(top_supporters.contributor_fullname)

.. image:: /_static/barh_fullname.png

That's all well and good, but this chart is still pretty ugly. If you wanted to hand this data off to your graphics department, or try your hand at a simple chart yourself using something like `Chartbuilder <https://quartz.github.io/Chartbuilder/>`_, you'd need to export this data into a spreadsheet.

Guess what? It's this easy.

.. code-block:: python

    top_supporters.head(5).to_csv("top_supporters.csv")
