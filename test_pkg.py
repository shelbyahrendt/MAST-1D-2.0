'''
Testing all packages are installed as required by the
MAST-1D Quick-Start document by using conda and the partial package list in the
environment.yml file copied here for convenience:
----------------
name: MAST1Dpy36
channels:
  - defaults
dependencies:
  - python=3.6
  - matplotlib
  - numpy
  - pandas
  - xlrd
-----------------

Note: creating the environment using the full package list from the
MAST-1D Quick-Start did not work since many of the packages come
with the python 2.7 installation

'''

import csv
import datetime
import copy #this includes 'deepcopy'
import itertools
import json
import math
import matplotlib
import numpy
import os
import pandas
import pickle
import sys
#import tkfiledialog
import tkinter #this includes filedialog
from tkinter import filedialog
import xlrd
