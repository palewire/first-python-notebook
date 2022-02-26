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

# Remix

Now here’s where things get fun. Looking back over the cells in your notebook, you’ll seethat the entire analysis is scripted top to bottom. Which means it can be rerun, reproduced and even remixed.

Remember this line earlier?

```{code-cell}
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
```

That’s where we set which proposition we wanted to filter on. It was a key fork in the road, which shaped all the analysis that followed.

If we substitute a different proposition name from the `value_counts` list just above, we could rerun our notebook and analyze another proposition without writing any code.

Let’s try it. Pick the death penalty ban that was on the same ballot. Paste it over the existing cell.

```{code-cell}
my_prop = 'PROPOSITION 062- DEATH PENALTY. INITIATIVE STATUTE.'
```

Now go to the `Run` menu at the top of the notebook and select `Run All Cells.` Wait a few seconds and, boom, you'll have a whole new group of donors mapped out.
