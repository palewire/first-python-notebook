=======================
Chapter 7: Hello filter
=======================

Now that we've seen all the propositions in the dataset, we're ready to take a crucial step towards our goal by filtering the list down to just those committees that supported or opposed Proposition 64.

We can do that by copying the full name of the proposition that appears in the dataset and inserting it into the following statement, which follows the ``pandas`` system for filtering a ``DataFrame``.

You start with the variable you want to filter, and then create an evaluation by combining a column with an `"operator" <https://en.wikipedia.org/wiki/Operator_(computer_programming)>`_ like ``==`` or ``>`` or ``<`` with a value to compare the field against.

.. code-block:: python

    props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

.. image:: /_static/prop_filter.png

Now that we've seen what it outputs, we should save the results of that filter into new variable separate from the full list we imported from the CSV file.

.. code-block:: python

    prop = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

The find out how many records are left after the filter, we can use Python's built-in `len <https://docs.python.org/2/library/functions.html#len>`_ function to inspect our new variable.

.. code-block:: python

    len(prop)

.. image:: /_static/prop_len.png
