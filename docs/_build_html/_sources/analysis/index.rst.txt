=========================
Chapter 3: Hello analysis
=========================

In some ways, your database is no different from a human source. Getting a good story requires careful, thorough questioning. In this section we will move ahead by conducting an interview with ``pandas`` to pursue our quest of finding out the biggest donors to Proposition 64.

Let's start with something easy. What were the ten biggest contributions? We can find the answer by using the `sort_values <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html>`_ method to rearrange our list using the ``amount`` field.

.. code-block:: python

    merged.sort_values("amount")

.. image:: /_static/merged_sort.png

Note that returns the ``DataFrame`` resorted in ascending order from lowest to highest. To answer our question you'll need to reverse it. Here's how:

.. code-block:: python

    merged.sort_values("amount", ascending=False)

.. image:: /_static/merged_sort_desc.png

You can limit the result to the top five by returning to the ``head`` method and passing in the number of results we'd like.

.. code-block:: python

    merged.sort_values("amount", ascending=False).head(5)

.. image:: /_static/merged_sort_head.png

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

We can now use this new variable to rank the five biggest supporting contributions by using ``sort_values`` again.

.. code-block:: python

    support.sort_values("amount", ascending=False).head(5)

.. image:: /_static/support_sort.png

Now let's repeat all that for opposing contributions. First the filter into a new variable.

.. code-block:: python

    oppose = merged[merged.committee_position == 'OPPOSE']

Then a count.

.. code-block:: python

    len(oppose)

.. image:: /_static/oppose_len.png

Then a ranking.

.. code-block:: python

    oppose.sort_values("amount", ascending=False).head(10)

.. image:: /_static/oppose_sort.png

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

We've encountered a lot of different committees as we've explored the data. A natural question follows: Which ones have raised the most money?

To figure that out, we'll need to group the data by that column and then sum up the ``amount`` for each. We can do that be using the ``pandas`` `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_ method and the ``sum`` trick we've already learned.

If you scroll back up and look carefully as the ``info`` command we ran after merging out data, you will noticed it includes a column named ``committee_name_x`` and ``commitee_name_y``. That is because the field was present on both our committee list and our contributions list prior to joining them together. Rather than drop one of them, ``pandas`` is trained to keep them both and to append suffixes to the end.

That's the field we want to group by here. Since they are identical, it doesn't matter which one we pick. Let's go with x.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum()

.. image:: /_static/committee_group.png

Again our data has come back as an ugly ``Series``. To reformat it as a pretty ``DataFrame`` use the ``reset_index`` method again.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum().reset_index()

.. image:: /_static/committee_group_df.png

Sorting the biggest totals to the top is as easy as appending the ``sort_values`` trick we already know to the end. And voila there's our answer.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/committee_group_sort.png

Finding the top contributors is just as easy. We only need to substitute the name fields into the ``groupby`` method.

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/name_group.png

.. note::

    You should be noticing that several of the top contributors appear to be the same person with their name entered in slightly different ways. This is another important lesson of campaign contributions data. Virtually none of the data is standardized by the campaigns or the government. The onus is on the analyst to show caution and responsibly combine records where the name fields refer to the same person.

To find out if each contributor supported or opposed the measure, you simple add that field to our ``groupby`` method.

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/name_position_group.png

You've done it. Our brief interview is complete and you've answered the big question that started our inquiry. If you're interested in continuing the interview, see if you can answer a few more questions on your own. Here are some ideas:

- What percentage of donations came from people who live outside of California?
- What are the top employers of donors who gave for and against the measure?
- Which committees had the fewest donors?
