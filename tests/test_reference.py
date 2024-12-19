# -*- coding: utf-8 -*-
from autoclr import load


load("system")

import os, sys
lib_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
sys.path.append(lib_dir)

import clr
clr.AddReference("TestLib")

import TestLib
TestLib.Test.Completed()
