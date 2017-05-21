=========================
Chapter 10: Hello sorting
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

We can now use this new variable to rank the five biggest supporting contributions by using ``sort_values`` again.

.. code-block:: python

    support.sort_values("amount", ascending=False).head(5)

.. image:: /_static/support_sort.png

Then a ranking.

.. code-block:: python

    oppose.sort_values("amount", ascending=False).head(10)

.. image:: /_static/oppose_sort.png
