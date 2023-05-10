
## sphinx/readthedocs

```
pip install sphinx nbsphinx
sphinx-build docs html
...
```


## pypi

```
pip install build
# change setup.py version
python -m build
# ? setup.py build
# test
pip install ~/Dropbox/proj/fstflowchat/dist/fstflowchat-0.0.3.tar.gz
python3 -m twine upload dist/*
```
