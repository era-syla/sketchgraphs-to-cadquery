import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07347, -0.07807).lineTo(-0.07572, -0.07807).lineTo(-0.07572, 0.07409).lineTo(0.07347, 0.07409).lineTo(0.07347, -0.07807).close()
solid=wp_sketch0.add(loop0).extrude(0.050697702193836194)
