# -*- coding: utf-8 -*-
import os, sys, platform, wget, pythonnet


def load(**params):
    architecture = platform.uname().machine.lower()

    # get download url
    download_url = None
    if sys.platform == "win32":
        # if architecture == "x64":
        #     download_url = "https://download.visualstudio.microsoft.com/download/pr/92f9abc6-1e19-40cd-82cf-670be98d3533/46e1346503f4b54418bf9d5f861f1d43/dotnet-runtime-8.0.11-win-x64.zip"
        # elif architecture == "arm64":
        #     download_url = "https://download.visualstudio.microsoft.com/download/pr/3b250d28-7fae-473c-a064-c312c35ca7c8/bc1771d6d4b7dd9dbe6fbb417b9ef1e6/dotnet-runtime-8.0.11-win-arm64.zip"

        # archive_name = "dotnet.zip"
        raise RuntimeError("use `system` loader on windows!")
    elif sys.platform == "linux":
        if architecture == "x64":
            download_url = "https://download.visualstudio.microsoft.com/download/pr/805cdca8-ac43-4d76-8ce8-efd11f1997f2/17aeb8b0cd34c6f8d80217bf6a4ed3cd/dotnet-runtime-8.0.11-linux-x64.tar.gz"
        elif architecture in ( "arm64", "aarch64" ):
            download_url = "https://download.visualstudio.microsoft.com/download/pr/501c5677-1a80-4232-9223-2c1ad336a304/867b5afc628837835a409cf4f465211d/dotnet-runtime-8.0.11-linux-arm64.tar.gz"

        archive_name = "dotnet.tar.gz"
    elif sys.platform == "darwin":
        if architecture == "arm64":
            download_url = "https://download.visualstudio.microsoft.com/download/pr/e5b4d32a-09a7-4028-accb-3b6c51828282/e4ecc94db4507f16a9916dc3be9b6706/dotnet-runtime-8.0.11-osx-arm64.tar.gz"
        elif architecture == "x64":
            download_url = "https://download.visualstudio.microsoft.com/download/pr/f32ae8ed-e8e3-4d1b-8425-852696e4dbe6/1f67d82ebd50b27574ccc4a06b2500b8/dotnet-runtime-8.0.11-osx-x64.tar.gz"

        archive_name = "dotnet.tar.gz"

    if download_url is None:
        raise RuntimeError("Unsupported OS!")
    
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

    os.makedirs(os.path.dirname(dotnet_root), exist_ok = True)

    # check dotnet root directory exists
    if not os.path.exists(dotnet_root):
        # download binary file
        archive_file = os.path.join(os.path.dirname(dotnet_root), archive_name)
        wget.download(download_url, archive_file)
        print("")

        # extract file
        if sys.platform == "win32":
            import zipfile

            zipfile.ZipFile(archive_file).extractall(dotnet_root)
        else:
            import tarfile

            tarfile.open(archive_file).extractall(dotnet_root)

        os.remove(archive_file)

    pythonnet.load("coreclr", dotnet_root = dotnet_root, **params)
