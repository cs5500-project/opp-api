# Quick start

## Prerequisites
* [Install `sqlite3`](https://www.servermania.com/kb/articles/install-sqlite)
  * Hint: MacOS already has `sqlite3` installed

## Installation

* Create a virtual environment
* Activate the virtual environment
* Install the ['required' dependencies](./requirements.txt). You can install each of the dependencies individually, but you can also use [this](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-r).
* Open a terminal to the root of this repo and run the following command:
  * `uvicorn main:app --reload`
  * This command will create your database, if it doesn't already exist, create a web server to host your ReST API's, and automatically reload any code changes to your service.
  * Note, this command runs in the forground, so keep that terminal open or else you won't be able to test your service. 

## Post-Installation

* There are some bugs in this app that you need to resolve before you can use it. Refer to the TODOs section below for hints on how to fix them.
* Open the following URL on a browser of your choice: `http://127.0.0.1:8000/docs`
* Since all the API's are protected, you need to authenicate and authorize yourself. So create a user as the very first thing you do.


# Development

If you want to experiment, break things, and see how the ReST API's behave to changes in code,
make one change to a module, then test an API at `http://127.0.0.1:8000/docs`


HINT: You need to create your own secret key that no one else should know about. You can create a secret key on your own
similar to how to create a password for any account that you create. Or you can use this command to generate a long and robust secret key: ` openssl rand -hex 32`

ANOTHER HINT: You need to choose an algorithm to use to encode your JWT tokens. Here's a [list of algorithms](https://github.com/mpdavis/python-jose/blob/master/jose/constants.py#L4) to choose from. 


### To run this program:
Create venv: python3 -m venv "your venv name (.venv or venv, etc)"</br>
Activate your venv: source "venv-name"/bin/activate</br>
Check your venv: which python</br>
Pip install: pip install -r requirements.txt</br>
Run: uvicorn main:app --reload</br>
