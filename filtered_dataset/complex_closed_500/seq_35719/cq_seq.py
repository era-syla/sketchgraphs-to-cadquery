import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07874, 0.14241).lineTo(-0.0, 0.14241).lineTo(0.0, -0.07349).lineTo(-0.07874, -0.07349).lineTo(-0.07874, 0.14241).close()
solid=wp_sketch0.add(loop0).extrude(0.2224329724921132)
