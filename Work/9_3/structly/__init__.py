# structly/__init__.py

# (a) Controlling Exported Symbols

from .structure import *
from .reader import *
from .tableformat import *

# (b) Exporting Everything

__all__ = [*structure.__all__, *reader.__all__, *tableformat.__all__]
