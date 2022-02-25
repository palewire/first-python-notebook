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

Now it's time to get our hands on some real data.

The coalition has created simplified data files containing the disclosure forms that committees campaigning either for against one of the 17 propositions on the ballot in November 2016 filed with the state of California.

They are:

| Name                | Description                                                                   |
| ------------------- | ----------------------------------------------------------------------------- |
| [committees.csv]    | Committees active in the election linked to propositions supported or opposed |
| [contributions.csv] | Donors reported by each of the committees                                     |

The data are structured in rows of comma-separated values. This is known as a [CSV file]. It is the most common way you will find data published online.

## Creating a DataFrame

The pandas library is able to read in files from a variety formats, including CSV.

If it's not currently running start up your Jupyter Notebook as described in {doc}`chapter two </notebook/index>`.

Scroll down to the first open cell. There we will import the first CSV file listed above using the [read_csv] function included with pandas.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
```

```{code-cell}
pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
```

```{warning}
You will need to precisely type in the URL to the file. Feel free to copy and paste it from the example above into your notebook.
```

After you run the cell, you should see a big table printed below.

It is a DataFrame where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might.

The advantage here is that rather than manipulating the data through a haphazard series of clicks and keypunches we will be gradually grinding down the data using a computer programming script that is 100% transparent and reproducible.

## Creating a variable

In order to do that, we need to store our DataFrame so it can be reused in subsequent cells. We can do this by saving in a ["variable"], which is a fancy computer programming word for a named shortcut where we save our work as we go.

Go back to your initial cell and change it to this. Then rerun it.

```{code-cell}
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv")
```

After you run it, you shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `committee_list`, which we can now begin interacting with in the cells that follow.

We can do this by calling ["methods"] that pandas has made available to all DataFrames.

You may not have known it at the time, but `read_csv` was one of these methods. There are dozens more that can do all sorts of interesting things. Let's start with some easy ones that analysts use all the time.

## Using the head method

First, to preview the first few rows of the dataset, try the [head] method. Hit the `+` button in the toolbar to add a new cell below the first one. Type this in it and hit the run button again.

```{code-cell}
committee_list.head()
```

## Using the info method

To get a look at all of the columns and what type of data they store, add another cell and try [info].

```{code-cell}
committee_list.info()
```

Look carefully at those results and you see we have more than 100 links between committees and propositions.

## Creating another DataFrame

With that we're ready to move on to a related, similar task: Importing all of the individual contributions reported to last year's 17 ballot measures.

We'll start by using the `read_csv` method to import the second CSV file linked above. Save it as a new variable just as we did before. Let's call this one `contrib_list`.

```{code-cell}
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv")
```

Just as we did earlier, you can inspect the contents of this new file with the head method.

```{code-cell}
contrib_list.head()
```

You should also inspect the columns using the info method. Running these two tricks whenever you open a new file is a good habit to develop so that you can carefully examine the data you're about to work with.

```{code-cell}
contrib_list.info()
```

Now that you've got some data imported, we're ready to begin our analysis.

["methods"]: https://en.wikipedia.org/wiki/Method_(computer_programming)
["variable"]: https://en.wikipedia.org/wiki/Variable_(computer_science)
[california civic data coalition]: http://www.californiacivicdata.org/
[committees.csv]: https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/committees.csv
[contributions.csv]: https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/src/_static/contributions.csv
[csv file]: https://en.wikipedia.org/wiki/Comma-separated_values
[head]: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html
[info]: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html
[read_csv]: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
