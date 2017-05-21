========================
Chapter 7: Hello filters
========================

Until last November, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved Proposition 64, which asked if the practice ought to be legalized.

A yes vote supported legalization. A no vote opposed it. `In the final tally <http://elections.cdn.sos.ca.gov/sov/2016-general/sov/65-ballot-measures-formatted.pdf>`_, 57% of voters said yes.

Our next mission is to use the DataFrames containing campaign committees and contributors to figure out the biggest donors both for and against the measure.

To do that, the first thing we need to do is isolate the fundraising committees active on Proposition 64, which are now buried among of the list of more than 100 groups active last November.

.. youtube:: lRyABONedV4

*********************
Filtering a DataFrame
*********************

The most common way to filter a DataFrame is to pass an expression as an "index" that can be used to decide which records should be kept and which discarded.

You write the expression by combining a column on your DataFrame with an `"operator" <https://en.wikipedia.org/wiki/Operator_(computer_programming)>`_ like ``==`` or ``>`` or ``<`` and a value to compare the column against.

.. note::

    If you are familiar with writing `SQL <https://en.wikipedia.org/wiki/SQL>`_ to manipulate databases, pandas' filtering system is somewhat similar to a WHERE query. The `official pandas documentation <http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#where>`_ offers direct translations between the two.

In our case, the column we want to filter against is prop.prop_name. We only want to keep those records where the value there matches the full name of Proposition 64.

Where do we get that? Our friend :doc:`value counts </value_counts/index>`.

Running the command we learned before to list and count all of the proposition names will spit out the full name of all 17 measures.

.. code-block:: python

    props.prop_name.value_counts()

From that result we can copy the full name of the proposition and place it between quotation marks to form the filter expression expected by pandas.

.. code-block:: python

    props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'

That expression is then placed between two flat brackets following the variable we want to filter. Place the following code in the next open cell in your notebook.

.. code-block:: python

    props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

Run it and it outputs the filtered dataset, just those committees active on Proposition 64.

.. image:: /_static/prop_filter.png

Now we should save the results of that filter into new variable separate from the full list we imported from the CSV file.

Since it includes only the committees for one proposition lets call it the singular prop.

.. code-block:: python

    prop = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

To check our work find out how many committees are left after the filter, let's run the DataFrame inspection commands we learned earlier.

First head.

.. code-block:: python

    prop.head()

Then info.

.. code-block:: python

    prop.info()
