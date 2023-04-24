# fstflowchat

**fstflowchat** is a small, pedagogical, fst-based dialog toolkit.


fstflowchat uses finite state transducers to control dialog flow.  It
uses graphviz to visualize the dialog flow and as a graph
specification language for the dialog FST.  Each graph edge specifies
two functions, a test function that determines if the edge is a valid
transition, and an output fuction that determines the system's output
as it changes state.


## Installation

To install the development version, run 

```
pip install git+https://github.com/abecode/fstflowchat
```

Currently the development version is preferred.

To run the stable version (in the future), run

```
pip install fstflowchat
```


Currently the only dependency is the [graphviz
application](https://graphviz.org/download/) and the [pygraphviz
library](https://pygraphviz.github.io/documentation/stable/install.html).
For mac installation issues, please use the following command as
described in this [stackoverflow
question](https://stackoverflow.com/questions/69970147/how-do-i-resolve-the-pygraphviz-error-on-mac-os)

```
python -m pip install \
    --global-option=build_ext \
    --global-option="-I$(brew --prefix graphviz)/include/" \
    --global-option="-L$(brew --prefix graphviz)/lib/" \
    pygraphviz
```

## Running a demo

To see a demo, run 

```
fstflowchat-example
```

## Documentation

For more information, please see the [documentation](https://fstflowchat.readthedocs.io/en/latest/)
