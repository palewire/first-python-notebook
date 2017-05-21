==========================
Chapter 16: Hello cleaning
==========================

You've probably noticed that top two supporters are the same person, `Sean Parker <https://en.wikipedia.org/wiki/Sean_Parker>`_. However, due to variations in how the ``contributor_lastname`` and ``contributor_firstname`` fields were filled out on the disclosure forms his contributions were not combined during our earlier grouping.

A common approach to correcting this issue is to create a new column where the cleaned up version of names are stored alongside the raw values from the public data. If two rows with different raw names are given an identical name in the clean column, that field can then be used to group the data and aggregate their contributions together.

There are several different approaches to making that happen. In this introductory lesson we're going to take a simplified approach that will also teach you a valuable skill: How to use panda's ``apply`` method to generate a new column.

The first step is to write a Python `function <https://docs.python.org/2.0/ref/function.html>`_. A function is a fundamental tool shipped with Python that allows you to define a chunk of code that you can rerun later. A typical function will take an input and return a result based on what's passed in each time it's run.

Functions are useful when you have a series of statements you want to run again and again. In our case, we're going to write a function that can inspect any row in our data frame. If that row's name field starts with the phrase ``SEAN PARKER`` we're going to return a common clean name that all Sean Parker rows can share. If it doesn't, we're just going to return the raw name value.

That looks like the code below. Create a new cell and run it there.

.. code-block:: python

    def combine_names(row):
        if row.contributor_fullname.startswith('SEAN PARKER'):
            return 'SEAN PARKER'
        return row.contributor_fullname

You know it's a function because it starts with ``def``. The name we're giving the function, ``combine_names`` is what follows. Then a parenthesis that defines the input the function will expect each time it's run. Since we're going to run this function on every row in a ``DataFrame``, we will only have one input and we will name it ``row``.

Now that we have our function, we'll want to run it across our DataFrame and store the result for each row in a new column. In pandas this can be done for a ``DataFrame`` with the ``apply`` method. To run the method row by row, pandas requires you pass the number 1 into the ``axis`` option.

.. code-block:: python

    top_supporters.apply(combine_names, axis=1)

That will spit out a ``Series`` with the returned value for each row. Notice that the two Sean Parker rows are now identical.

.. image:: /_static/apply-series.png

That ``Series`` can now be saved into a new column on the ``DataFrame`` by assigning it with a new name.

.. code-block:: python

    top_supporters['contributor_cleanname'] = top_supporters.apply(combine_names, axis=1)

This same approach can be used to add new columns that do all kinds of things. One common trick is to use the apply method and a function to divide one column into another, or some other mathematical computation.

Now you can regroup the data using this new column and total the columns again, exactly as we did before.

.. code-block:: python

    top_supporters.groupby(
        "contributor_cleanname"
    ).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

The money previously split between two variations on Sean Parker's name are now combined. You could now remake the charts above without the duplication.

.. image:: /_static/apply-group.png

And that's it. You've completed this class. If you want to keep working, try inventing your own questions to ask and answer with the database, or find more information to analyze at `californiacivicdata.org <http://www.californiacivicdata.org/>`_.

If you have any questions or feedback on the class, please contact me at `ben.welsh@gmail.com <mailto:ben.welsh@gmail.com>`_.
