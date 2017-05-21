=========================
Chapter 11: Hello groupby
=========================

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
