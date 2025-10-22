import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05786, -0.04255).lineTo(0.07651, -0.04255).lineTo(0.07651, 0.03685).lineTo(0.04428, 0.03685).lineTo(0.04428, 0.09369).lineTo(-0.05786, 0.09369).lineTo(-0.05786, -0.04255).close()
solid=wp_sketch0.add(loop0).extrude(-0.3647123235980111)
