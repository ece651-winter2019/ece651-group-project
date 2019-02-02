# [TAKEN FROM THE BOCADILLO PROJECT]

# Contributing to Bocadillo

## Contents

- [Introduction](#introduction)
- [Getting started](#getting-started)
- [Code style](#code-style)
- [Pull Request process](#pull-request-process)
- [Notes to maintainers](#notes-to-maintainers)

## Introduction

### What is this document about?

Have you found a bug? You'd like to add a new feature or improve the docs? Fantastic news! All contributions are happily welcome.

Here, we point at a few guidelines that you should follow in order to get your contribution accepted.

### Always discuss ideas!

Before submitting any code changes for review, you should first **open an issue** so that maintainers and contributors can discuss it with you.

This step is important because there may be aspects you didn't think about, or there may be ways to expand or focus your suggestions. Eventually, discussing your suggestions with others can only improve the quality of the contribution you'll make.

## Getting started

Bocadillo has a single repository for both the `bocadillo` package and its documentation.

### Configuring the development environment

All development is done on ubuntu 18.04.1 LTS. Assuming you have just installed ubuntu fresh, this section will outline the steps to installing dependencies and tools required for development on the project.  

First update and upgrade the system

```console
sudo apt-get update
sudo apt-get upgrade
```

install required dependencies from apt

```console
sudo apt-get install --assume-yes make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev git mercurial
```
Ubuntu comes with python 3.6 but development will be done using the latest python version 3.7.2. In order to get this version of python it can be built from source using the following commands  

First download the source code
```console
cd ~
mkdir tmp && cd tmp
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
tar xvf Python-3.7.2.tar.xz
cd Python-3.7.2
```

prepare the build
```console
./configure --enable-optimizations --with-ensurepip=install
```

Next build the python programs using make (the -j options allows the build to be done in parallel)
```console
make -j 8
```
Then, you’ll want to install your new version of Python. You’ll use the altinstall target here in order to not overwrite the system’s version of Python. Since you’re installing Python into /usr/local/bin, you’ll need to run as root:

```console
sudo make altinstall
```

Verify the install. The python interpreter should have been installed into /usr/local/bin
```console
/usr/local/bin/python3.7 --version
```

You should be able to simply use
```console
python3.7
```
If this does not find the correct interpreter, you make need to add '/usr/local/bin' to the PATH environment variable.  

Or you could simply add an alias to your .bashrc file
```
alias python="/usr/local/bin/python3.7"
```

Remove the build folder if you like:
```console
cd ~
rm -r ~/tmp
```

### python dependencies

Project dependencies are managed through [Pipenv]. You should install it if you haven't already:

```console
python -m pip install --user pipenv
```
This does user installation and puts pipenv in your `/home/USER_NAME/.local/` folder. This needs to be added to you PATH environment variable to continue

Backup bashrc file
```bash
cp ~/.bashrc ~/.bashrc.old
```
Modify path and reload bashrc
```bash
echo "export PATH=~/.local/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```
Confirm the line has been added to the end of the bashrc file with tail `tail ~/.bashrc`. This should return text containing the line `export PATH=~/.local/bin:$PATH`

Now clone the repo in a location of your choice, then install all the required python packages using pipenv
```console
git clone https://github.com/adkulas/ece651-group-project.git
cd ece651-group-project
pipenv install --dev
```

You should now have a virutal environment with all depencies installed. To activate the virutal environment simply use:
```console
pipenv shell
```


### Setting up for contribution

Here's how to get your copy of the repo ready for development:

- Clone the `ece651-group-project` repo.
- Clone the repo on your computer: `git clone https://github.com/adkulas/ece651-group-project.git`.
- Checkout the `master` branch and grab its latest version: `git pull origin master`.
- Install the project (see installation steps above).
- Create a branch (e.g. `fix/some-bug`) and work on it.
- Push to your remote: `git push origin fix/some-bug`.
- [Open a pull request] and follow the [PR process](#pull-request-process) below.


#### Installing the documentation packages

If you're planning to contribute documentation, you should also install the NPM dependencies. Make sure you have [Node] and [NPM] installed, then run:

```bash
npm install
```

To verify the NPM packages are correctly installed, you can fire up the docs site:

```bash
npm start
```

and access it at http://localhost:8080.

#### Running tests

Before making any changes, you should first run the tests in order to make sure everything is correcly setup.

Bocadillo uses [pytest] as its testing framework. The test suite can be run using:

```bash
pytest
```

To also generate a [coverage] report, run:

```bash
pytest --cov=./
```

### Contributing documentation

There are a few extra things you need to known in order to contribute documentation for Bocadillo.

This section supposes that you have already installed Bocadillo's [documentation dependencies](#installing-the-documentation-packages).

**Note**: Bocadillo's documentation site is made with [VuePress]. You may need to refer to its documentation, although the main problems you'll encounter are listed here.

#### How the documentation is structured

All documentation lives in the `docs/` directory. It is structured as follows:

- `getting-started`: resources for users getting started with Bocadillo.
- `guides`: discussions about key topics and concepts, including background, information and usage hints.
- `how-to`: recipes for solving key problems or addressing specific use cases.
- `discussions`: these give more in-depth background about important topics or activities related to application development.
- `api`: technical reference for Bocadillo's machinery; generated from the modules', classes' and functions' docstrings.

#### Running the docs site

To run the documentation site, run:

```bash
npm start
```

It will be accessible at http://localhost:8080.

The docs site is hot-reloaded on any changes to the contents of the `docs/` directory. The only exception to this is the API Reference (see [Generating the API Reference](#generating-the-api-reference)).

#### Creating documentation pages

To write a new page for the docs, create a new `.md` file in the appropriate directory (see [How the documentation is structured](#how-the-documentation-is-structured)), then add a route in the appropriate `sidebar` configuration in `docs/.vuepress/config.js`.

Feel free to refer to the [VuePress] docs if needed.

#### Generating the API Reference

Bocadillo uses [Pydoc-Markdown] to generate the API reference in Markdown format from Python docstring. The generated `.md` file are then wired up in the `config.js` file.

In order to view the changes you've made to Python dosctrings in the docs site, you'll need to regenerate the API reference:

```bash
pymdoc generate
```

The `docs/api` will be hot-reloaded and the docs site will display the updated API Reference docs.

See `pymdoc.yml` for the configuration details and [Pydoc-Markdown] documentation for usage reference.

#### Debugging the docs site

It may happen that the documentation site does not seem to behave properly.

You should first open your browser's dev tools and check for any errors. VuePress errors generally give enough clues as to what's wrong and how you can fix it.

If there is an issue with VuePress' hot-reloading, you need to close the current tab and open a fresh copy of the docs site in a new tab.

## Code style

### Black formatting

In order to reduce format-related issues and make code reviews more efficient, this repo uses the [Black](https://github.com/ambv/black) auto-formatter to format your code on commit. This is implemented using a [pre-commit](https://pre-commit.com) hook.

To make sure your code is formatted automatically before any commit, run this inside the repo after installing all dependencies:

```shell
pre-commit install
```

In practice, Black may intervene and reformat some of the Python files when committing to your local. When this happens, the commit will abort and you'll need to `git add` files edited by Black and `git commit` again.

If you wish to manually apply Black before a commit, run `$ pre-commit`.

### Type annotations

Bocadillo makes heavy use of type annotations in order to document input and output types of functions and methods, as well as facilitate early detection of bugs.

You are encouraged to provide annotations for each and every function and method you write.

Do:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Don't:

```
def add(x, y):
    return x + y
```

For background on the benefits of type annotations, I recommend Stav Shamir's [The other (great) benefit of Python type annotations](https://medium.com/@shamir.stav_83310/the-other-great-benefit-of-python-type-annotations-896c7d077c6b).

If you need help when writing type annotations, be sure to check out the official documentation of the [typing] module.

### Code documentation

Comments and docstrings are crucial in order to convey key information about the code. You should use them when needed.

Be sure, however, not to over-comment. **Code should be self-documenting**. For example, if you find yourself adding comments to delimit your code, it may be worth refactoring — e.g. into a few descriptively-named functions.

There are 3 types of code documentation you may find yourself using.

#### Module docstrings

All modules should have a descriptive docstring at their top. For example:

```python
"""Exception classes."""

class MyException(Exception):
    pass
```

#### Function, method or class docstrings

Every public function, method or class should have a proper docstring.

The formatting of the docstring is inspired by the [NumPyDoc] style. It should be followed so that your code can be properly picked up by [Pydoc-Markdown] to generate API reference.

Here is an example of a compliant class with its methods:

```python
"""Definition of the Foo class."""
import operator
from functools import reduce


class Foo:
    """Some really cool kind of foo.

    # Parameters
    bar (str): used to configure XYZ.
    """

    def __init__(self, bar: str):
        self._bar = bar

    @property
    def zed(self) -> str:
        """z with an exclamation mark."""
        return 'z!'

    def create_baz(self) -> int:
        """Create `baz` from the current `bar`.

        # Returns
        baz (int): multiplication the ASCII codes for each letter in `bar`.
        """
        return reduce(operator.mul, map(ord, self._bar))
```

#### Comments

A comment is a line that starts with `#`. There are two use cases to comments:

- To explain complex code that may not be easily understood by future developers.
- To explain **why** a portion of code was implemented the way it was.

As a rule of thumb, don't use comments to explain *what* your code is doing, but to explain *why* it's doing what it's doing. Again, code should be self-documenting. If you need to explain *what* your code is doing, try simplifying it into smaller components (functions, methods, objects) with descriptive names.

## Pull Request process

1. Make sure to **open an issue** before submitting a PR (see [Always discuss ideas](#always-discuss-ideas)). Note: not all features can be accepted, as some may be out-of-scope and would be better off as third-party packages. It would be sad if you worked on a PR for days but it gets rejected because of reasons that could have been quickly pointed at if you discussed it in an issue.
2. Ensure your changes are well-commented and you haven't left any commented-out lines of code or debug `print` statements.
3. If your changes imply additions or changes in interface, make sure to the documentation. This includes environment variables, file locations, extra keyword arguments, etc.
4. You must add [tests](#running-tests) for the feature or bug fix you are providing.
5. Your PR must pass the Travis CI builds. It will not be merged if the tests fail.
6. The PR can be merged once it has obtained approval from at least one collaborator or maintainer.

## Notes to maintainers

**This section is solely aimed at maintainers and owners of the Bocadillo repository.**

### Versioning

Versioning is managed through [bumpversion](https://pypi.org/project/bumpversion/).

To update the package's version, use:

```bash
bumpversion "patch | minor | major | post_release"
```

This will create a new commit tagged with the new version.

See [bumpversion official docs](https://pypi.org/project/bumpversion/) for all the available options.

### Releasing

This section documents how to release new versions to PyPI.

#### Testing

It is recommended to make a test release to TestPyPI before releasing a new version to production.

You can do so by pushing to the `release/test` branch.

- Grab the latest version from `master`:

```bash
git checkout release/test
git merge master
```

- If the current version has already been released to TestPyPI, update the package version (see [versioning](#versioning)).

- Push to remote:

```bash
git push
```

#### Production

When ready to release a new version to production:

- Update the package version if necessary (see [versioning](#versioning)).

- Push the tagged commit to remote:

```bash
$ git push --tags
```

[Open a pull request]: https://github.com/bocadilloproject/bocadillo/compare
[type annotations]: https://medium.com/@shamir.stav_83310/the-other-great-benefit-of-python-type-annotations-896c7d077c6b
[typing]: https://docs.python.org/3/library/typing.html
[NumPyDoc]: https://numpydoc.readthedocs.io
[Pydoc-Markdown]: https://niklasrosenstein.github.io/pydoc-markdown/
[Node]: https://nodejs.org/en
[NPM]: https://www.npmjs.com
[Pipenv]: https://github.com/pypa/pipenv
[pytest]: https://docs.pytest.org
[VuePress]: https://vuepress.vuejs.org
[coverage]: https://coverage.readthedocs.io
