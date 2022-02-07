=======================
Chapter 3: Hello pandas
=======================

Lucky for us, Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: `navigate the web`_, `parse data`_, `interact with a database`_, `run fancy statistics`_, `build a pretty website`_ and `so`_ `much`_ `more`_.

Creative people have put these tools to work to get `a wide range of things done <https://www.python.org/about/success/>`_ in the academy, the laboratory and even in outer space.

Some of those tools are included in a toolbox that comes with the language, known as the standard library. Others have been built by members of Python's developer community and need to be downloaded and installed from the web.

One that's important for this class is called `pandas`_. It is a tool invented at a financial investment firm that has become a leading open-source library for accessing and analyzing data in many different fields.

***************************
Install pandas with pipenv
***************************

We'll install pandas the same way we installed the JupyterLab earlier: Our new friend :doc:`pipenv </pipenv/index>`.

Let's pick up where we left off at the end of :doc:`chapter 2 </notebook/index>`. Save your notebook by clicking the disk icon or selecting "save and checkpoint" from the file menu. Then switch to your command prompt and hit ``CTRL-C``.

That will kill your notebook and return you to the command line. There we'll install pandas:

.. code-block:: python

    pipenv install pandas


*************
Import pandas
*************

Reopen your notebook and create a new cell at the top of your Jupyter notebook. There we will import the pandas library for use in our script. Type in the following and hit the play button again.

.. code-block:: python

    import pandas

If nothing happens, that's good. It means you have pandas installed and ready.

.. note::

    If you get an error message, return to the prerequisites section make sure you have everything installed properly.

    If you do and it still doesn't work, copy and paste the tail end of your error message into Google. Among the results there will almost certainly be others working through the same problem.

Return to the cell with the import and rewrite it like this.

.. code-block:: python

    import pandas as pd

This will import the pandas library at the shorter variable name of pd. This is not required but it is standard practice in the pandas community and you will frequently see examples of pandas code online using it as shorthand. It's not required, but it's good to get in the habit so that your code will be understood by other computer programmers.

******************************
Conduct a simple data analysis
******************************

Those two little letters contain dozens of data analysis tools that we'll use in future lessons.

They can import massive data files, compute advanced statistics, filter, sort, rank and just about anything else you'd want to do.

We'll get to that soon, but let's start out with something simple.

First let's make a list of numbers in a new notebook cell. To keep things simple, I am going to enter all of the even numbers between zero and ten and press play.

.. code-block:: python

    my_list = [2, 4, 6, 8]

If you're a skilled Python programmer, you can do some cool stuff with any list. But hand it over to pandas instead, and you can analyze it without knowing much computer code at all.

In this case, it's as simple as converting that plain Python list into what pandas calls a `Series <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html>`_. Make it happen in your next cell.

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

How about the average (also known as the mean)? Keep adding cells and calculating new statistics.

.. code-block:: python

    my_series.mean()

The median?

.. code-block:: python

    my_series.median()

The standard deviation?

.. code-block:: python

    my_series.std()

And all of the above, plus a little more about the distribution, in one simple command.

.. code-block:: python

    my_series.describe()

With those simple techniques, we're only scratching the surface of what pandas makes possible.

Substitute in a series of 10 million records at the top of the stack (or even just the odd numbers between zero and ten), and your notebook would calculate all those statistics again without you having to write any more code.

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
