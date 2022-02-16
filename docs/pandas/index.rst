======
Pandas
======

Lucky for us, Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: `navigate the web`_, `parse data`_, `interact with a database`_, `run fancy statistics`_, `build a pretty website`_ and `so`_ `much`_ `more`_.

Creative people have put these tools to work to get `a wide range of things done <https://www.python.org/about/success/>`_ in the academy, the laboratory and even in outer space.

Some of those tools are included in a toolbox that comes with the language, known as the standard library. Others have been built by members of Python's developer community and need to be downloaded and installed from the web.

One that's important for this class is called `pandas`_. It is a tool invented at a financial investment firm that has become a leading open-source library for accessing and analyzing data in many different fields.


*************
Import pandas
*************

Create a new cell at the top of your Jupyter notebook. There we will import the pandas library for use in our script. Type in the following and hit the play button again.

.. code-block:: python

    import pandas

If nothing happens, that's good. It means you have pandas installed and ready as to use.

.. note::

    Since pandas is created by a third party separate from the core Python developers, it wouldn't be installed by default if you followed our `advanced installation <../appendix>`_ instructions.

    It's available to you because the JupyterLab Desktop developers have pre-selected a curated list of common utilities to include with their installation, another reason to love their easy installer.

Return to the cell with the import and rewrite it like this.

.. code-block:: python

    import pandas as pd

This will import the pandas library at the shorter variable name of ``pd``. This is standard practice in the pandas community and you will frequently see examples of pandas code online using it as shorthand. It's not required, but it's good to get in the habit so that your code will be understood by other computer programmers.

******************************
Conduct a simple data analysis
******************************

Those two little letters contain dozens of data analysis tools that we'll use in future lessons.

They can import massive data files, compute advanced statistics, filter, sort, rank and do just about anything else you'd want to do.

We'll get to all of that soon enough, but let's start out with something simple.

Let's make a list of numbers in a new notebook cell. To keep things simple, enter all of the even numbers between zero and ten. Press play.

.. code-block:: python

    my_list = [2, 4, 6, 8]

If you're a skilled Python programmer, you can do some cool stuff with any list, and even run some stats. But if you hand over to pandas instead, you'll be impressed by how easily you can analyze the data without knowing much computer code at all.

In this case, it's as simple as converting that plain Python list into what pandas calls a `Series <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html>`_. Here's how to make it happen in your next cell.

.. code-block:: python

    my_series = pd.Series(my_list)

Once the data becomes a Series, you can immediately run a wide range of `descriptive statistics <https://en.wikipedia.org/wiki/Descriptive_statistics>`_. Let's try a few.

First, let's sum all the numbers. Make a new cell and run this. It should spit out the total.

.. code-block:: python

    my_series.sum()

Then find the maximum value in the next.

.. code-block:: python

    my_series.max()

The minimum value in the next.

.. code-block:: python

    my_series.min()

How about the average, which also known as the mean?

.. code-block:: python

    my_series.mean()

The median?

.. code-block:: python

    my_series.median()

and the standard deviation?

.. code-block:: python

    my_series.std()

Finally, all of the above, plus a little more about the distribution, in one simple command.

.. code-block:: python

    my_series.describe()

Substitute in a series of 10 million records at the top of the notebook — or even just the odd numbers between zero and ten — and your notebook would calculate all those same statistics without you needing to write any more code.

Once your data, however large or complex, is imported into pandas, there's little limit to what you can do to filter, merge, group, aggregate, compute or chart using simple methods like the ones above.

In the next chapter we'll get started doing just using data tracking the flow of money in California politics.

.. _navigate the web: http://docs.python-requests.org/
.. _parse data: https://docs.python.org/2/library/csv.html
.. _interact with a database: http://www.sqlalchemy.org/
.. _run fancy statistics: https://www.scipy.org/
.. _build a pretty website: https://www.djangoproject.com/
.. _so: https://www.crummy.com/software/BeautifulSoup/
.. _much: http://www.nltk.org/
.. _more: https://pillow.readthedocs.io/en/stable/
.. _pandas: http://pandas.pydata.org/
.. _Pipenv: ../pipenv/
