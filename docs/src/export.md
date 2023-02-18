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

# Export

Saving the dataframes you’ve created to your computer requires one final pandas method. It’s [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html), an exporting companion to `read_csv`. Append it to any dataframe and provide a filepath. That's all it takes.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list['per_hour'] = merged_list.accidents / merged_list.total_hours
merged_list['per_100k_hours'] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

```{code-cell}
merged_list.to_csv("accident-rate-ranking.csv")
```

The file it creates can be imported into other program for reuse, including the data visualization programs many newsrooms rely on to publish graphics. For instance, the file we've exported above could be used to quickly draft a chart with Datawrapper, like this one:

<iframe title="Helicopter accident rates" aria-label="Split Bars" id="datawrapper-chart-6gTy3" src="https://datawrapper.dwcdn.net/6gTy3/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="452" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(e){if(void 0!==e.data["datawrapper-height"]){var t=document.querySelectorAll("iframe");for(var a in e.data["datawrapper-height"])for(var r=0;r<t.length;r++){if(t[r].contentWindow===e.source)t[r].style.height=e.data["datawrapper-height"][a]+"px"}}}))}();
</script>

```{note}
Interesting in learning more about how to publish data online? Check out ["First Visual Story,"](https://palewi.re/docs/first-visual-story/) a tutorial that will show you how journalists at America’s top news organizations escape rigid content-management systems to publish custom interactive graphics on deadline.
```


The `to_csv()` method accepts several additional optional arguments. The most important one is the filename input, which is used to specify the path and name of the file that will be created. The `index=False` keyword argument tells pandas to exclude the index column of the DataFrame. You can also specify the separator by passing the `sep` parameter.


```{code-cell}
merged_list.to_csv("accident-rate-ranking.csv", index=False, sep=";")
```

This will create a CSV file without the index with semicolons as the separator between values.

And with that, you've completed “First Python Notebook.” If you have any questions or critiques, you can get involved on [our GitHub repository](https://github.com/palewire/first-python-notebook), where all of the code that powers this site is available as open source.
