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

Now it’s time to get our hands on some real data. In 2018, the Los Angeles Times published an investigation headlined, [“The Robinson R44, the world’s best-selling civilian helicopter, has a long history of deadly crashes.”](https://www.latimes.com/projects/la-me-robinson-helicopters/)

![jupyterlab desktop download](/_static/R44-story.png)

It reported that Robinson’s R44 led all major models with the highest fatal accident rate from 2006 to 2016. The analysis was [published on GitHub](https://github.com/datadesk/helicopter-accident-analysis) as a series of Jupyter notebooks.

The analysis was based on two key datasets:

1. The National Transportation Safety Board's [Aviation Accident Database](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx)
2. The Federal Aviation Administration's [General Aviation and Part 135 Activity Survey](https://www.faa.gov/data_research/aviation_data_statistics/general_aviation/)

After a significant amount of work gathering and cleaning the source data, the number of accidents for each helicopter model were normalized using the flight hours estimates in the survey. For the purposes of this demonstration, we will read in tidied versions of each file that are ready for analysis.

The data are structured in rows of comma-separated values. This is known as a [CSV file](https://en.wikipedia.org/wiki/Comma-separated\_values). It is the most common way you will find data published online. The pandas library is able to read in files from a variety formats, including CSV.

## Create a DataFrame

Scroll down to the first open cell. There we will import the first CSV file listed above using the [read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) function included with pandas.

```{warning}
You will need to precisely type in the URL to the file. Feel free to copy and paste it from the example above into your notebook.
```

```{code-cell}
:tags: [hide-cell]

import pandas as pd
```

```{code-cell}
pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
```

After you run the cell, you should see a big table like the one above. It is a DataFrame where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might.

The advantage here is that rather than manipulating the data through a haphazard series of clicks and keypunches we will be gradually grinding down the data using a computer programming script that is 100% transparent and reproducible.

## Creating a variable

In order to do more with your DataFrame, we need to store it so it can be reused in subsequent cells. We can do this by saving in a ["variable"](https://en.wikipedia.org/wiki/Variable_(computer_science)), which is a fancy computer programming word for a named shortcut where we save our work as we go.

Go back to your initial cell and change it to this. Then rerun it.

```{code-cell}
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
```

After you run it, you shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `committee_list`, which we can now begin interacting with in the cells that follow.

We can do this by calling ["methods"](https://en.wikipedia.org/wiki/Method_(computer_programming)) that pandas makes available to all DataFrames.

You may not have known it at the time, but `read_csv` is one of these methods. There are dozens more that can do all sorts of interesting things. Let's start with some easy ones that analysts use all the time.

## Use the `head` method

To preview the first few rows of the dataset, try the [head](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html) method. Add a new cell and type this in and hit the run button again.

```{code-cell}
committee_list.head()
```

## Use the `info` method

To get a look at all of the columns and what type of data they store, add another cell and try the [info](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html) method.

```{code-cell}
committee_list.info()
```

Look carefully at those results and you see we have more than 100 links between committees and propositions.

## Create another DataFrame

With that we're ready to move on to a related, similar task: Importing all of the individual contributions reported to last year's 17 ballot measures.

We'll start by using the `read_csv` method to import the second CSV file linked above. Save it as a new variable just as we did before. Let's call this one `contrib_list`.

```{code-cell}
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv")
```

Just as we did earlier, you can inspect the contents of this new file with the `head` method.

```{code-cell}
contrib_list.head()
```

You should also inspect the columns using the `info` method. Running these two tricks whenever you open a new file is a good habit to develop so that you can carefully examine the data you’re about to work with.

```{code-cell}
contrib_list.info()
```

Now that you've got some data imported, we're ready to begin our analysis.
