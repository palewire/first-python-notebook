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

```{include} ./_templates/nav.html
```

# Pandas

Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: [navigate the web](http://docs.python-requests.org/), [parse data](https://docs.python.org/2/library/csv.html), [interact with a database](http://www.sqlalchemy.org/), [run fancy statistics](https://www.scipy.org/), [build a pretty website](https://www.djangoproject.com/) and [so](https://www.crummy.com/software/BeautifulSoup/) [much](http://www.nltk.org/) [more](https://pillow.readthedocs.io/en/stable/).

Creative people have put these tools to work to get [a wide range of things done](https://www.python.org/about/success/) in the academy, the laboratory and even in outer space. Some are included in a toolbox that comes with the language, known as the standard library. Others have been built by members of Python’s developer community and need to be downloaded and installed from the web.

One third-party tool that's important for this class is called [pandas](http://pandas.pydata.org/). It was invented for use at a [financial investment firm](https://www.aqr.com/) and has become the leading open-source library for accessing and analyzing data in many different fields.

## Import pandas

Create a new cell at the top of your notebook where we will import pandas for our use. Type in the following and hit the play button.

```{code-cell}
import pandas
```

If nothing happens, that's good. It means you have pandas installed and ready as to use.

```{note}
Since pandas is created by a third party independent from the core Python developers, it wouldn't be installed by default if you followed our [our advanced installation](/appendix/index.md) instructions.

It's available to you because the JupyterLab Desktop developers have pre-selected a curated list of common utilities to include with their installation, another reason to love their easy installer.
```

Return to the cell with the import and rewrite it like this.

```{code-cell}
import pandas as pd
```

This will import the pandas library at the shorter variable name of `pd`. This is standard practice in the pandas community. You will frequently see examples of pandas code online using `pd` as shorthand. It's not required, but it's good to get in the habit so that your code is more likely to be quickly understood by other computer programmers.

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

First, sum all the numbers. Make a new cell and run this. It should spit out the total.

```{code-cell}
:tags: [hide-output,show-input]
my_series.sum()
```

Then find the maximum value in the next.

```{code-cell}
:tags: [hide-output,show-input]
my_series.max()
```

The minimum value in the next.

```{code-cell}
:tags: [hide-output,show-input]
my_series.min()
```

How about the average, which also known as the mean?

```{code-cell}
:tags: [hide-output,show-input]
my_series.mean()
```

The median?

```{code-cell}
:tags: [hide-output,show-input]
my_series.median()
```

The standard deviation?

```{code-cell}
:tags: [hide-output,show-input]
my_series.std()
```

Finally, all of the above, plus a little more about the distribution, in one simple command.

```{code-cell}
:tags: [hide-output,show-input]
my_series.describe()
```

Now try switching `my_list` to contain the odd numbers between zero and ten, then run the cells again. You should see the same operations run on a different input. If you substituted in a series of 10 million records, your notebook would calculate all those same statistics without you needing to write any more code. 

Once your data, however large or complex, is imported into pandas, there's little limit to what you can do to filter, merge, group, aggregate, compute or chart using simple methods like the ones above. In the chapter to come we’ll start doing just using that with data from a real Los Angeles Times investigation.