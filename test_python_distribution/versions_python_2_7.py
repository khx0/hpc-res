# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-04-23
# file: versions_python_2_7.py
##########################################################################################

from subprocess import call
call("python --version", shell = True)

import sys
print "Python sys.version = ", sys.version_info

import numpy as np
print "Numpy version = ", np.__version__

import scipy
print "Scipy version = ", scipy.__version__

import matplotlib as mpl
print "Matplotlib version = ", mpl.__version__

import networkx
print "networkx version = ", networkx.__version__