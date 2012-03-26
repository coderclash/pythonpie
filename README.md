# PythonPie - A Simple JSON API for Safely Running Python Code.

We run your codes.

** Warning, sandbox not implemented. Trust me. Not good. **


### Features

* Uses gevent for fastness.
* Sandboxes python.


### Install/Usage

**Make sure redis is installed and running on the standard ports!**

1. `git clone git@github.com:coderclash/pythonpie.git`
2. `cd pythonpie`
3. `mkvirtualenv pythonpie`
4. `pip install -r requirements`
5. `gunicorn pythonpie:app -b 127.0.0.1:5000`
6. `python tests.py`