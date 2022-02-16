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

# Remix

Now here's where things get fun. Your entire analysis is scripted top to bottom, which means it can be rerun and reproduced. It also be remixed.

Remember this line earlier?

```{code-cell}
my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'
```

That's where we set which proposition we wanted to filter on. It was a key fork in the road, which shaped all the analysis that followed.

That means that if we substituted a different proposition name from the `value_counts` list just above it we could rerun our notebook and conduct an identical analysis of another proposition, without writing another line of code.

Let's try it. I picked the death penalty ban that was on the same ballot and changed that cell of code to this:

```{code-cell}
my_prop = 'PROPOSITION 062- DEATH PENALTY. INITIATIVE STATUTE.'
```

Now I go to the Run menu at the top of the notebook and selected "Run All Cells." Wait a few seconds and, boom, you'll have a whole new group of donors plotted out.
