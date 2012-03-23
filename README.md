# A simple sandboxed Python REST & JSON API.

We run your codes.


### Features

* Uses gevent for fastness.
* Sandboxes python


### Install/Usage

**Make sure redis is installed and running on the standard ports!**

1. `git clone git@github.com:coderclash/pythonpie.git`
2. `cd emailpie`
3. `mkvirtualenv pythonpie`
4. `pip install -r requirements`
5. `python rundev.py`
6. Visit http://localhost:5000/v1/check?email=test@gmail.com
