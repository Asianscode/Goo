import sys
import site
from .cell import create_cell, CellType, YolkType, SimpleType
from .reloader import *
from .simulator import Simulator
from .force import create_force
from .division import *
from .handler import *

bl_info = {
    "name": "Goo Add-on",
    "author": "Antoine A. Ruzette, Charles Dai, Sean Megason",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf > Goo Panel",
    "description": "A tool for simulating cellular interactions and dynamics.",
    "warning": "",
    "wiki_url": "https://github.com/smegason/Goo",
    "tracker_url": "https://github.com/smegason/Goo/issues",
    "category": "Simulation",
}
"""solved the addon not showing problem"""
__credits__ = 'Harvard Medical School'
