# Flask Tests
## By Charlie Cook, begun Feb. 22nd, 2021

This project contains a Flask application written in Python that tests various
features of Flask, as well as the Brython module that takes on the job of
Javascript.

Before running, you need to install the `brython` module through pip, or for
example through the AUR, then run the `installBrython.sh` script to download
a copy of `brython.js` into the static directory where it will be served from to
allow for Brython scripts to function.

To run, navigate to the root directory of this project and run `python
flaskHello.py`, then open a web browser to `localhost:5000`. You can then visit
several pages, each outlined in the `add_url_rule` calls in the aforementioned
.py file.
