# prune
:deciduous_tree: Trim Entries from a Python Dictionary

# install
`pipenv install prune` or `pip3 install prune`

# usage
```python
from prune import prune

tree = { "ford": { "country": "USA", "year": "2005" }, "ferrari": { "country": "Italy", "year": "1995" }}
branches = ["ford.year", "ferrari.year"]
prune(tree, branches)
# tree is now { "ford": { "country": "USA" }, "ferrari": { "country": "Italy" }}
```

# support
Post an issue at https://github.com/DanielJDufour/prune/issues or email the package author at daniel.j.dufour@gmail.com
