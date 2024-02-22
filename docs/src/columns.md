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

Before we move on to the next chapter, here's a challenge. See if you can answer a few more questions a journalist might ask about our dataset. All four of the questions below can be answered using only tricks we've covered thus far. See if you can do it.

1. What was the total number of fatalities?
2. Which helicopter maker had the most accidents?
3. What was the total number of helicopter accidents by year?
4. Which state had the most helicopter accidents?

Once you’ve written code answered those, you’re ready to move on to the next chapter.