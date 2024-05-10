# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:30:18 2024

@author: DELL
"""

from setuptools import setup
from Cython.Build import cythonize
setup(extension_modules = cythonize("goli.pyx"))
