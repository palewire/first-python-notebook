========================
Chapter 7: Hello filters
========================

Until November 2016, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved Proposition 64, which asked if the practice ought to be legalized.

A yes vote supported legalization. A no vote opposed it. `In the final tally`_, 57% of voters said yes.

Our next mission is to use the DataFrames containing campaign committees and contributors to figure out the biggest donors both for and against the measure.

To do that, the first thing we need to do is isolate the fundraising committees active on Proposition 64, which are now buried among of the list of more than 100 groups active last November.

*********************
Filtering a DataFrame
*********************

The most common way to filter a DataFrame is to pass an expression as an "index" that can be used to decide which records should be kept and which discarded.

You write the expression by combining a column on your DataFrame with an `"operator"`_ like ``==`` or ``>`` or ``<`` and a value to compare the column against.

.. note::

    If you are familiar with writing `SQL`_ to manipulate databases, pandas' filtering system is somewhat similar to a ``WHERE`` query. The `official pandas documentation`_ offers direct translations between the two.

In our case, the column we want to filter against is ``prop_name``. We only want to keep those records where the value there matches the full name of Proposition 64.

Where do we get that? Our friend :ref:`value counts <value counts>`.

Running the command we learned before to :ref:`list <list data>` and :ref:`count <value counts>` 
all of the proposition names will spit out the full name of all 17 measures.

.. code-block:: python

    committee_list.prop_name.value_counts()

From that result we can copy the full name of the proposition and place it between quotation marks in a variable in a new cell. This will allow us to reuse it later.

.. code-block:: python

    my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'

In the next cell we will ask pandas to narrow down our list of committees to just those that match the proposition we're interested in. We will create a filter expression that looks like this: :code:`committee_list.prop_name == my_prop`, and place it between two flat brackets following the variable we want to filter. Place the following code in the next open cell in your notebook.

.. code-block:: python

    committee_list[committee_list.prop_name == my_prop]

Run it and it outputs the filtered dataset, just those committees active on Proposition 64.

Now we should save the results of that filter into new variable separate from the full list we imported from the CSV file.

Since it includes only the committees for one proposition lets call it the singular prop.

.. code-block:: python

    my_committees = committee_list[committee_list.prop_name == my_prop]

To check our work find out how many committees are left after the filter, let's run the DataFrame inspection commands we learned earlier.

First head.

.. code-block:: python

    my_committees.head()

Then info.

.. code-block:: python

    my_committees.info()


.. _In the final tally: http://elections.cdn.sos.ca.gov/sov/2016-general/sov/65-ballot-measures-formatted.pdf
.. _"operator": https://en.wikipedia.org/wiki/Operator_(computer_programming)
.. _SQL: https://en.wikipedia.org/wiki/SQL
.. _official pandas documentation: https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where
