import os
from setuptools import setup

# Utility function to read the README file.close# Used for the
# long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put
# a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sinar.myreps",
    version = "0.0.1",
    author = "Khairil Yusof",
    author_email = "khairil.yusof@sinarproject.org",
    description = ("Python library to lookup information on elected "
                        "representatives and boundaries."),
    license = "AGPL",
    keyowrds = "poplus mapit malaysia opengov"
    url = "",
    packages=['sinar.myreps', 'tests'],
    long_description = read('README.md'),
    classifiers[
        ],
)
