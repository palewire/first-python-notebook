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

```{include} ./_templates/nav.html
```

# Data

In 2018, the Los Angeles Times published an investigation headlined, [“The Robinson R44, the world’s best-selling civilian helicopter, has a long history of deadly crashes.”](https://www.latimes.com/projects/la-me-robinson-helicopters/)

![jupyterlab desktop download](/_static/R44-story.png)

It reported that Robinson’s R44 led all major models with the highest fatal accident rate from 2006 to 2016. The analysis was [published on GitHub](https://github.com/datadesk/helicopter-accident-analysis) as a series of Jupyter notebooks.

The findings were drawn from two key datasets:

1. The National Transportation Safety Board's [Aviation Accident Database](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx)
2. The Federal Aviation Administration's [General Aviation and Part 135 Activity Survey](https://www.faa.gov/data_research/aviation_data_statistics/general_aviation/)

After a significant amount of work gathering and cleaning the source data, the number of accidents for each helicopter model were normalized using the flight hours estimates in the survey. For the purposes of this demonstration, we will read in tidied versions of each file that are ready for analysis.

The data are structured in rows of comma-separated values. This is known as a [CSV file](https://en.wikipedia.org/wiki/Comma-separated\_values). It is the most common way you will find data published online. The pandas library is able to read in files from a variety formats, including CSV.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
```

## The `read_csv` method

Scroll down to the first open cell. There we will import the first CSV file using the [read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) function included with pandas.

```{code-cell}
:tags: [show-input]
pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
```

```{warning}
You will need to precisely type in the URL to the file. Feel free to copy and paste it from the example above into your notebook.
```

After you run the cell, you should see a big table output to your notebook. It is a “DataFrame” where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might.

A major advantage of Jupyter over spreadsheets is that rather than manipulating the data through a haphazard series of clicks and keypunches we will be gradually grinding it down using a computer programming script that is transparent and reproducible.

In order to do more with your DataFrame, we need to store it so it can be reused in subsequent cells. We can do this by saving in a variable, which is a fancy computer programming word for a named shortcut where we save our work as we go.

In order to do more with your DataFrame, we need to store it so it can be reused in subsequent cells. We can do this by saving it in a variable, just as we did in with our `number` in chapter two.

Go back to your initial cell and change it to this. Then rerun it.

```{code-cell}
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/stanford-january-2023/docs/src/_static/ntsb-accidents.csv")
```

After you run it, you shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `accident_list`, which we can now begin interacting with in the cells that follow.

We can do this by calling ["methods"](https://en.wikipedia.org/wiki/Method_(computer_programming)) that pandas makes available to all DataFrames. You may not have known it at the time, but `read_csv` is one of these methods. There are dozens more that can do all sorts of interesting things. Let’s start with some easy ones that analysts use all the time.

## The `head` method

To preview the first few rows of the dataset, try the [head](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html) method. Add a new cell and type this in and hit the play button again.

```{code-cell}
:tags: [show-input]
accident_list.head()
```

It does the first five by default. If you want a different number, submit it as an input.

```{code-cell}
:tags: [show-input]
accident_list.head(1)
```

## The `info` method

To get a look at all of the columns and what type of data they store, add another cell and try the [info](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html) method. Look carefully at the results and you'll see we have 163 fatal accidents to review.

```{code-cell}
:tags: [show-input]
accident_list.info()
```

Now that you've got some data imported, we’re ready to begin our analysis.
