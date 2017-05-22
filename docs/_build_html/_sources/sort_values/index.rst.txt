=========================
Chapter 10: Hello sorting
=========================

Another simple but common technique for analyzing data is sorting.

What were the ten biggest contributions? We can find the answer by using the `sort_values <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html>`_ method to rearrange our list using the amount field.

.. code-block:: python

    merged.sort_values("amount")

.. image:: /_static/merged_sort.png

Note that returns the ``DataFrame`` resorted in ascending order from lowest to highest. That is pandas default way of sorting.

To answer our question you'll need to reverse that, so that values are sorted in descending order from biggest to smallest. It's a little tricky at first, but here's how to do it with sort_values.

.. code-block:: python

    merged.sort_values("amount", ascending=False)

.. image:: /_static/merged_sort_desc.png

You can limit the result to the top five by chaining the ``head`` method at the end.

.. code-block:: python

    merged.sort_values("amount", ascending=False).head()

.. image:: /_static/merged_sort_head.png

We can now use the new variable to rank the five biggest supporting contributions by using ``sort_values`` again.

.. code-block:: python

    support.sort_values("amount", ascending=False).head()

.. image:: /_static/support_sort.png

And now how about the opposition.

.. code-block:: python

    oppose.sort_values("amount", ascending=False).head()

.. image:: /_static/oppose_sort.png
