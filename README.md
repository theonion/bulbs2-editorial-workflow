# bulbs2-editorial-workflow [![Build Status](https://travis-ci.org/theonion/bulbs2-editorial-workflow.svg?branch=master)](https://travis-ci.org/theonion/bulbs2-editorial-workflow)

> do not pass go; do not collect $200

`bulbs2-editorial-workflow` is a companion app to [bulbs2](https://github.com/theonion/bulbs2) that enforces a specific 
publishing workflow. The workflow is as follows:

1. new content is in state _draft_
2. _draft_ content can be sent to the editors, moving it to _waiting for editor_ 
3. _waiting for editor_ content can move to: (a) _approved for publication_ status, or (b) be sent back to the author and back to _draft_ status

This is handled through a Finite State Machine. However, approving content for publication does not automatically 
assign a publication date: that needs to be done separately by the implementation. It also does not contain any logic 
for notification.

Unlike the base `bulbs2`, this is opinionated: hence why is is not in the main package. This is specifically what I 
meant when I said prescriptive code should be refactored to its own repo.

A great example of how this is useful is the distinction of workflow between Onion Studios and The Onion. Both have 
content that needs to be published (so they would rely on the base `bulbs2` dependency), but Onion Studios does __not__ 
need to have an enforced editorial-approval workflow while The Onion does. So, The Onion would add this as a 
dependency and Onion Studios would not. Their base content would still have the same mixins, but The Onion would 
add this to control its approval process.


## Getting the Code

You can clone the code via _git_:

```bash
$ git clone https://github.com/theonion/bulbs2-editorial-workflow.git
```

Alternatively, if you just want to use it in a Django application, you can install it via _pip_:

```bash
$ pip install -e git+https://github.com/theonion/bulbs2-editorial-workflow.git#egg=bulbs2-editorial-workflow
```

__Note:__ since this is a far-afield project that may or may not be brought to production, I am refraining from adding 
it to the PyPI index.


## Testing the Code

To run the tests, clone the repository from GitHub (see steps above). You should then create a virtual environment with 
Python 3 and install the project to that:

```bash
$ cd /path/to/virtualenvs
$ virtualenv -p python3 bulbs2-editorial-workflow
$ source bulbs2/bin/activate
$ cd /path/to/bulbs2-editorial-workflow
$ pip install -e .
$ pip install "file://$(pwd)#egg=bulbs2-editorial-workflow[dev]"
$ py.test tests
```

If you don't have Python 3 on your system, you can _brew_ install it:

```bash
$ brew install python3
$ brew linkapps
```

If you don't have _virtualenv_ on you system, you can _pip_ install that:

```bash
$ pip install virtualenv
```

If you don't have _brew_ installed, you can get that via:

```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you don't have _pip_, install Python 2 and Python 3 via _brew_:

```bash
$ brew install python2 python3
$ brew linkapps
```
