# -*- coding: utf-8 -*-
"""
Automatic loader for pythonnet(coreclr)
"""

__version__ = "0.1.0"

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


def load(type:Literal["default", "system", "offline"], **params):
    """
    load coreclr automatically with given loader type and additional parameters

    Parameters
    ----------
    - type: type of loader(Literal["default", "system", "offline"])
    """
    if type == "default":
        from .loaders.default import load as _load
    elif type == "system":
        from .loaders.system import load as _load
    elif type == "offline":
        from .loaders.offline import load as _load
    else:
        raise NameError("Unsupported load type!")
    
    _load(**params)

__all__ = [ "load" ]
