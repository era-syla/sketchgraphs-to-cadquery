import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04992, 0.04655).lineTo(0.0, 0.04655).lineTo(0.0, 0.01052).lineTo(-0.04992, 0.01052).lineTo(-0.04992, 0.04655).close()
solid=wp_sketch0.add(loop0).extrude(0.08222573261304404)
