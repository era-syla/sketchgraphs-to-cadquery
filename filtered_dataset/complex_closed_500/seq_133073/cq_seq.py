import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00673, -0.05217).lineTo(0.01327, -0.05217).lineTo(0.01327, -0.04217).lineTo(-0.00673, -0.04217).lineTo(-0.00673, -0.05217).close()
solid=wp_sketch0.add(loop0).extrude(0.020091119766546584)
