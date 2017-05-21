=======================
Chapter 9: Hello totals
=======================

Question one answered. Here's number two: What is the total sum of contributions that have been reported?

To answer that let's start by getting our hands on ``amount``, the column with the numbers in it. We can do that just as we did with other columns above.

.. code-block:: python

    merged.amount

.. image:: /_static/merged_amount.png

Now add up the column's total using the ``pandas`` method `sum <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sum.html>`_.

.. code-block:: python

    merged.amount.sum()

.. image:: /_static/merged_amount_sum.png

There's our big total. Fun fact: This number is guaranteed to be lower than the totals reported by the campaigns. Why? Campaigns are only required to report the names of donors over $200, so our data is missing all of the donors who gave smaller amounts of money.

The overall totals are reported elsewhere in lump sums and cannot be replicated by adding up the individual contributions. Understanding this is crucial to understanding not just this data, but all campaign finance data.

Adding up a big total is all well and good. But we're aiming for something more nuanced. We want to separate the money spent for the proposition from the money spent against it. To do that, we'll need to return to the filtering trick we learned above.

First let's look at the column we're going to filter by, ``committee_position``.

.. code-block:: python

    merged.committee_position

.. image:: /_static/merged_position.png

Now let's filter our merged table down using that column and the ``pandas`` filtering method that combines a column, an operator and the value we want to filter by.

.. code-block:: python

    merged[merged.committee_position == 'SUPPORT']

.. image:: /_static/support_filter.png

Let's stick the result in a variable.

.. code-block:: python

    support = merged[merged.committee_position == 'SUPPORT']

And count how many contributions are in this new, more limited set.

.. code-block:: python

    len(support)

.. image:: /_static/support_len.png


Now let's repeat all that for opposing contributions. First the filter into a new variable.

.. code-block:: python

    oppose = merged[merged.committee_position == 'OPPOSE']

Then a count.

.. code-block:: python

    len(oppose)

.. image:: /_static/oppose_len.png

Now sum up the total disclosed contributions to each for comparison. First the opposition.

.. code-block:: python

    oppose.amount.sum()

.. image:: /_static/oppose_amount_sum.png

Then the supporters.

.. code-block:: python

    support.amount.sum()

.. image:: /_static/support_amount_sum.png


The support is clearly larger. But what percent is it of the overall disclosed total? We can find out by combined two ``sum`` calculations using the division operator.

.. code-block:: python

    support.amount.sum() / merged.amount.sum()

.. image:: /_static/support_amount_percent.png
