======================
Chapter 8: Hello merge
======================

Our next job is to filter down the contributions list, which includes all disclosed contributions to all proposition campaigns, to just those linked to Proposition 64.

We *could* try to do this with a filter, as we did :doc:`before </filter/index>` with the committees.

But look carefully at the columns listed in the contribution file's info output.

.. code-block:: python

    contrib_list.info()

Now compare that to the committees file.

.. code-block:: python

    committee_list.info()

You will notice that this file contains a field called ``calaccess_committee_id`` that is identical to the one found in the committee file.

That's because these two files are drawn from a `"relational database"`_ that stores data in an array of tables linked together by common identifiers. In this case, the unique identifying codes of committees in one table can be expected to match those found in another.

We can therefore safely join the two files using the pandas `merge`_ method.

.. note::

    If you are familar with traditional databases, you may recognize that the merge method in pandas is similar to SQL's ``JOIN`` statement. If you dig into `merge's documentation`_ you will see it has many of the same options, such as the ability to conduct "inner" and "outer" joins.

******************
Merging DataFrames
******************

By default the ``merge`` method in pandas will return only those rows where a common identifier is found in both tables, which is known as an "inner" join.

That means that if we merge the full contributions file to our filtered list of Proposition 64 committees, only the contributions to the Proposition 64 committees will remain. The result will be equivalent to a filter.

That's exactly what we want. So let's try it.

Merging two DataFrames is as simple as passing both to pandas built-in merge method and specifying which field we'd like to use to connect them together. We will save the result into another new variable.

.. code-block:: python

    merged = pd.merge(my_committees, contrib_list, on="calaccess_committee_id")

That new DataFrame variable can be inspected like any other.

.. code-block:: python

    merged.head()

By looking at the columns you can check how many rows survived the merge.

.. code-block:: python

    merged.info()

You can also see that the DataFrame now contains all of the columns in both tables. Columns with the same name have had a suffix automatically appended to indicate whether they came from the first or second DataFrame submitted to the merge.

We have now created a new dataset that includes only contributions supporting and opposing Proposition 64. We're ready to move on from preparing our data. It's time to interview it.


.. _"relational database": https://en.wikipedia.org/wiki/Relational_database
.. _merge: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
.. _merge's documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
