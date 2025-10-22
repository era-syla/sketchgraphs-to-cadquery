import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02582, 0.02205).lineTo(-0.12742, 0.02205).lineTo(-0.12742, -0.07955).lineTo(-0.02582, -0.07955).lineTo(-0.02582, 0.02205).close()
solid=wp_sketch0.add(loop0).extrude(-0.1821071853650457)
