# -*- coding: utf-8 -*-
import os, subprocess, pythonnet


def load(**params):
    """
    load coreclr from system automatically with additional parameters
    """

    dotnet_root = params.pop("dotnet_root", None)

    if dotnet_root is None:
        output = subprocess.check_output([ "dotnet", "--info" ]).decode("utf-8")
        if output == "" or not "Base Path:" in output:
            raise RuntimeError("dotnet is not installed on system!")

        for line in output.strip().split("\n"):
            if line.strip().startswith("Base Path:"):
                dotnet_root = os.path.dirname(line.replace("Base Path:", "").strip())

    try:
        pythonnet.load("coreclr", dotnet_root = dotnet_root, **params)
    except:
        load(dotnet_root = os.path.dirname(dotnet_root), **params)
