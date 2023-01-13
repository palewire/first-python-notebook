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

# Notebooks

You should see a new panel with an empty box at the top. That means you are all set up and ready to write Python. If you‘ve never done it before, you can remain calm. We can start out slow with some simple math.

Type the following into the box, then hit the play button in the toolbar above the notebook (or hit `SHIFT+ENTER` on your keyboard). The number four should appear.

```{code-cell}
:tags: [show-input]
2+2
```

There. Not so bad, right? You have just written your first code. In the jargon of Python, you have entered two [integers](https://docs.python.org/3/library/functions.html#int) and combined them using [the addition operator](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).

Now try writing in your own math problem in the next cell. Maybe `2+3` or `2+200`. Whatever strikes your fancy. After you've typed it in, hit the play button or `SHIFT+ENTER`.

The to-and-fro of writing Python code in a cell and then running it with the play button is the rhythm of working in a notebook.

If you get an error after you run a cell, look carefully at your code and see that it exactly matches what’s been written in the example. Here's an example of a error that I've added intentionally:

```{code-cell}
:tags: [show-input,raises-exception]
2+2+
```

Don’t worry. Code crashes are a normal part of life for computer programmers. They’re usually caused by small typos that can be quickly corrected. 

```{code-cell}
:tags: [show-input]
2+2+2
```

The best thing you can do is remain calm and carefully read the error message. It usually contains clues that can help you fix the problem.

Over time you will gradually stack cells to organize an analysis that runs down your notebook from the top. A simple example is storing your number in a variable in one cell:

```{code-cell}
number = 2
```

Then adding it to another value in the next cell:

```{code-cell}
:tags: [show-input]
number + 3
```

Run those two cells in succession and the notebook should output the number five. 

Change the `number` value to 3 and run both cells again. Instead of 5, it should now output 6.

So, first this:

```{code-cell}
number = 3
```

Then this:

```{code-cell}
:tags: [show-input]
number + 3
```

Now try defining your own numeric variable and doing some math with it. You can name it whatever you want. Want to try some other math operations? The `-` sign does subtraction. Multipication is `*`. Division is `/`.

```{note}
Cells can contain variables, functions or imports. If you’ve never written code before and are unfamiliar with those terms, we recommend [“An Informal Introduction to Python”](https://docs.python.org/3/tutorial/introduction.html) and subsequent sections of python.org's official tutorial.
```

Once you've got the hang of making the notebook run, you’re ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.
