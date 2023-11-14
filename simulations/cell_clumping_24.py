# doublet.py - simulates 2 cells adhering to each other
# with different balances of cortical tension and cell adhesion

from goo import goo
import bpy
from importlib import reload
reload(goo)
goo.setup_world()

  
#================== Cell A Collection ==================
# Create a type for cell A
#goo.make_type("A_Cells", type = 'cell')
# Define cell A1
goo.make_cell("cell_A1", loc = (0.1,0,0), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A2", loc = (2,0,0), type = "A_Cells")
# Define cell A3
goo.make_cell("cell_A3", loc = (0,1,1.83), type = "A_Cells")
# Define cell A4
goo.make_cell("cell_A4", loc = (0.74,2.85,-0.57), type = "A_Cells")
# Define cell A3
goo.make_cell("cell_A5", loc = (0,-2,0), type = "A_Cells")
# Define cell A4
goo.make_cell("cell_A6", loc = (-2,0,0), type = "A_Cells")
# Define cell A1
goo.make_cell("cell_A7", loc = (3.39,0.25,0.76), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A8", loc = (2,-2.03,0), type = "A_Cells")
# Define cell A3
goo.make_cell("cell_A9", loc = (0.098,-2.59,1.79), type = "A_Cells")
# Define cell A4
goo.make_cell("cell_A10", loc = (1.67,0.73,2.9), type = "A_Cells")
# Define cell A3
goo.make_cell("cell_A11", loc = (1.11,-2.04,-1.77), type = "A_Cells")
# Define cell A4
goo.make_cell("cell_A12", loc = (-1.15,1,-1.93), type = "A_Cells")

# Define cell A1
goo.make_cell("cell_A13", loc = (2,2,1.4), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A14", loc = (-0.98,1.95,0), type = "A_Cells")
# Define cell A1
goo.make_cell("cell_A15", loc = (0.97,-0.59,1.63), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A16", loc = (2.66,2,-0.57), type = "A_Cells")
# Define cell A1
goo.make_cell("cell_A17", loc = (0.92,1.16,-1.47), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A18", loc = (-1.16,-1,-1.22), type = "A_Cells")

# Define cell A1
goo.make_cell("cell_A19", loc = (-1.07,-0.76,1.58), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A20", loc = (0.1,2.9,1.38), type = "A_Cells")
# Define cell A1
goo.make_cell("cell_A21", loc = (1.9,-2.45,1.9), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A22", loc = (-.19,-.39,3.32), type = "A_Cells")
# Define cell A1
goo.make_cell("cell_A23", loc = (2.74,-0.34,-1.8), type = "A_Cells")
# Define cell A2
goo.make_cell("cell_A24", loc = (-2.1,0.9,1.81), type = "A_Cells")



#================== Force A Collection ==================

strength = -3000
falloff = 0

# Create a type for force A
#goo.make_type("A_Cells", type = 'force')
# Define force A1
goo.make_force("force_A1", "cell_A1", "A_Cells", strength, falloff)
goo.add_motion('cell_A1', -1000)
# Define force A2
goo.make_force("force_A2", "cell_A2", "A_Cells", strength, falloff)
goo.add_motion('cell_A2', -1000)
# Define force A3
goo.make_force("force_A3", "cell_A3", "A_Cells", strength, falloff)
goo.add_motion('cell_A3', -1000)
# Define force A4
goo.make_force("force_A4", "cell_A4", "A_Cells", strength, falloff)
goo.add_motion('cell_A4', -1000)
# Define force A5
goo.make_force("force_A5", "cell_A5", "A_Cells", strength, falloff)
goo.add_motion('cell_A5', -1000)
# Define force A6
goo.make_force("force_A6", "cell_A6", "A_Cells", strength, falloff)
goo.add_motion('cell_A6', -1000)

# Define force A1
goo.make_force("force_A7", "cell_A7", "A_Cells", strength, falloff)
goo.add_motion('cell_A7', -1000)
# Define force A2
goo.make_force("force_A8", "cell_A8", "A_Cells", strength, falloff)
goo.add_motion('cell_A8', -1000)
# Define force A3
goo.make_force("force_A9", "cell_A9", "A_Cells", strength, falloff)
goo.add_motion('cell_A9', -1000)
# Define force A4
goo.make_force("force_A10", "cell_A10", "A_Cells", strength, falloff)
goo.add_motion('cell_A10', -1000)
# Define force A5
goo.make_force("force_A11", "cell_A11", "A_Cells", strength, falloff)
goo.add_motion('cell_A11', -1000)
# Define force A6
goo.make_force("force_A12", "cell_A12", "A_Cells", strength, falloff)
goo.add_motion('cell_A12', -1000)

# Define force A1
goo.make_force("force_A13", "cell_A13", "A_Cells", strength, falloff)
goo.add_motion('cell_A13', -1000)
# Define force A2
goo.make_force("force_A14", "cell_A14", "A_Cells", strength, falloff)
goo.add_motion('cell_A14', -1000)
# Define force A1
goo.make_force("force_A15", "cell_A15", "A_Cells", strength, falloff)
goo.add_motion('cell_A15', -1000)
# Define force A2
goo.make_force("force_A16", "cell_A16", "A_Cells", strength, falloff)
goo.add_motion('cell_A16', -1000)
# Define force A1
goo.make_force("force_A17", "cell_A17", "A_Cells", strength, falloff)
goo.add_motion('cell_A17', -1000)
# Define force A2
goo.make_force("force_A18", "cell_A18", "A_Cells", strength, falloff)
goo.add_motion('cell_A18', -1000)

# Define force A1
goo.make_force("force_A19", "cell_A19", "A_Cells", strength, falloff)
goo.add_motion('cell_A19', -1000)
# Define force A2
goo.make_force("force_A20", "cell_A20", "A_Cells", strength, falloff)
goo.add_motion('cell_A20', -1000)
# Define force A1
goo.make_force("force_A21", "cell_A21", "A_Cells", strength, falloff)
goo.add_motion('cell_A21', -1000)
# Define force A2
goo.make_force("force_A22", "cell_A22", "A_Cells", strength, falloff)
goo.add_motion('cell_A22', -1000)
# Define force A1
goo.make_force("force_A23", "cell_A23", "A_Cells", strength, falloff)
goo.add_motion('cell_A23', -1000)
# Define force A2
goo.make_force("force_A24", "cell_A24", "A_Cells", strength, falloff)
goo.add_motion('cell_A24', -1000)


#================== Simulation setup ==================
handlers = goo.handler_class()
handlers.launch_simulation(start = 1, # default, 1
                           end = 500, # default, 250
                           filepath = "C:\\Users\\anr9744\\Projects\\Goo\\data\\16clump", 
                           adhesion = True, # default, True
                           data = False, # default, False
                           growth = True, 
                           motility = True
                           )