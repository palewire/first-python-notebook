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

<nav>
  <div class="row">
    <div class="sevencol">
      <div class="shingle">
        <a href="https://palewi.re/">
          <div rel="rnews:copyrightedBy rnews:hasSource rnews:providedBy">
            <div about="http://palewi.re/" typeof="rnews:Organization">
              <div property="rnews:name">palewire</div>
            </div>
          </div>
        </a>
      </div>
    </div>
    <div class="fivecol last links">
      <ul>
        <li>
          <a href="http://palewi.re/posts/" title="Posts">
            Posts
          </a>
        </li>
        <li>
          <a href="http://palewi.re/work/" title="Work">
            Work
          </a>
        </li>
        <li>
          <a href="http://palewi.re/talks/" title="Talks">
            Talks
          </a>
        </li>
        <li>
          <a href="http://palewi.re/who-is-ben-welsh/" title="Who is Ben Welsh?">
            About
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<div class="row topbar">
    <div class="twelvecol last"></div>
</div>

# Sorting

Another simple but common technique for analyzing data is sorting.

What were the ten biggest contributions? We can find the answer by using the [sort_values] method to rearrange our list using the amount field.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/committees.csv")
contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/contributions.csv")
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
my_committees = committee_list[committee_list.prop_name == my_prop]
merged = pd.merge(my_committees, contrib_list, on="calaccess_committee_id")
support = merged[merged.committee_position == 'SUPPORT']
oppose = merged[merged.committee_position == 'OPPOSE']
```

```{code-cell}
merged.sort_values("amount")
```

Note that returns the DataFrame resorted in ascending order from lowest to highest. That is pandas default way of sorting.

To answer our question you'll need to reverse that, so that values are sorted in descending order from biggest to smallest.

It's a little tricky at first, but here's how to do it with sort_values.

```{code-cell}
merged.sort_values("amount", ascending=False)
```

You can limit the result to the top five by chaining the head method at the end.

```{code-cell}
merged.sort_values("amount", ascending=False).head()
```

We can now use the new variable to rank the five biggest supporting contributions by using sort_values again.

```{code-cell}
support.sort_values("amount", ascending=False).head()
```

And now how about the opposition.

```{code-cell}
oppose.sort_values("amount", ascending=False).head()
```

[sort_values]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html