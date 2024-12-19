# -*- coding: utf-8 -*-
import os, sys, platform, io, pythonnet
from .. import __path__
from ..assets import resources


def load(**params):
    """
    extract asset binary file and load coreclr automatically with additional parameters
    """

    # check if os supported
    res_name = f"{sys.platform}_{platform.uname().machine}"
    if not res_name in resources.keys():
        raise FileNotFoundError("Unsupported OS!")

    # # check if os supported
    # binary_dir = os.path.join(__path__[0], "assets", sys.platform)
    # if not os.path.exists(binary_dir):
    #     raise FileNotFoundError("Unsupported OS!")

    # get dotnet root path per os
    if sys.platform == "win32":
        dotnet_root = params.pop(
            "dotnet_root",
            os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "autoclr", "dotnet")
        )
    elif sys.platform == "darwin":
        dotnet_root = params.pop(
            "dotnet_root",
            os.path.join(os.path.expanduser("~"), "Library", "Application Support", "autoclr", "dotnet")
        )
    else:
        dotnet_root = params.pop(
            "dotnet_root",
            os.path.join(os.path.expanduser("~"), ".autoclr", "dotnet")
        )

    # check dotnet root directory exists
    if not os.path.exists(dotnet_root):
        # extract file
        if sys.platform == "win32":
            import zipfile

            zipfile.ZipFile(io.BytesIO(resources[res_name]["value"])).extractall(dotnet_root)
        else:
            import tarfile

            tarfile.open(fileobj = io.BytesIO(resources[res_name]["value"])).extractall(dotnet_root)

    # # check dotnet root directory exists
    # if not os.path.exists(dotnet_root):
    #     os.makedirs(os.path.dirname(dotnet_root), exist_ok = True)

    #     binary_file_name = os.path.join(binary_dir, platform.uname().machine)
    #     if sys.platform == "win32":
    #         import zipfile

    #         zip = zipfile.ZipFile(f"{binary_file_name}.zip")
    #         zip.extractall(dotnet_root)
    #         zip.close()
    #     else:
    #         import tarfile

    #         tar = tarfile.open(f"{binary_file_name}.tar.gz")
    #         tar.extractall(dotnet_root)
    #         tar.close()

    pythonnet.load("coreclr", dotnet_root = dotnet_root, **params)
