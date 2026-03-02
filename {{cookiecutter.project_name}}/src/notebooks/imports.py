# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
# ---

# %% [markdown]
# # Lagring av notebooks som rene tekstfiler
# Jupyter notebooks skal lagres `.py`- eller `.R`-format, i stedet for i
# `.ipynb`-format. Se begrunnelse og beskrivelse i
# [ADR0020](https://adr.ssb.no/0020-lagringsformat-for-jupyter-notebooks/).
# Du kan fortsatt jobbe med filene som notebooks på vanlig måte.
#
# For å åpne en slik fil som Notebook i JupyterLab, høyreklikk på fila og velg
# Open With &rarr; Notebook.

# %%
# Central imports (pandas as pd etc.)
import os

import pandas as pd

# %% [markdown]
# ### Demo av importer fra produksjonsnivå

# %%
# Do local imports here
from functions.fizzbuzz import fizzbuzz


# %%
# Example local function import
for x in fizzbuzz(range(1, 26)):
    print(x)
