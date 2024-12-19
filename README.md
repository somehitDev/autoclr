<h1 align="center">
    autoclr
</h1>
<p align="center">
    Automatic loader for pythonnet(coreclr)
</p>
<br/>

<div align="center">
    <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue" />
    <br>
    <a href="https://github.com/somehitDev/autoclr/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/somehitDev/autoclr.svg" alt="MIT License" />
    </a>
    <a href="https://pypi.org/project/autoclr/">
        <img src="https://img.shields.io/pypi/v/autoclr" alt="pypi" />
    </a>
</div>
<br/><br/>


## 🎛️ requirements
- python 3.7 or higher
- tested on

|           OS          | Tested | Pass |          Issue         |
| --------------------- | ------ | ---- | ---------------------- |
| Mac 13(Sequoia)       |   ✅   |  ✅  |                        |
| Windows 10(ARM64/UTM) |   ✅   |  ❎  | binary not working     |
| Linux(Ubuntu/ARM)     |   ✅   |  ✅  | arm64, aarch64 support |

<br><br>

## 🌐 install
### - using pip
```zsh
python -m pip install autoclr
```

```zsh
python -m pip install git+https://github.com/somehitDev/autoclr.git
```

<br><br>

## 🛠 usage
```python
from autoclr import load

# default
load("default", **params)
# system
load("system", **params)
# online
load("online", **params)
```
- default
  - call pythonnet.load coreclr and parameters.
- system
  - get dotnet_root from system installed dotnet.
  - if not installed, raise error.
- online
  - extract archive downloaded from dotnet official site and load clr.
- offline
  - not available not.

<br><br>

## Changes
- See [CHANGELOG.md](https://github.com/somehitDev/autoclr/blob/main/CHANGELOG.md)
