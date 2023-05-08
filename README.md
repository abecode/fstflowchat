# fstflowchat

**fstflowchat** is a small, pedagogical, fst-based dialog toolkit.


fstflowchat uses finite state transducers to control dialog flow.  It
uses graphviz to visualize the dialog flow and as a graph
specification language for the dialog FST.  Each graph edge specifies
two functions, a test function that determines if the edge is a valid
transition, and an output fuction that determines the system's output
as it changes state.


## Installation


To run the stable version run

```
pip install fstflowchat
```

You will first need to install graphviz [graphviz
application](https://graphviz.org/download/) and the [pygraphviz
library](https://pygraphviz.github.io/documentation/stable/install.html).


For mac installation issues, please use the following command after
running `brew install graphviz`, as described in this [stackoverflow
question](https://stackoverflow.com/questions/69970147/how-do-i-resolve-the-pygraphviz-error-on-mac-os)

```
python -m pip install \
	--global-option=build_ext \
	--global-option="-I$(brew --prefix graphviz)/include/" \
	--global-option="-L$(brew --prefix graphviz)/lib/" \
	pygraphviz
```

To install on a Colab notebook, run the following shell escaped
commands to install graphviz and its development libraries and test
the python pygraphviz library before installing fstflowchat:

```
# install graphviz with development libraries
!apt install libgraphviz-dev

# test pygraphviz library (used by fstflowchat
!pip install pygraphviz

# install fstflowchat
!pip install fstflowchat
```


If you are interested in contributing to fstflowchat or if you want to
use the latest code from github (potentially with breaking changes)
you can install fstflowchat in the following ways:

```
# clone and install as an editable pip library
git clone git+https://github.com/abecode/fstflowchat
cd fstflowchat
pip install -e .

# pip install directly from github
pip install git+https://github.com/abecode/fstflowchat
```


## Running a demo

To see a demo, run

```
fstflowchat-example
```

## Documentation

For more information, please see the [documentation](https://fstflowchat.readthedocs.io/en/latest/)
