# Import Libraries and setup world
from goo import goo
import importlib
import bpy

importlib.reload(goo)
goo.setup_world()

# setup material
goo.add_material_cell("CellGreen", 0.007, 0.300, 0.005)

# Add cells and cell collections
bpy.app.handlers.frame_change_post.clear()
master_coll = bpy.context.view_layer.layer_collection
collection = bpy.context.blend_data.collections.new(name='sphere')
bpy.context.collection.children.link(collection)
bpy.context.view_layer.active_layer_collection = \
bpy.context.view_layer.layer_collection.children['sphere']
goo.make_cell(goo.Cell(name_string="sphere(0, 0, 0)",
                       loc=(0, 0, 0),
                       material="CellGreen"))

# Add handlers for division, growth and adhesion
handlers = goo.handler_class()
handlers.active_cell_types += ['sphere']
handlers.set_division_rate('sphere', 20)
handlers.set_growth_rate('sphere', 20)
bpy.app.handlers.frame_change_post.append(handlers.div_handler)
bpy.app.handlers.frame_change_post.append(handlers.growth_handler)
