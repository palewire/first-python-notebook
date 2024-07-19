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

# Group

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/L27IfY7PZD0?si=WiYeGHh8DTDzoSbz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

The [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) method allows you to group a DataFrame by a column and then calculate a sum, or any other statistic, for each unique value. This functions much like the ["pivot table"](https://en.wikipedia.org/wiki/Pivot_table) feature found in most spreadsheets.

Let's use it to total up the accidents by make and model. You start by passing the field you want to group on to the function.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list['latimes_make_and_model'] = accident_list['latimes_make_and_model'].str.upper()
```

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model")
```

A nice start but you’ll notice you don’t get much back. The data’s been grouped, but we haven’t chosen what to do with it yet. If we wanted the total by model, we would use the `size` method.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model").size()
```

The result is much like `value_counts`, but we're allowed run to all kinds of statistical operations on the group, like `sum`, `mean` and `std`. For instance, we could sum the total number of fatalities for each maker by stringing that field on the end followed by the statistical method.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model")['total_fatalities'].sum()
```

## Reset a DataFrame

You may notice that even though the result of a `groupby` has two columns, pandas does not return a clean-looking table the same way other operations like `head` do. In most instances, you can convert ugly tables like the ones above into a pretty DataFrame by tacking on the `reset_index` method on the end of your code.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model").size().reset_index()
```

Why doesn't `groupby` return a DataFrame? Why does `reset_index` have such a weird name?

Like so much in computer programming, the answer is simply, “because the people who created the library said so.” It’s important to learn that all open-source programming tools are made by humans, and humans have their quirks. Over time you’ll see pandas has more than a few.

As a beginner, you should just accept the oddities and keep moving. As you get more advanced, if there’s something about the system you think could be improved you should consider [contributing](https://pandas.pydata.org/pandas-docs/stable/development/contributing.html) to the Python code that operates the library.

You can clean up the `0` column name assigned by pandas with the `rename` method.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model").size().rename("accidents").reset_index()
```

Now save that as a variable.

```{code-cell}
:tags: [show-input]
accident_counts = accident_list.groupby("latimes_make_and_model").size().rename("accidents").reset_index()
```

That will return a DataFrame with the accident totals we need to calculate a rate. Inspect it with `head`.

```{code-cell}
:tags: [show-input]
accident_counts.head()
```

Now we‘ve got a ranking we can work with.
