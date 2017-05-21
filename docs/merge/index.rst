======================
Chapter 8: Hello merge
======================

Our next job is to filter down this list, which includes all disclosed contributions to all proposition campaigns, to just those linked to Proposition 64.

We could try to do this with a filter, as we did above with the committees. But look carefully at the columns listed above in the contribution file's ``info`` output. You will notice that this file contains a field called ``calaccess_committee_id`` that is identical to the one found in the committee CSV.

That's because these two files are drawn from a `"relational database" <https://en.wikipedia.org/wiki/Relational_database>`_ that tracks a variety of information about campaigns using an array of tables linked by common identifiers. In this case, the unique identifying codes of committees in one table can be expected to match those found in another.

We can therefore safely join the two files using the ``pandas`` `merge <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html>`_ method. By default this method will return only those rows with ids found in both tables. That means that if we join the full contributions file to our filtered list of Proposition 64 committees, only the contributions to the Proposition 64 committees will remain.

Here's how to do it. It's as simple as passing both variables to ``merge`` and specifying which field we'd like to join with. We will save the result into another new variable.

.. code-block:: python

    merged = pandas.merge(prop, contribs, on="calaccess_committee_id")

That new ``DataFrame`` variable can inspected just as the ones above.

.. code-block:: python

    merged.head()

.. image:: /_static/merged_head.png

After all that we have created a new dataset that includes only contributions supporting and opposing Proposition 64. We're ready to move on from preparing our data to interviewing it.
