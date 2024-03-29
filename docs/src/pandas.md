---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_versio   n: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Pandas

Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: [navigate the web](http://docs.python-requests.org/), [parse data](https://docs.python.org/2/library/csv.html), [interact with a database](http://www.sqlalchemy.org/), [run fancy statistics](https://www.scipy.org/), [build a pretty website](https://www.djangoproject.com/) and [so](https://www.crummy.com/software/BeautifulSoup/) [much](http://www.nltk.org/) [more](https://pillow.readthedocs.io/en/stable/).

Creative people have put these tools to work to get [a wide range of things done](https://www.python.org/about/success/) in the academy, the laboratory and even in outer space. Some are included in a toolbox that comes with the language, known as the standard library. Others have been built by members of Python’s developer community and need to be downloaded and installed from the web.

![pandas on PyPI](https://palewi.re/docs/first-python-notebook/_static/img/pandas-pypi.png)

One third-party tool that's important for this class is called [pandas](http://pandas.pydata.org/). It was invented for use at a [financial investment firm](https://www.aqr.com/) and has become the leading open-source library for accessing and analyzing data in many different fields.

## Import pandas

Create a new cell at the top of your notebook where we will import pandas for our use. Type in the following and hit the play button.

```{code-cell}
import pandas
```

If nothing happens, that's good. It means you have pandas installed and ready as to use.

```{note}
Since pandas is created by a third party independent from the core Python developers, it wouldn't be installed by default if you followed our [our advanced installation](/appendix/index.md) instructions.

It's available to you because the JupyterLab Desktop developers have pre-selected a curated list of common utilities to include with the package, another reason to love their easy installer.

If your notebook doesn't have pandas, you can install it by running `%pip install pandas` in a cell. This will download and install the library using the [pip](https://pip.pypa.io/en/stable/) package manager and Jupyter's built-in [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
```

Return to the cell with the import and rewrite it like this.

```{code-cell}
import pandas as pd
```

This will import the pandas library at the shorter variable name of `pd`. This is standard practice in the pandas community. You will frequently see examples of pandas code online using `pd` as shorthand. It's not required, but it's good to get in the habit so that your code is more likely to be quickly understood by other computer programmers.

```{note}
In Python, a variable is a way to store a value in memory for later use. A variable is a named location in the computer's memory where a value can be stored and retrieved. Variables are used to store data values, such as numbers, strings, lists, or objects, and they can be used throughout the program to refer to the stored value.

To create your own variable in Python, you use the assignment operator (=) to assign a value to a variable. The variable name is on the left side of the assignment operator and the value is on the right side.
```

## Conduct a simple data analysis

Those two little letters contain dozens of data analysis tools that we'll use in future lessons. They can read in millions of records, compute advanced statistics, filter, sort, rank and do just about anything else you'd want to do with data.

We'll get to all of that soon enough, but let's start out with something simple.

Let's make a list of numbers in a new notebook cell. To keep things simple, enter all of the even numbers between zero and ten. Name its variable something plain like `my_list`. Press play.

```{code-cell}
my_list = [2, 4, 6, 8]
```

You can do cool stuff with any list, even calculate advanced statistics, if you're a skilled Python programmer who is ready and willing to write a big chunk of code. The advantage of pandas is that it saves time by quickly and easily analyzing data with hardly any computer code at all.

In this case, it's as simple as converting that plain Python list into what pandas calls a [Series](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html). Here's how to make it happen in your next cell. Let’s stick with simple variables and name it `my_series`.

```{code-cell}
my_series = pd.Series(my_list)
```

Once the data becomes a Series, you can immediately run a wide range of [descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics). Let's try a few.

How about summing all the numbers? Make a new cell and run this. It should spit out the total.

```{code-cell}
:tags: [show-input]
my_series.sum()
```

Then find the maximum value in the next.

```{code-cell}
:tags: [show-input]
my_series.max()
```

The minimum value in the next.

```{code-cell}
:tags: [show-input]
my_series.min()
```

How about the average, which also known as the mean?

```{code-cell}
:tags: [show-input]
my_series.mean()
```

The median?

```{code-cell}
:tags: [show-input]
my_series.median()
```

The standard deviation?

```{code-cell}
:tags: [show-input]
my_series.std()
```

Finally, all of the above, plus a little more about the distribution, in one simple command.

```{code-cell}
:tags: [show-input]
my_series.describe()
```

Before you move on, go back to the cell with your `my_list` variable and change what's in the list. Here I'll change the values from evens to odds.

```{code-cell}
my_list = [1, 3, 5, 7, 9]
```

Then rerun all the cells below it. You'll see all the statistics update to reflect the different dataset, for instance, the final describe call change to:

```{code-cell}
:tags: [hide-cell]
my_series = pd.Series(my_list)
```

```{code-cell}
:tags: [show-input]
my_series.describe()
```

If you substituted in a series of 10 million records, your notebook would calculate all those same statistics without you needing to write any more code. Once your data, however large or complex, is imported into pandas, there's little limit to what you can do to filter, merge, group, aggregate, compute or chart using simple methods like the ones above. In the chapter to come we’ll start doing just using that with data from a real Los Angeles Times investigation.
