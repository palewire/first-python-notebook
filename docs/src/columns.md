---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Columns

We’ll begin with the `latimes_make_and_model` column, which records the standardized name of each helicopter that crashed. To access its contents separate from the rest of the DataFrame, append a pair of flat brackets with the column’s name in quotes inside. 

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

```{code-cell}
:tags: [show-input]
accident_list['latimes_make_and_model']
```

That will list the column out as a `Series`, just like the ones we created from scratch earlier. Just as we did then, you can now start tacking on additional methods that will analyze the contents of the column.

````{note}
You can also access columns a second way, like this: `accident_list.latimes_make_and_model`. This method is quicker to type, but it won't work if your column has a space in its name. So we're teaching the universal bracket method instead.
````

## Count a column's values

In this case, the column is filled with characters. So we don’t want to calculate statistics like the median and average, as we did before.

There’s another built-in pandas tool that will total up the frequency of values in a column. The method is called [`value_counts`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html) and it’s just as easy to use as `sum`, `min` or `max`. All you need to do it is add a period after the column name and chain it on the tail end of your cell.

```{code-cell}
:tags: [show-input]
accident_list['latimes_make_and_model'].value_counts()
```

Congratulations, you've made your first finding. With that little line of code, you've calculated an important fact: During the period being studied, the Robinson R44 had more fatal accidents than any other helicopter.

But wait. Before we congratulate ourselves, let's take a closer look at the data. Our value counts operation has turned up an imperfection that was buried in the data. Can you see it?

## Cleaning data columns

On closer inspection, we can see that Bell 206 helicopter is listed two different ways, as `BELL 206` and `bell 206`. The variation in capitalization is causing pandas to treat them as two distinct values, when they really ought to be tallied together into one total.

This is a common problem and a simple example of how "dirty" data can trip up a computer program. The solution is to clean up the column prior to analysis.

In this case, we can use the `str` method, which is short for string. In many computer programming languages, string is the technical term used to refer to text. Thus, the pandas `str` method is designed to manipulate a column of text. It can change the casing of text, find and replace different patterns and conduct many other useful operations.

You can access by chaining `.str` and your desired manipulation method after the column name. In this case, we want to use the `upper` method, which will convert all of the text in the column to uppercase.

```{code-cell}
:tags: [show-input]

accident_list['latimes_make_and_model'].str.upper()
```

It's not useful to use in this case, but we can try out the companion `lower` method to see it do the opposite.

```{code-cell}
:tags: [show-input]

accident_list['latimes_make_and_model'].str.lower()
```

To correct the bug, we need to assign the result of the `upper` operation to our existing column and overwrite what's there. We can do that with the `=` operator.

```{code-cell}
:tags: [show-input]

accident_list['latimes_make_and_model'] = accident_list['latimes_make_and_model'].str.upper()
```

```{note}
You can find a full list of `str` methods, along with useful examples, in the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods).
```

Now we can run `value_counts` again to see if the problem has been fixed.

```{code-cell}
:tags: [show-input]

accident_list['latimes_make_and_model'].value_counts()
```

Much better! Now we have a clean list of helicopter models and their frequencies.

While this example is simple, it's a good illustration of how data cleaning is handled. In the real world, you will almost always need to clean your data before you can analyze it, and the challenges will typically be much more complex than this one. Pandas offers a wide range of tools to help you clean your data, but the basic process is always the same: Identify the problem, fix it, and then check your work. The `value_counts` method is one of the most useful tools in this process.

## Pop quiz

Before we move on to the next chapter, here's a challenge. See if you can answer a few more questions a journalist might ask about our dataset. All four of the questions below can be answered using only tricks we've covered thus far. See if you can do it.

1. What was the total number of fatalities?
2. Which helicopter maker had the most accidents?
3. What was the total number of helicopter accidents by year?
4. Which state had the most helicopter accidents?

Once you’ve written code answered those, you’re ready to move on to the next chapter.