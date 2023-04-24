# fstflowchat

fstflowchat is a small, pedagogical, fst-based dialog toolkit

https://stackoverflow.com/questions/69970147/how-do-i-resolve-the-pygraphviz-error-on-mac-os

**fstflowchat** is a Python library for making dialog systems using
finite state transducers to control the dialog flow.  It uses graphviz
to visualize the dialog flow and as a graph specification language for
the dialog graph.  Each graph edge specifies two functions, a test
function that determines if the edge is a valid transition, and an
output fuction that determines the system's output as it changes state.


## Installation

Currently the only dependency is the [graphviz
application](https://graphviz.org/download/) and the [pygraphviz
library](https://pygraphviz.github.io/documentation/stable/install.html).
For mac installation issues, please use the following command as
described in this [stackoverflow
question](https://stackoverflow.com/questions/69970147/how-do-i-resolve-the-pygraphviz-error-on-mac-os)



## More Information

For more information, please see the [documentation](https://fstflowchat.readthedocs.io/en/latest/)
