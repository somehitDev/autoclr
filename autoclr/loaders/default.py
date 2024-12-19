# -*- coding: utf-8 -*-
import pythonnet


def load(**params):
    """
    load coreclr(using pythonnet.load itself) with given additional parameters
    """

    pythonnet.load("coreclr", **params)
