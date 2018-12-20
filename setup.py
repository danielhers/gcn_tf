#!/usr/bin/env python

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()
with open(os.path.join(here, "requirements")) as f:
    REQUIREMENTS = f.readlines()


setup(name="gcn",
      version="0.1",
      description="Graph Convolutional Layer for Tensorflow",
      long_description=README,
      install_requires=REQUIREMENTS,
      author="Leshem Choshen",
      author_email="leshem.choshen@mail.huji.ac.il",
      url="https://github.com/borgr/gcn_tf",
      license="Apache 2.0",
      py_modules=["gcn", "gcn1"]
      )
